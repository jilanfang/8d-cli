"""Tests for CLI context helpers."""

from fireline.cli.context import get_default_factory, get_store
from fireline.config.schema import save_user_config


def test_get_default_factory_arg_wins(tmp_path, monkeypatch):
    assert get_default_factory("factory_arg") == "factory_arg"


def test_get_default_factory_env_wins(tmp_path, monkeypatch):
    monkeypatch.setenv("FIRELINE_DEFAULT_FACTORY", "factory_env")
    assert get_default_factory(None) == "factory_env"


def test_get_default_factory_config_file(tmp_path, monkeypatch):
    monkeypatch.delenv("FIRELINE_DEFAULT_FACTORY", raising=False)
    config_dir = tmp_path / ".fireline"
    monkeypatch.setattr("fireline.config.schema.CONFIG_DIR", config_dir)
    monkeypatch.setattr("fireline.config.schema.CONFIG_PATH", config_dir / "config.json")
    save_user_config({"default_factory": "factory_config"})
    assert get_default_factory(None) == "factory_config"


def test_get_store_seeds_preset(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    monkeypatch.setenv("FIRELINE_DATA_DIR", str(data_dir))
    store = get_store("factory_default")
    assert store.factory_dir.exists()
    assert (store.factory_dir / "experience" / "patterns.yaml").exists()
    assert len(store.list_cases()) >= 1
