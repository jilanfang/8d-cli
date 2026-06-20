"""Tests for Report model."""

from fireline.domain.models.report import Report, ReportFormat, ReportSection


def test_create_report():
    r = Report(
        report_id="RPT-1",
        case_id="CASE-1",
        format=ReportFormat.EIGHT_D,
        sections=[
            ReportSection(section_id="full", title="Test", content="content"),
        ],
        confidence=0.8,
    )
    assert r.report_id == "RPT-1"
    assert r.format == ReportFormat.EIGHT_D


def test_report_format_enum():
    assert ReportFormat.EIGHT_D.value == "8d"
    assert ReportFormat.RCA.value == "rca"
    assert ReportFormat.CAPA.value == "capa"


def test_report_defaults():
    r = Report(report_id="RPT-2", case_id="CASE-2")
    assert r.format == ReportFormat.EIGHT_D
    assert r.status == "draft"
    assert r.sections == []
    assert r.confidence == 0.0
