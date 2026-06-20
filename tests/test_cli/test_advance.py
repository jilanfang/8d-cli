"""Smoke tests for CLI advance command and gate blocking."""

from typer.testing import CliRunner

from fireline.cli.main import app

runner = CliRunner()


def test_advance_help():
    result = runner.invoke(app, ["advance", "--help"])
    assert result.exit_code == 0
    assert "目标状态" in result.output


def test_advance_blocked_without_d1_to_d4(tmp_path):
    env = {"FIRELINE_DATA_DIR": str(tmp_path)}
    new_result = runner.invoke(
        app,
        ["new", "客户反馈USB无输出", "--mock", "--factory", "factory_advance_test"],
        env=env,
    )
    assert new_result.exit_code == 0
    case_id = new_result.output.split("案件已创建:")[1].split()[0].strip()

    result = runner.invoke(
        app,
        ["advance", case_id, "--target", "d5_d8", "--mock", "--factory", "factory_advance_test"],
        env=env,
    )
    assert result.exit_code == 0
    assert "推进被阻断" in result.output
    assert any(marker in result.output for marker in ["D1", "D2", "D3", "D4"])


def test_advance_to_d5_d8_after_filling_required_questions(tmp_path):
    env = {"FIRELINE_DATA_DIR": str(tmp_path)}
    new_result = runner.invoke(
        app,
        ["new", "客户反馈USB无输出", "--mock", "--factory", "factory_advance_test"],
        env=env,
    )
    assert new_result.exit_code == 0
    case_id = new_result.output.split("案件已创建:")[1].split()[0].strip()

    answers = [
        ("d1-q1", '{"owner": "李四"}'),
        ("d1-q2", '{"customer_contact": "王五"}'),
        ("d1-q3", '{"technical_lead": "张三"}'),
        ("d2-q1", '{"customer_view": "客户反馈USB无输出"}'),
        ("d2-q4", '{"object_boundary": "USB模块A1"}'),
        ("d2-q5", '{"impact_qty": 100}'),
        ("d3-q1", '{"customer_field_risk": true}'),
        ("d3-q2", '{"in_transit_risk": false}'),
        ("d4-q2", '{"candidate_causes": []}'),
        ("d4-q3", '{"root_cause": "焊点开裂"}'),
        ("d4-q4", '{"primary_escape_point": "ATE"}'),
        ("d4-q6", '{"control_point": "回流炉"}'),
    ]
    for qid, value in answers:
        r = runner.invoke(
            app,
            ["question", case_id, qid, "--answer", value, "--factory", "factory_advance_test"],
            env=env,
        )
        assert r.exit_code == 0, f"Failed to answer {qid}: {r.output}"

    result = runner.invoke(
        app,
        ["advance", case_id, "--target", "d5_d8", "--mock", "--factory", "factory_advance_test"],
        env=env,
    )
    assert result.exit_code == 0
    assert "案件已推进到: d5_d8" in result.output


def test_advance_to_closed_blocked_without_d6(tmp_path):
    env = {"FIRELINE_DATA_DIR": str(tmp_path)}
    new_result = runner.invoke(
        app,
        ["new", "客户反馈USB无输出", "--mock", "--factory", "factory_closed_test"],
        env=env,
    )
    assert new_result.exit_code == 0
    case_id = new_result.output.split("案件已创建:")[1].split()[0].strip()

    result = runner.invoke(
        app,
        ["advance", case_id, "--target", "closed", "--mock", "--factory", "factory_closed_test"],
        env=env,
    )
    assert result.exit_code == 0
    assert "推进被阻断" in result.output
    assert "D6" in result.output
