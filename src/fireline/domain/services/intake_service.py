"""Intake service: raw input -> extracted answers + follow-ups."""

from __future__ import annotations

from pathlib import Path

from fireline.adapters.llm.provider import LLMClient
from fireline.adapters.skill.mapper import map_case_to_skill
from fireline.domain.models.case import Case
from fireline.skill.engine import SkillEngine
from fireline.skill.models import SkillEvidenceBundle, SkillEvidenceItem


class IntakeService:
    def __init__(self, llm_client: LLMClient, base_dir: Path | None = None):
        self.engine = SkillEngine(llm_client)
        self.base_dir = base_dir

    async def process(self, raw_input: str, factory_id: str) -> tuple[Case, list[str]]:
        from fireline.adapters.storage.json_store import JsonStore
        from fireline.domain.services.case_service import CaseService

        store = JsonStore(factory_id, base_dir=self.base_dir)
        case_service = CaseService(store)
        case = case_service.create_case(raw_input, factory_id)

        skill_case = map_case_to_skill(case)
        skill_evidence = SkillEvidenceBundle(
            items=[
                SkillEvidenceItem(
                    type="cli_input",
                    ref="new",
                    content=raw_input,
                    summary=raw_input,
                )
            ]
        )
        result = await self.engine.process(skill_case, skill_evidence, "intake")

        extracted = result.stage_output.get("extracted", {})
        for qid, value in extracted.items():
            if value:
                case_service.update_answer(case.case_id, qid, value, status="complete")

        follow_ups = result.stage_output.get("triggered_questions", [])
        return case_service.get_case(case.case_id), follow_ups
