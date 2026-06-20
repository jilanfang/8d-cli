"""Report generation service."""

from __future__ import annotations

from eight_d_coach.deliverables import DeliverableBuilder

from fireline.adapters.skill.mapper import map_case_to_skill
from fireline.domain.models.case import Case
from fireline.domain.models.report import Report, ReportFormat, ReportSection


class ReportService:
    def __init__(self):
        self.builder = DeliverableBuilder()

    def generate(self, case: Case, report_format: str = "8d") -> Report:
        fmt = ReportFormat(report_format)
        skill_case = map_case_to_skill(case)
        content = self.builder.build_full_report(skill_case, fmt.value)
        sections = [
            ReportSection(section_id="full", title="完整报告", content=content),
        ]
        return Report(
            report_id=f"RPT-{case.case_id}",
            case_id=case.case_id,
            format=fmt,
            sections=sections,
            confidence=0.7,
        )
