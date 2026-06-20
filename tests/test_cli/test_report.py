"""Smoke tests for CLI report command — report generation and formats."""

from typer.testing import CliRunner

from fireline.cli.main import app

runner = CliRunner()


def test_report_help():
    result = runner.invoke(app, ["report", "--help"])
    assert result.exit_code == 0
    assert "报告" in result.output


def test_report_empty_case(tmp_path):
    """Report for empty case generates structured output with a report ID."""
    env = {"FIRELINE_DATA_DIR": str(tmp_path)}
    new_result = runner.invoke(
        app,
        ["new", "客户反馈USB无输出", "--mock", "--factory", "factory_report_empty"],
        env=env,
    )
    assert new_result.exit_code == 0
    case_id = new_result.output.split("案件已创建:")[1].split()[0].strip()

    result = runner.invoke(
        app, ["report", case_id, "--factory", "factory_report_empty"], env=env
    )
    assert result.exit_code == 0
    assert "RPT-" in result.output


def test_report_with_answers(tmp_path):
    """Report with answers includes filled content."""
    env = {"FIRELINE_DATA_DIR": str(tmp_path)}
    new_result = runner.invoke(
        app,
        ["new", "客户反馈USB无输出", "--mock", "--factory", "factory_report_answers"],
        env=env,
    )
    assert new_result.exit_code == 0
    case_id = new_result.output.split("案件已创建:")[1].split()[0].strip()

    # Fill in D1 answers before generating report
    for qid, answer in [
        ("d1-q1", '{"name": "张三", "role": "质量工程师"}'),
        ("d1-q2", '{"name": "李四", "role": "客户对接"}'),
        ("d1-q3", '{"name": "王五", "role": "技术负责人"}'),
    ]:
        r = runner.invoke(
            app,
            ["question", case_id, qid, "--answer", answer, "--factory", "factory_report_answers"],
            env=env,
        )
        assert r.exit_code == 0, f"Failed to answer {qid}: {r.output}"

    result = runner.invoke(
        app, ["report", case_id, "--factory", "factory_report_answers"], env=env
    )
    assert result.exit_code == 0
    assert "RPT-" in result.output


def test_report_rca_format(tmp_path):
    """RCA format works and produces a report ID."""
    env = {"FIRELINE_DATA_DIR": str(tmp_path)}
    new_result = runner.invoke(
        app,
        ["new", "客户反馈USB无输出", "--mock", "--factory", "factory_report_rca"],
        env=env,
    )
    assert new_result.exit_code == 0
    case_id = new_result.output.split("案件已创建:")[1].split()[0].strip()

    result = runner.invoke(
        app, ["report", case_id, "--format", "rca", "--factory", "factory_report_rca"], env=env
    )
    assert result.exit_code == 0
    assert "RPT-" in result.output


def test_report_missing_case(tmp_path):
    """Report for non-existent case shows error and exits 1."""
    env = {"FIRELINE_DATA_DIR": str(tmp_path)}
    result = runner.invoke(
        app, ["report", "CASE-NONEXISTENT", "--factory", "factory_report_missing"], env=env
    )
    assert result.exit_code == 1
    assert "不存在" in result.output
