"""Smoke tests for cases command."""

from typer.testing import CliRunner

from fireline.cli.main import app

runner = CliRunner()


def test_cases_help():
    result = runner.invoke(app, ["cases", "--help"])
    assert result.exit_code == 0
    assert "列出" in result.output


def test_cases_lists_new_case(tmp_path):
    env = {"FIRELINE_DATA_DIR": str(tmp_path)}
    new_result = runner.invoke(
        app,
        ["new", "客户反馈USB无输出", "--mock", "--factory", "factory_cases_test"],
        env=env,
    )
    assert new_result.exit_code == 0

    result = runner.invoke(app, ["cases", "--factory", "factory_cases_test"], env=env)
    assert result.exit_code == 0
    assert "案件列表" in result.output
    assert "d0_d4" in result.output


def test_cases_empty_factory(tmp_path):
    env = {"FIRELINE_DATA_DIR": str(tmp_path)}
    result = runner.invoke(
        app, ["cases", "--factory", "factory_cases_empty_test"], env=env
    )
    assert result.exit_code == 0
    assert "暂无案件" in result.output
