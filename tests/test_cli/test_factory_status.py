"""Smoke tests for CLI factory status and init commands."""

from typer.testing import CliRunner

from fireline.cli.main import app

runner = CliRunner()


def test_factory_status_help():
    result = runner.invoke(app, ["factory", "status", "--help"])
    assert result.exit_code == 0


def test_factory_status_with_data(tmp_path):
    """Factory status on a factory that has cases shows counts."""
    env = {"FIRELINE_DATA_DIR": str(tmp_path)}
    # Create a case first so the factory has data
    new_result = runner.invoke(
        app,
        ["new", "客户反馈USB无输出", "--mock", "--factory", "factory_status_data"],
        env=env,
    )
    assert new_result.exit_code == 0

    result = runner.invoke(
        app, ["factory", "status", "factory_status_data"], env=env
    )
    assert result.exit_code == 0
    assert "factory_status_data" in result.output
    assert "案件" in result.output


def test_factory_status_empty_factory(tmp_path):
    """Factory status on empty/nonexistent factory handles gracefully."""
    env = {"FIRELINE_DATA_DIR": str(tmp_path)}
    result = runner.invoke(
        app, ["factory", "status", "factory_status_empty"], env=env
    )
    assert result.exit_code == 0


def test_factory_init_creates_factory(tmp_path):
    """Factory init creates a new factory."""
    env = {"FIRELINE_DATA_DIR": str(tmp_path)}
    result = runner.invoke(
        app, ["factory", "init", "brand_new_factory"], env=env
    )
    assert result.exit_code == 0
    assert "brand_new_factory" in result.output


def test_factory_init_with_name(tmp_path):
    """Factory init with --name flag."""
    env = {"FIRELINE_DATA_DIR": str(tmp_path)}
    result = runner.invoke(
        app,
        ["factory", "init", "factory_named", "--name", "Named 工厂"],
        env=env,
    )
    assert result.exit_code == 0
    assert "factory_named" in result.output
    assert "Named" in result.output
