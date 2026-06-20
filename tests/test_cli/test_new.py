"""Smoke tests for CLI new command."""

from typer.testing import CliRunner

from fireline.cli.main import app

runner = CliRunner()


def test_new_help():
    result = runner.invoke(app, ["new", "--help"])
    assert result.exit_code == 0
    assert "原始输入" in result.output


def test_new_with_mock():
    result = runner.invoke(
        app, ["new", "客户反馈USB无输出", "--mock", "--factory", "factory_cli_test"]
    )
    assert result.exit_code == 0
    assert "案件已创建" in result.output


def test_show_missing_case():
    result = runner.invoke(app, ["show", "CASE-NOT-EXIST", "--factory", "factory_cli_test"])
    assert result.exit_code != 0
    assert "案件不存在" in result.output
