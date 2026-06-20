"""Tests for LLM provider registry."""

from fireline.adapters.llm.provider import PROVIDERS, get_provider_spec


def test_registry_not_empty():
    assert len(PROVIDERS) > 0


def test_registry_has_openrouter():
    spec = get_provider_spec("openrouter")
    assert spec is not None
    assert spec.name == "openrouter"


def test_registry_has_deepseek():
    spec = get_provider_spec("deepseek")
    assert spec is not None
    assert spec.name == "deepseek"


def test_provider_spec_has_api_base():
    spec = get_provider_spec("openrouter")
    assert spec is not None
    assert spec.default_api_base is not None
    assert spec.default_api_base.startswith("https://")


def test_get_provider_spec_missing():
    spec = get_provider_spec("nonexistent")
    assert spec is None
