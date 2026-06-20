"""Report model and formats."""

from datetime import datetime, timezone
from enum import StrEnum

from pydantic import BaseModel, Field


class ReportFormat(StrEnum):
    EIGHT_D = "8d"
    RCA = "rca"
    CAPA = "capa"


class ReportSection(BaseModel):
    section_id: str
    title: str
    content: str


class Report(BaseModel):
    report_id: str
    case_id: str
    format: ReportFormat = ReportFormat.EIGHT_D
    status: str = "draft"
    sections: list[ReportSection] = Field(default_factory=list)
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    confidence: float = 0.0
