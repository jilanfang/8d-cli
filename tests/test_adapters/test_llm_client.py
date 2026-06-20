"""Tests for LLM client JSON parsing and retry behavior."""

from unittest.mock import AsyncMock, MagicMock

import pytest

from fireline.adapters.llm.client import LLMClientError, OpenAICompatibleClient
from fireline.config.schema import LLMConfig


@pytest.fixture
def config():
    return LLMConfig(provider="openrouter", model="deepseek/deepseek-chat", api_key="test-key")


async def test_complete_returns_json_on_valid_response(config):
    client = OpenAICompatibleClient(config)
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = '{"answer": "ok"}'
    client.client = MagicMock()
    client.client.chat.completions.create = AsyncMock(return_value=mock_response)

    result = await client.complete("prompt")
    assert result == {"answer": "ok"}


async def test_complete_retries_on_invalid_json_then_succeeds(config):
    client = OpenAICompatibleClient(config)
    bad_response = MagicMock()
    bad_response.choices = [MagicMock()]
    bad_response.choices[0].message.content = "not json"

    good_response = MagicMock()
    good_response.choices = [MagicMock()]
    good_response.choices[0].message.content = '{"answer": "ok"}'

    client.client = MagicMock()
    client.client.chat.completions.create = AsyncMock(side_effect=[bad_response, good_response])

    result = await client.complete("prompt")
    assert result == {"answer": "ok"}
    assert client.client.chat.completions.create.call_count == 2


async def test_complete_raises_after_two_failures(config):
    client = OpenAICompatibleClient(config)
    bad_response = MagicMock()
    bad_response.choices = [MagicMock()]
    bad_response.choices[0].message.content = "not json"

    client.client = MagicMock()
    client.client.chat.completions.create = AsyncMock(return_value=bad_response)

    with pytest.raises(LLMClientError):
        await client.complete("prompt")
    assert client.client.chat.completions.create.call_count == 2
