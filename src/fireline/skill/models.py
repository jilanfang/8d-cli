"""Self-contained data models for the 8D Root Cause Coach skill.

These models are intentionally minimal and decoupled from any particular
application, storage, or agent framework. They describe only the state needed
to execute the 8D methodology.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any, Literal


class AnswerStatus(StrEnum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETE = "complete"


@dataclass
class SkillAnswer:
    """A single answer to a question point."""

    value: Any | None = None
    status: Literal["pending", "in_progress", "complete"] = AnswerStatus.PENDING


@dataclass
class SkillEvidenceItem:
    """A piece of evidence referenced by the case."""

    type: str
    ref: str
    summary: str | None = None
    content: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class SkillEvidenceBundle:
    """Collection of evidence items passed to the skill."""

    items: list[SkillEvidenceItem] = field(default_factory=list)

    def summary(self) -> str:
        lines = []
        for item in self.items:
            line = f"- [{item.type}] {item.ref}"
            if item.summary:
                line += f": {item.summary}"
            lines.append(line)
        return "\n".join(lines) if lines else "（暂无证据）"


@dataclass
class SkillPattern:
    """Factory-specific pattern recognized from historical quality data."""

    phenomenon_type: str
    frequency: str = "medium"
    hit_count: int = 0
    typical_causes: list[dict[str, Any]] = field(default_factory=list)
    escape_point_patterns: list[dict[str, Any]] = field(default_factory=list)
    investigation_order: list[str] = field(default_factory=list)


@dataclass
class SkillTruthChain:
    """A previously verified truth chain for a recurring phenomenon."""

    phenomenon: str
    verified_root_cause: str
    escape_point: str
    control_point_lost: str
    evidence_refs: list[str] = field(default_factory=list)


@dataclass
class SkillControlPointProfile:
    """A control point profile for a factory."""

    type: str
    function: str
    location: str
    status: str = "exists"


@dataclass
class SkillExperienceContext:
    """Optional factory-specific experience context injected by the caller."""

    factory_id: str | None = None
    mode: str = "general"
    patterns: list[SkillPattern] = field(default_factory=list)
    vocabulary: dict[str, str] = field(default_factory=dict)
    control_point_map: list[SkillControlPointProfile] = field(default_factory=list)
    truth_chains: list[SkillTruthChain] = field(default_factory=list)


@dataclass
class SkillCaseState:
    """Minimal case state required by the skill.

    Callers (e.g. a CLI or an agent harness) maintain richer case models;
they map to this stripped-down state before invoking the skill.
    """

    case_id: str
    status: str = "d0_d4"
    current_stage: str = "d0"
    answers: dict[str, SkillAnswer] = field(default_factory=dict)
    data_sources: list[dict[str, Any]] = field(default_factory=list)


@dataclass
class SkillInput:
    """Convenience wrapper for Skill inputs."""

    case_state: SkillCaseState
    evidence_bundle: SkillEvidenceBundle
    stage_target: str
    experience_context: SkillExperienceContext | None = None


@dataclass
class SkillOutput:
    """Result of running the skill for a stage_target."""

    stage_output: dict[str, Any]
    gate_status: str
    next_actions: list[str]
    draft_deliverable: str
    confidence: float

    def to_dict(self) -> dict[str, Any]:
        return {
            "stage_output": self.stage_output,
            "gate_status": self.gate_status,
            "next_actions": self.next_actions,
            "draft_deliverable": self.draft_deliverable,
            "confidence": self.confidence,
        }
