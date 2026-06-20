"""CLI shared context helpers."""

import os
import shutil
from pathlib import Path

from fireline.adapters.storage.json_store import JsonStore
from fireline.config.schema import (
    FirelineConfig,
    load_user_config,
)


def get_default_factory(factory_id: str | None) -> str:
    """Resolve factory ID with precedence: arg > env > config file > default."""
    if factory_id:
        return factory_id
    env_value = os.environ.get("FIRELINE_DEFAULT_FACTORY")
    if env_value:
        return env_value
    user_cfg = load_user_config()
    if user_cfg.get("default_factory"):
        return user_cfg["default_factory"]
    return FirelineConfig().default_factory


def get_preset_data_dir(factory_id: str) -> Path | None:
    """Return preset factory data directory inside the project, if it exists.

    Uses the project root (``src/fireline/cli/context.py`` -> ``parents[3]`` = project root).
    """
    path = Path(__file__).parents[3] / "data" / "factories" / factory_id
    return path if path.exists() else None


# Legacy alias — used by older code
_preset_dir = get_preset_data_dir


def get_store(factory_id: str | None) -> JsonStore:
    """Get a JsonStore for the resolved factory, seeding from preset if needed."""
    factory_id = get_default_factory(factory_id)
    cfg = FirelineConfig()
    store = JsonStore(factory_id, base_dir=cfg.data_dir)
    if not store.factory_dir.exists():
        preset = _preset_dir(factory_id)
        if preset:
            shutil.copytree(preset, store.factory_dir)
    return store
