"""Core case model for 8D investigations."""

from datetime import datetime, timezone
from enum import StrEnum
from typing import Any, Literal, Self

from pydantic import BaseModel, Field, model_validator


class CaseStatus(StrEnum):
    D0_D4 = "d0_d4"
    D5_D8 = "d5_d8"
    CLOSED = "closed"


class CloseReason(StrEnum):
    NORMAL = "normal"
    EARLY = "early"
    CANCELLED = "cancelled"


class DataSource(BaseModel):
    type: str
    ref: str
    summary: str | None = None


class HistoryEntry(BaseModel):
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    action: str
    question_id: str | None = None
    input: str | None = None


class Answer(BaseModel):
    value: Any | None = None
    status: Literal["pending", "in_progress", "complete"] = "pending"
    updated_at: datetime | None = None


class Case(BaseModel):
    case_id: str
    status: CaseStatus = CaseStatus.D0_D4
    close_reason: CloseReason | None = None
    factory_id: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    data_sources: list[DataSource] = Field(default_factory=list)
    answers: dict[str, Answer] = Field(default_factory=dict)
    history: list[HistoryEntry] = Field(default_factory=list)

    @model_validator(mode="after")
    def ensure_updated_at(self) -> Self:
        if self.updated_at is None:
            self.updated_at = self.created_at
        return self

    def set_answer(
        self,
        question_id: str,
        value: Any,
        status: Literal["pending", "in_progress", "complete"] = "complete",
    ) -> None:
        self.answers[question_id] = Answer(
            value=value,
            status=status,
            updated_at=datetime.now(timezone.utc),
        )
        self.updated_at = datetime.now(timezone.utc)

    def add_history(
        self, action: str, question_id: str | None = None, input_text: str | None = None
    ) -> None:
        self.history.append(
            HistoryEntry(
                action=action,
                question_id=question_id,
                input=input_text,
            )
        )
        self.updated_at = datetime.now(timezone.utc)
