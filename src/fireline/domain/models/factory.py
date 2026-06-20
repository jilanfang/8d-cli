"""Factory experience and data model."""

from datetime import datetime, timezone
from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field


class FactoryMode(StrEnum):
    GENERAL = "general"
    SPECIALIZED = "specialized"


class Pattern(BaseModel):
    phenomenon_type: str
    frequency: str = "medium"
    hit_count: int = 0
    typical_causes: list[dict[str, Any]] = Field(default_factory=list)
    escape_point_patterns: list[dict[str, Any]] = Field(default_factory=list)
    investigation_order: list[str] = Field(default_factory=list)


class ControlPointProfile(BaseModel):
    type: str
    function: str
    location: str
    status: str = "exists"


class TruthChain(BaseModel):
    phenomenon: str
    verified_root_cause: str
    escape_point: str
    control_point_lost: str
    evidence_refs: list[str] = Field(default_factory=list)


class FactoryExperience(BaseModel):
    factory_id: str
    mode: FactoryMode = FactoryMode.GENERAL
    patterns: list[Pattern] = Field(default_factory=list)
    vocabulary: dict[str, str] = Field(default_factory=dict)
    control_point_map: list[ControlPointProfile] = Field(default_factory=list)
    truth_chains: list[TruthChain] = Field(default_factory=list)
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class Factory(BaseModel):
    factory_id: str
    name: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    experience: FactoryExperience
