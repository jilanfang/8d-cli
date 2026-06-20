"""Tests for Case model."""

from fireline.domain.models.case import Answer, Case


def test_case_creation():
    case = Case(case_id="CASE-TEST-001", factory_id="factory_default")
    assert case.case_id == "CASE-TEST-001"
    assert case.factory_id == "factory_default"
    assert case.status.value == "d0_d4"


def test_set_answer():
    case = Case(case_id="CASE-TEST-002", factory_id="factory_default")
    case.set_answer("d0-q1", "USB接口无输出")
    assert "d0-q1" in case.answers
    assert case.answers["d0-q1"].status == "complete"
    assert case.answers["d0-q1"].value == "USB接口无输出"


def test_answer_serialization():
    answer = Answer(value="test", status="complete")
    data = answer.model_dump()
    assert data["value"] == "test"
    assert data["status"] == "complete"
