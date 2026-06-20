"""Smoke tests for config command."""

import json

from typer.testing import CliRunner

from fireline.cli.main import app

runner = CliRunner()


def test_config_factory_help():
    result = runner.invoke(app, ["config", "factory", "--help"])
    assert result.exit_code == 0
    assert "默认工厂" in result.output


def test_config_factory_persists(tmp_path, monkeypatch):
    config_dir = tmp_path / ".fireline"
    monkeypatch.setattr("fireline.config.schema.CONFIG_DIR", config_dir)
    monkeypatch.setattr("fireline.config.schema.CONFIG_PATH", config_dir / "config.json")

    result = runner.invoke(app, ["config", "factory", "factory_test"])
    assert result.exit_code == 0
    assert "factory_test" in result.output

    config = json.loads((config_dir / "config.json").read_text(encoding="utf-8"))
    assert config["default_factory"] == "factory_test"
