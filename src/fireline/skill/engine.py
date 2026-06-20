"""Skill engine — orchestrates 8D methodology via embedded 8d-guru prompts."""

from __future__ import annotations

import json
from typing import Any

from fireline.adapters.llm.provider import LLMClient
from fireline.skill.causal import chain_confidence, validate_escape_chain, validate_why_chain
from fireline.skill.deliverables import DeliverableBuilder
from fireline.skill.gates import GateValidator
from fireline.skill.guru_loader import GuruDataLoader
from fireline.skill.models import (
    SkillCaseState,
    SkillEvidenceBundle,
    SkillExperienceContext,
    SkillOutput,
)
from fireline.skill.question_catalog import QuestionCatalog


def _serialize_case(case_state: SkillCaseState) -> dict[str, Any]:
    return {
        "case_id": case_state.case_id,
        "status": case_state.status,
        "current_stage": case_state.current_stage,
        "answers": {qid: a.value for qid, a in case_state.answers.items()},
    }


def _serialize_evidence(evidence: SkillEvidenceBundle) -> list[dict[str, Any]]:
    return [
        {"type": i.type, "ref": i.ref, "summary": i.summary, "content": i.content}
        for i in evidence.items
    ]


def _format_experience(experience: SkillExperienceContext | None) -> str:
    if experience is None:
        return ""
    parts: list[str] = []
    if experience.patterns:
        parts.append("### 历史质量模式\n")
        for p in experience.patterns:
            parts.append(f"- **{p.phenomenon_type}**（频次: {p.frequency}, 命中: {p.hit_count}）")
    if experience.truth_chains:
        parts.append("\n### 已验证 Truth Chain\n")
        for t in experience.truth_chains:
            parts.append(f"- {t.phenomenon} → 根因: {t.verified_root_cause}")
    return "\n".join(parts)


class SkillEngine:
    """Stateless 8D methodology engine.

    Reads prompts from embedded 8d-guru markdown (bundled as package data),
    injects case state and factory experience context, calls the LLM, runs
    deterministic gate / 5-Why / Escape Point validation, and returns
    structured output.
    """

    def __init__(self, llm_client: LLMClient):
        self.llm_client = llm_client
        self.guru = GuruDataLoader()
        self.gate_validator = GateValidator()
        self.deliverable_builder = DeliverableBuilder()

    async def process(
        self,
        case_state: SkillCaseState,
        evidence_bundle: SkillEvidenceBundle,
        stage_target: str,
        experience_context: SkillExperienceContext | None = None,
    ) -> SkillOutput:
        """Run the skill for a given stage_target (question id or ``"intake"``)."""
        if stage_target == "intake":
            return await self._process_intake(case_state, evidence_bundle)

        return await self._process_question(
            case_state, evidence_bundle, stage_target, experience_context
        )

    # ── question guidance ──────────────────────────────────────────

    async def _process_question(
        self,
        case_state: SkillCaseState,
        evidence_bundle: SkillEvidenceBundle,
        stage_target: str,
        experience_context: SkillExperienceContext | None = None,
    ) -> SkillOutput:
        QuestionCatalog.get(stage_target)  # validate question exists

        prompt = self.guru.assemble_question_prompt(
            stage_target,
            _serialize_case(case_state),
            _serialize_evidence(evidence_bundle),
            _format_experience(experience_context),
        )

        llm_result = await self.llm_client.complete(prompt, json_mode=True)
        stage_output = self._normalize_output(llm_result)

        gate_status, blockers = self._check_gate(case_state, stage_target)
        if stage_target in ("d4-q2", "d4-q3", "d4-q4", "d4-q6"):
            gate_status, blockers = self._apply_d4_validation(
                stage_target, stage_output, gate_status, blockers
            )

        next_actions = self._suggest_next(case_state, stage_target, gate_status, blockers)
        draft = self.deliverable_builder.build_for_question(stage_target, stage_output, case_state)
        confidence = self._compute_confidence(stage_output, gate_status, case_state)

        return SkillOutput(
            stage_output=stage_output,
            gate_status=gate_status,
            next_actions=next_actions,
            draft_deliverable=draft,
            confidence=confidence,
        )

    # ── intake ──────────────────────────────────────────────────────

    async def _process_intake(
        self,
        case_state: SkillCaseState,
        evidence_bundle: SkillEvidenceBundle,
    ) -> SkillOutput:
        raw_input = evidence_bundle.items[0].content if evidence_bundle.items else ""
        prompt = self.guru.assemble_intake_prompt(raw_input, _serialize_case(case_state))

        llm_result = await self.llm_client.complete(prompt, json_mode=True)

        extracted = llm_result.get("extracted", {})
        routing = llm_result.get("routing", {})
        triggered = (
            routing.get("triggered_questions", [])
            if isinstance(routing, dict)
            else []
        ) or llm_result.get("triggered_questions", [])

        return SkillOutput(
            stage_output={
                "extracted": extracted,
                "triggered_questions": triggered,
                "confidence": llm_result.get("confidence", 0.5),
            },
            gate_status="passed",
            next_actions=triggered,
            draft_deliverable="## Intake 提取结果\n\n"
            + json.dumps(extracted, ensure_ascii=False, indent=2),
            confidence=llm_result.get("confidence", 0.5),
        )

    # ── helpers ─────────────────────────────────────────────────────

    @staticmethod
    def _normalize_output(llm_result: dict[str, Any]) -> dict[str, Any]:
        if not isinstance(llm_result, dict):
            return {"raw": llm_result, "confidence": 0.0}
        llm_result.setdefault("confidence", 0.5)
        return llm_result

    def _check_gate(
        self, case: SkillCaseState, stage_target: str
    ) -> tuple[str, list[str]]:
        target_stage = stage_target.split("-")[0]
        result = self.gate_validator.check(case, target_stage)
        if result.passed:
            return "passed", []
        return "blocked", result.blockers

    def _apply_d4_validation(
        self,
        stage_target: str,
        stage_output: dict[str, Any],
        gate_status: str,
        blockers: list[str],
    ) -> tuple[str, list[str]]:
        if stage_target == "d4-q3":
            result = validate_why_chain(stage_output.get("why_chain", []))
            if not result.valid:
                blockers.extend(result.reasons)
                gate_status = "blocked"
        elif stage_target == "d4-q4":
            result = validate_escape_chain(stage_output.get("escape_chain", []))
            if not result.valid:
                blockers.extend(result.reasons)
                gate_status = "blocked"
        return gate_status, blockers

    def _suggest_next(
        self,
        case: SkillCaseState,
        stage_target: str,
        gate_status: str,
        blockers: list[str],
    ) -> list[str]:
        if gate_status == "blocked":
            return [f"先解决 gate 阻断: {b}" for b in blockers]
        next_q = QuestionCatalog.next_incomplete(
            {qid: {"status": a.status} for qid, a in case.answers.items()},
            stage=stage_target.split("-")[0],
        )
        if next_q:
            return [f"继续回答 {next_q.id} ({next_q.name})"]
        return [f"{stage_target.split('-')[0].upper()} 阶段问题点已填满，可尝试 advance"]

    @staticmethod
    def _compute_confidence(
        stage_output: dict[str, Any],
        gate_status: str,
        case: SkillCaseState,
    ) -> float:
        base = stage_output.get("confidence", 0.5)
        if gate_status == "blocked":
            base *= 0.7
        why_chain = stage_output.get("why_chain", [])
        escape_chain = stage_output.get("escape_chain")
        base = min(base, chain_confidence(why_chain, escape_chain))
        return round(max(0.0, min(1.0, base)), 2)
