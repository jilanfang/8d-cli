"""Tests for D4AnalysisService."""

import pytest

from fireline.domain.services.d4_service import D4AnalysisService


@pytest.mark.asyncio
async def test_analyze_sequence(mock_llm_client, base_case):
    svc = D4AnalysisService(mock_llm_client)
    results = await svc.analyze(base_case, None)
    assert "d4-q2" in results
    assert "d4-q3" in results
    assert "d4-q4" in results
    for qid, result in results.items():
        assert result["question_id"] == qid
        assert "stage_output" in result


@pytest.mark.asyncio
async def test_analyze_with_experience(mock_llm_client, base_case, factory_experience):
    svc = D4AnalysisService(mock_llm_client)
    results = await svc.analyze(base_case, factory_experience)
    assert len(results) == 3


@pytest.mark.asyncio
async def test_analyze_returns_three_questions(mock_llm_client, base_case):
    svc = D4AnalysisService(mock_llm_client)
    results = await svc.analyze(base_case, None)
    assert set(results.keys()) == {"d4-q2", "d4-q3", "d4-q4"}


@pytest.mark.asyncio
async def test_analyze_each_result_has_gate_status(mock_llm_client, base_case):
    svc = D4AnalysisService(mock_llm_client)
    results = await svc.analyze(base_case, None)
    for result in results.values():
        assert "gate_status" in result
        assert result["gate_status"] in ("passed", "blocked")


@pytest.mark.asyncio
async def test_analyze_each_result_has_confidence(mock_llm_client, base_case):
    svc = D4AnalysisService(mock_llm_client)
    results = await svc.analyze(base_case, None)
    for result in results.values():
        assert "confidence" in result
        assert 0.0 <= result["confidence"] <= 1.0
