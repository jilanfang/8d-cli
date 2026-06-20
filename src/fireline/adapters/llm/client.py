"""OpenAI-compatible LLM client."""

from typing import Any

from openai import AsyncOpenAI

from fireline.adapters.llm.provider import LLMClient, get_provider_spec
from fireline.config.schema import LLMConfig


class LLMClientError(Exception):
    """Raised when the LLM client fails to produce a usable response."""


class OpenAICompatibleClient(LLMClient):
    """Async OpenAI-compatible client with JSON-mode parsing."""

    def __init__(self, config: LLMConfig):
        self.config = config
        spec = get_provider_spec(config.provider)
        api_base = config.api_base or (
            spec.default_api_base if spec else "https://api.openai.com/v1"
        )
        api_key = config.api_key or "no-key"
        self.client = AsyncOpenAI(base_url=api_base, api_key=api_key)

    async def complete(
        self,
        prompt: str,
        json_mode: bool = True,
        temperature: float | None = None,
    ) -> dict[str, Any]:
        import json

        kwargs: dict[str, Any] = {
            "model": self.config.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature if temperature is not None else self.config.temperature,
            "max_tokens": self.config.max_tokens,
        }
        if json_mode:
            kwargs["response_format"] = {"type": "json_object"}

        last_error: Exception | None = None
        for attempt in range(2):
            try:
                response = await self.client.chat.completions.create(**kwargs)
                content = response.choices[0].message.content or "{}"
                return json.loads(content)
            except json.JSONDecodeError as exc:
                last_error = exc
                if attempt == 0:
                    kwargs["messages"].append(
                        {"role": "assistant", "content": response.choices[0].message.content or ""}
                    )
                    kwargs["messages"].append(
                        {
                            "role": "user",
                            "content": (
                                "Your previous response was not valid JSON. "
                                "Please return a valid JSON object."
                            ),
                        }
                    )
            except Exception as exc:
                last_error = exc
                if attempt == 0:
                    continue

        raise LLMClientError(
            f"Failed to get valid JSON response after retries: {last_error}"
        ) from last_error


class MockLLMClient(LLMClient):
    """Deterministic mock client for tests and demos without API keys."""

    def __init__(self, response: dict[str, Any] | None = None):
        self.response = response or {"answer": "mock answer", "confidence": 0.8}

    async def complete(
        self,
        prompt: str,
        json_mode: bool = True,
        temperature: float | None = None,
    ) -> dict[str, Any]:
        return dict(self.response)


def make_llm_client(config: LLMConfig | None = None, mock: bool = False) -> LLMClient:
    from fireline.config.schema import FirelineConfig

    cfg = config or FirelineConfig().llm
    if mock or not cfg.api_key:
        return MockLLMClient()
    return OpenAICompatibleClient(cfg)
