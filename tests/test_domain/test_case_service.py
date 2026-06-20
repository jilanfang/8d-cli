"""Tests for CaseService."""

import pytest

from fireline.domain.models.case import CaseStatus
from fireline.domain.services.case_service import CaseService


def test_create_case(store):
    svc = CaseService(store)
    case = svc.create_case("测试问题", "test_factory")
    assert case.case_id.startswith("CASE-")
    assert case.factory_id == "test_factory"
    assert case.status == CaseStatus.D0_D4
    assert len(case.history) == 1
    assert case.history[0].action == "new"


def test_get_case_exists(store, base_case):
    svc = CaseService(store)
    case = svc.get_case(base_case.case_id)
    assert case is not None
    assert case.case_id == base_case.case_id


def test_get_case_not_found(store):
    svc = CaseService(store)
    case = svc.get_case("CASE-NONEXISTENT")
    assert case is None


def test_update_answer(store, base_case):
    svc = CaseService(store)
    updated = svc.update_answer(base_case.case_id, "d0-q1", {"phenomenon": "test"})
    assert updated.answers["d0-q1"].value == {"phenomenon": "test"}
    assert updated.answers["d0-q1"].status == "complete"


def test_list_cases(store):
    svc = CaseService(store)
    svc.create_case("case 1", "test_factory")
    svc.create_case("case 2", "test_factory")
    cases = svc.list_cases()
    assert len(cases) >= 2
    assert all(c.factory_id == "test_factory" for c in cases)


def test_case_id_increments(store):
    svc = CaseService(store)
    c1 = svc.create_case("a", "test_factory")
    c2 = svc.create_case("b", "test_factory")
    assert c1.case_id != c2.case_id


def test_update_answer_adds_history(store, base_case):
    svc = CaseService(store)
    updated = svc.update_answer(base_case.case_id, "d2-q1", "客户反馈USB无输出")
    history_entries = [h for h in updated.history if h.action == "answer"]
    assert len(history_entries) >= 1
    assert history_entries[-1].question_id == "d2-q1"


def test_update_answer_nonexistent_case_raises(store):
    svc = CaseService(store)
    with pytest.raises(ValueError, match="Case not found"):
        svc.update_answer("CASE-NONEXISTENT", "d0-q1", {"x": 1})


def test_create_case_has_close_reason_none(store):
    svc = CaseService(store)
    case = svc.create_case("新问题", "test_factory")
    assert case.close_reason is None
