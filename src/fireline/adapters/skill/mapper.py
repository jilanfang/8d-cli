"""Map Fireline domain models to the standalone 8D skill models."""

from __future__ import annotations

from typing import Any

from fireline.domain.models.case import Case
from fireline.domain.models.evidence import EvidenceBundle
from fireline.domain.models.factory import FactoryExperience
from fireline.skill.models import (
    SkillAnswer,
    SkillCaseState,
    SkillControlPointProfile,
    SkillEvidenceBundle,
    SkillEvidenceItem,
    SkillExperienceContext,
    SkillPattern,
    SkillTruthChain,
)


def map_case_to_skill(case: Case) -> SkillCaseState:
    """Convert a Fireline Case to the skill's minimal case state."""
    return SkillCaseState(
        case_id=case.case_id,
        status=case.status.value if hasattr(case.status, "value") else str(case.status),
        current_stage=_infer_current_stage(case),
        answers={
            qid: SkillAnswer(value=ans.value, status=ans.status)
            for qid, ans in case.answers.items()
        },
        data_sources=[
            {"type": ds.type, "ref": ds.ref, "summary": ds.summary} for ds in case.data_sources
        ],
    )


def _infer_current_stage(case: Case) -> str:
    status = case.status.value if hasattr(case.status, "value") else str(case.status)
    if status in ("d0_d4",):
        return "d0"
    if status in ("d5_d8",):
        return "d5"
    return "d0"


def map_evidence_to_skill(evidence: EvidenceBundle) -> SkillEvidenceBundle:
    """Convert a Fireline EvidenceBundle to the skill's evidence bundle."""
    return SkillEvidenceBundle(
        items=[
            SkillEvidenceItem(
                type=item.type,
                ref=item.ref,
                summary=item.summary,
                content=item.content,
                metadata=item.metadata,
            )
            for item in evidence.items
        ]
    )


def map_experience_to_skill(experience: FactoryExperience | None) -> SkillExperienceContext | None:
    """Convert a Fireline FactoryExperience to the skill's experience context."""
    if experience is None:
        return None
    return SkillExperienceContext(
        factory_id=experience.factory_id,
        mode=experience.mode.value if hasattr(experience.mode, "value") else str(experience.mode),
        patterns=[
            SkillPattern(
                phenomenon_type=p.phenomenon_type,
                frequency=p.frequency,
                hit_count=p.hit_count,
                typical_causes=p.typical_causes,
                escape_point_patterns=p.escape_point_patterns,
                investigation_order=p.investigation_order,
            )
            for p in experience.patterns
        ],
        vocabulary=experience.vocabulary,
        control_point_map=[
            SkillControlPointProfile(
                type=cp.type,
                function=cp.function,
                location=cp.location,
                status=cp.status,
            )
            for cp in experience.control_point_map
        ],
        truth_chains=[
            SkillTruthChain(
                phenomenon=t.phenomenon,
                verified_root_cause=t.verified_root_cause,
                escape_point=t.escape_point,
                control_point_lost=t.control_point_lost,
                evidence_refs=t.evidence_refs,
            )
            for t in experience.truth_chains
        ],
    )


def update_case_from_skill_output(case: Case, stage_output: dict[str, Any]) -> None:
    """Apply skill output back to a Fireline Case if needed.

    Currently the caller is responsible for persisting answers; this helper
    is a no-op placeholder for future automatic merge logic.
    """
    pass
