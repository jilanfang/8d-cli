"""LLM provider abstractions."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ProviderSpec:
    name: str
    env_key: str
    default_api_base: str
    is_gateway: bool = False


class LLMClient(ABC):
    """Abstract LLM client."""

    @abstractmethod
    async def complete(
        self, prompt: str, json_mode: bool = True, temperature: float | None = None
    ) -> dict[str, Any]:
        """Send prompt and return parsed JSON dict."""
        ...


# Simplified registry for Phase 1.
PROVIDERS: tuple[ProviderSpec, ...] = (
    ProviderSpec(
        name="openrouter",
        env_key="OPENROUTER_API_KEY",
        default_api_base="https://openrouter.ai/api/v1",
        is_gateway=True,
    ),
    ProviderSpec(
        name="deepseek",
        env_key="DEEPSEEK_API_KEY",
        default_api_base="https://api.deepseek.com",
    ),
)


def get_provider_spec(provider_name: str) -> ProviderSpec | None:
    for spec in PROVIDERS:
        if spec.name == provider_name.lower():
            return spec
    return None
