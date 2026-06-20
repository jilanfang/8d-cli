"""Question guidance service."""

from __future__ import annotations

from typing import Any

from fireline.adapters.llm.provider import LLMClient
from fireline.adapters.skill.mapper import (
    map_case_to_skill,
    map_evidence_to_skill,
    map_experience_to_skill,
)
from fireline.domain.models.case import Case
from fireline.domain.models.evidence import EvidenceBundle, EvidenceItem
from fireline.domain.models.factory import FactoryExperience
from fireline.skill.engine import SkillEngine
from fireline.skill.question_catalog import QuestionCatalog


class QuestionService:
    def __init__(self, llm_client: LLMClient):
        self.engine = SkillEngine(llm_client)

    async def guide(
        self,
        case: Case,
        question_id: str,
        experience: FactoryExperience | None = None,
    ) -> dict[str, Any]:
        QuestionCatalog.get(question_id)  # validate
        evidence = self._build_evidence(case)
        skill_case = map_case_to_skill(case)
        skill_evidence = map_evidence_to_skill(evidence)
        skill_experience = map_experience_to_skill(experience)
        result = await self.engine.process(
            skill_case, skill_evidence, question_id, skill_experience
        )
        return {
            "question_id": question_id,
            "prompt_text": result.draft_deliverable,
            "stage_output": result.stage_output,
            "gate_status": result.gate_status,
            "next_actions": result.next_actions,
            "confidence": result.confidence,
        }

    def _build_evidence(self, case: Case) -> EvidenceBundle:
        items = []
        for ds in case.data_sources:
            items.append(
                EvidenceItem(
                    type=ds.type,
                    ref=ds.ref,
                    summary=ds.summary or "",
                    content=ds.summary or "",
                )
            )
        return EvidenceBundle(items=items)
