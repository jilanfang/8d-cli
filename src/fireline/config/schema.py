"""Application configuration."""

import json
from pathlib import Path

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class LLMConfig(BaseModel):
    provider: str = "openrouter"
    model: str = "deepseek/deepseek-chat"
    api_key: str = ""
    api_base: str | None = None
    temperature: float = 0.1
    max_tokens: int = 4096


CONFIG_DIR = Path.home() / ".fireline"
CONFIG_PATH = CONFIG_DIR / "config.json"


def load_user_config() -> dict:
    """Load user-level JSON config, ignoring unknown keys."""
    if not CONFIG_PATH.exists():
        return {}
    try:
        return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def save_user_config(config: dict) -> None:
    """Persist user-level JSON config."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.write_text(json.dumps(config, indent=2, ensure_ascii=False), encoding="utf-8")


class SkillConfig(BaseModel):
    """Skill source configuration.

    When ``skill_path`` is set, the CLI mounts 8d-guru markdown prompts
    directly instead of using the embedded Jinja2 templates.
    """

    skill_path: str | None = None
    """Path to an 8d-guru installation. When set, bypasses Jinja2 templates."""
    profiles: list[str] = Field(default_factory=list)
    """Industry profiles to activate, e.g. ``["iatf16949"]``."""


class FirelineConfig(BaseSettings):
    default_factory: str = "factory_default"
    data_dir: Path = Path.home() / ".fireline" / "data"
    llm: LLMConfig = Field(default_factory=LLMConfig)
    skill: SkillConfig = Field(default_factory=SkillConfig)

    model_config = SettingsConfigDict(
        env_prefix="FIRELINE_",
        env_nested_delimiter="__",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )
