"""Tests for ReportService."""

import pytest

from fireline.domain.models.report import ReportFormat
from fireline.domain.services.report_service import ReportService


def test_generate_8d_empty(base_case):
    svc = ReportService()
    report = svc.generate(base_case, "8d")
    assert report.case_id == base_case.case_id
    assert report.format == ReportFormat.EIGHT_D
    assert len(report.sections) == 1
    assert "未填写" in report.sections[0].content


def test_generate_8d_partial(case_with_answers):
    svc = ReportService()
    report = svc.generate(case_with_answers, "8d")
    assert "D1" in report.sections[0].content


def test_generate_rca(base_case):
    svc = ReportService()
    report = svc.generate(base_case, "rca")
    assert report.format == ReportFormat.RCA


def test_generate_capa(base_case):
    svc = ReportService()
    report = svc.generate(base_case, "capa")
    assert report.format == ReportFormat.CAPA


def test_generate_invalid_format(base_case):
    svc = ReportService()
    with pytest.raises(ValueError):
        svc.generate(base_case, "invalid_format")


def test_generate_default_format_is_8d(base_case):
    svc = ReportService()
    report = svc.generate(base_case)
    assert report.format == ReportFormat.EIGHT_D


def test_report_has_report_id(base_case):
    svc = ReportService()
    report = svc.generate(base_case)
    assert report.report_id.startswith("RPT-")
    assert report.case_id in report.report_id


def test_report_has_confidence(base_case):
    svc = ReportService()
    report = svc.generate(base_case)
    assert 0.0 <= report.confidence <= 1.0
