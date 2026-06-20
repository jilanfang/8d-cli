"""Tests for GateService advancement logic."""

import pytest

from fireline.domain.models.case import Case, CaseStatus
from fireline.domain.services.gate_service import GateService


@pytest.fixture
def gate_service():
    return GateService()


def test_d5_d8_blocked_when_d1_missing(gate_service):
    case = Case(case_id="CASE-G1", factory_id="factory_default")
    passed, blockers = gate_service.can_advance(case, CaseStatus.D5_D8)
    assert not passed
    assert any("D1 缺少 Owner" in b for b in blockers)


def test_d5_d8_blocked_when_d2_missing(gate_service):
    case = Case(case_id="CASE-G2", factory_id="factory_default")
    case.set_answer("d1-q1", "李四")
    case.set_answer("d1-q2", "王五")
    case.set_answer("d1-q3", "张三")
    passed, blockers = gate_service.can_advance(case, CaseStatus.D5_D8)
    assert not passed
    assert any("D2" in b for b in blockers)


def test_d5_d8_blocked_when_d3_missing(gate_service):
    case = Case(case_id="CASE-G3", factory_id="factory_default")
    case.set_answer("d1-q1", "李四")
    case.set_answer("d1-q2", "王五")
    case.set_answer("d1-q3", "张三")
    case.set_answer("d2-q1", "客户反馈USB无输出")
    case.set_answer("d2-q4", "USB模块A1")
    case.set_answer("d2-q5", {"impact_qty": 100})
    passed, blockers = gate_service.can_advance(case, CaseStatus.D5_D8)
    assert not passed
    assert any("D3" in b for b in blockers)


def test_d5_d8_blocked_when_d4_missing(gate_service):
    case = Case(case_id="CASE-G4", factory_id="factory_default")
    case.set_answer("d1-q1", "李四")
    case.set_answer("d1-q2", "王五")
    case.set_answer("d1-q3", "张三")
    case.set_answer("d2-q1", "客户反馈USB无输出")
    case.set_answer("d2-q4", "USB模块A1")
    case.set_answer("d2-q5", {"impact_qty": 100})
    case.set_answer("d3-q1", {"customer_field_risk": True})
    case.set_answer("d3-q2", {"in_transit_risk": False})
    passed, blockers = gate_service.can_advance(case, CaseStatus.D5_D8)
    assert not passed
    assert any("D4" in b for b in blockers)


def test_d5_d8_passes_when_d1_d4_complete(gate_service):
    case = Case(case_id="CASE-G5", factory_id="factory_default")
    case.set_answer("d1-q1", "李四")
    case.set_answer("d1-q2", "王五")
    case.set_answer("d1-q3", "张三")
    case.set_answer("d2-q1", "客户反馈USB无输出")
    case.set_answer("d2-q4", "USB模块A1")
    case.set_answer("d2-q5", {"impact_qty": 100})
    case.set_answer("d3-q1", {"customer_field_risk": True})
    case.set_answer("d3-q2", {"in_transit_risk": False})
    case.set_answer("d4-q2", {"candidate_causes": []})
    case.set_answer("d4-q3", {"root_cause": "焊点开裂"})
    case.set_answer("d4-q4", {"primary_escape_point": "ATE"})
    case.set_answer("d4-q6", {"control_point": "回流炉"})
    passed, blockers = gate_service.can_advance(case, CaseStatus.D5_D8)
    assert passed
    assert blockers == []


def test_closed_blocked_without_d6(gate_service):
    case = Case(case_id="CASE-G6", factory_id="factory_default")
    case.set_answer("d1-q1", "李四")
    case.set_answer("d1-q2", "王五")
    case.set_answer("d1-q3", "张三")
    case.set_answer("d2-q1", "客户反馈USB无输出")
    case.set_answer("d2-q4", "USB模块A1")
    case.set_answer("d2-q5", {"impact_qty": 100})
    case.set_answer("d3-q1", {"customer_field_risk": True})
    case.set_answer("d3-q2", {"in_transit_risk": False})
    case.set_answer("d4-q2", {"candidate_causes": []})
    case.set_answer("d4-q3", {"root_cause": "焊点开裂"})
    case.set_answer("d4-q4", {"primary_escape_point": "ATE"})
    case.set_answer("d4-q6", {"control_point": "回流炉"})
    passed, blockers = gate_service.can_advance(case, CaseStatus.CLOSED)
    assert not passed
    assert any("D6" in b for b in blockers)


def test_closed_passes_with_d6(gate_service):
    case = Case(case_id="CASE-G7", factory_id="factory_default")
    case.set_answer("d1-q1", "李四")
    case.set_answer("d1-q2", "王五")
    case.set_answer("d1-q3", "张三")
    case.set_answer("d2-q1", "客户反馈USB无输出")
    case.set_answer("d2-q4", "USB模块A1")
    case.set_answer("d2-q5", {"impact_qty": 100})
    case.set_answer("d3-q1", {"customer_field_risk": True})
    case.set_answer("d3-q2", {"in_transit_risk": False})
    case.set_answer("d4-q2", {"candidate_causes": []})
    case.set_answer("d4-q3", {"root_cause": "焊点开裂"})
    case.set_answer("d4-q4", {"primary_escape_point": "ATE"})
    case.set_answer("d4-q6", {"control_point": "回流炉"})
    case.set_answer("d6-q4", {"verified": True})
    passed, blockers = gate_service.can_advance(case, CaseStatus.CLOSED)
    assert passed
    assert blockers == []
