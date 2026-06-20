"""Tests for QuestionService."""

import pytest

from fireline.domain.services.question_service import QuestionService


@pytest.mark.asyncio
async def test_guide_mock_d0(mock_llm_client, base_case, evidence_bundle):
    svc = QuestionService(mock_llm_client)
    result = await svc.guide(base_case, "d0-q1")
    assert result["question_id"] == "d0-q1"
    assert "stage_output" in result
    assert "gate_status" in result
    assert "prompt_text" in result
    assert "next_actions" in result
    assert "confidence" in result


@pytest.mark.asyncio
async def test_guide_mock_d4(mock_llm_client, base_case, evidence_bundle):
    svc = QuestionService(mock_llm_client)
    result = await svc.guide(base_case, "d4-q3")
    assert result["question_id"] == "d4-q3"
    assert "stage_output" in result


@pytest.mark.asyncio
async def test_guide_invalid_qid(mock_llm_client, base_case, evidence_bundle):
    svc = QuestionService(mock_llm_client)
    with pytest.raises(KeyError):
        await svc.guide(base_case, "invalid-q99")


@pytest.mark.asyncio
async def test_guide_with_experience(
    mock_llm_client, base_case, evidence_bundle, factory_experience
):
    svc = QuestionService(mock_llm_client)
    result = await svc.guide(base_case, "d0-q1", experience=factory_experience)
    assert "stage_output" in result


@pytest.mark.asyncio
async def test_guide_all_d_stages(mock_llm_client, base_case, evidence_bundle):
    """Each D stage has at least one question that works."""
    svc = QuestionService(mock_llm_client)
    stages = [
        "d0-q1", "d1-q1", "d2-q1", "d3-q1",
        "d4-q1", "d5-q1", "d6-q1", "d7-q1", "d8-q1",
    ]
    for qid in stages:
        result = await svc.guide(base_case, qid)
        assert result["question_id"] == qid


@pytest.mark.asyncio
async def test_guide_returns_gate_status_string(mock_llm_client, base_case, evidence_bundle):
    svc = QuestionService(mock_llm_client)
    result = await svc.guide(base_case, "d0-q1")
    assert result["gate_status"] in ("passed", "blocked")


@pytest.mark.asyncio
async def test_guide_confidence_in_range(mock_llm_client, base_case, evidence_bundle):
    svc = QuestionService(mock_llm_client)
    result = await svc.guide(base_case, "d0-q1")
    assert 0.0 <= result["confidence"] <= 1.0
