"""Tests for IntakeService."""

from pathlib import Path

import pytest

from fireline.adapters.llm.client import MockLLMClient
from fireline.adapters.storage.json_store import JsonStore
from fireline.domain.services.case_service import CaseService
from fireline.domain.services.intake_service import IntakeService


@pytest.fixture
def mock_client():
    return MockLLMClient(
        {
            "extracted": {"d1-q1": "李四"},
            "triggered_questions": ["d0-q3"],
        }
    )


@pytest.mark.asyncio
async def test_intake_writes_to_provided_base_dir(tmp_path: Path, mock_client):
    service = IntakeService(mock_client, base_dir=tmp_path)
    case, follow_ups = await service.process("客户反馈USB无输出", "factory_intake_test")

    assert case.case_id.startswith("CASE-")
    assert case.factory_id == "factory_intake_test"
    assert "d0-q3" in follow_ups

    # The case must be readable from the same base_dir without extra path hints.
    store = JsonStore("factory_intake_test", base_dir=tmp_path)
    loaded = store.load_case(case.case_id)
    assert loaded is not None
    assert loaded.case_id == case.case_id

    # d1-q1 extracted value should have been saved.
    case_service = CaseService(store)
    fetched = case_service.get_case(case.case_id)
    assert fetched.answers["d1-q1"].value == "李四"


@pytest.mark.asyncio
async def test_intake_does_not_write_to_home_by_default_when_base_dir_given(
    tmp_path: Path, mock_client
):
    service = IntakeService(mock_client, base_dir=tmp_path)
    case, _ = await service.process("客户反馈USB无输出", "factory_intake_test")

    home_store = JsonStore("factory_intake_test")
    assert not home_store.case_exists(case.case_id)
