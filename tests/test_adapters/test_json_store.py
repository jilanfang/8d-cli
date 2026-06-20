"""Tests for JSON storage adapter."""

from pathlib import Path

from fireline.adapters.storage.json_store import JsonStore
from fireline.domain.models.case import Case
from fireline.domain.models.factory import FactoryExperience


def test_save_and_load_case(tmp_path: Path):
    store = JsonStore("factory_test", base_dir=tmp_path)
    case = Case(case_id="CASE-TEST-001", factory_id="factory_test")
    store.save_case(case)
    loaded = store.load_case("CASE-TEST-001")
    assert loaded is not None
    assert loaded.case_id == "CASE-TEST-001"


def test_list_cases(tmp_path: Path):
    store = JsonStore("factory_test", base_dir=tmp_path)
    store.save_case(Case(case_id="CASE-A", factory_id="factory_test"))
    store.save_case(Case(case_id="CASE-B", factory_id="factory_test"))
    cases = store.list_cases()
    assert set(cases) == {"CASE-A", "CASE-B"}


def test_factory_isolation(tmp_path: Path):
    store_a = JsonStore("factory_a", base_dir=tmp_path)
    store_b = JsonStore("factory_b", base_dir=tmp_path)
    store_a.save_case(Case(case_id="CASE-1", factory_id="factory_a"))
    store_b.save_case(Case(case_id="CASE-1", factory_id="factory_b"))
    assert store_a.load_case("CASE-1").factory_id == "factory_a"
    assert store_b.load_case("CASE-1").factory_id == "factory_b"


def test_save_and_load_experience(tmp_path: Path):
    store = JsonStore("factory_test", base_dir=tmp_path)
    exp = FactoryExperience(factory_id="factory_test")
    store.save_experience(exp)
    loaded = store.load_experience()
    assert loaded is not None
    assert loaded.factory_id == "factory_test"
