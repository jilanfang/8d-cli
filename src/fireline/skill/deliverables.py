"""Build human-readable draft deliverables from case state.

Supports both 8d-guru and legacy field naming conventions.
"""

from __future__ import annotations

from typing import Any

from fireline.skill.models import SkillCaseState


def _guru_or_legacy(
    data: dict[str, Any], guru_key: str, legacy_key: str, default: Any = None
) -> Any:
    """Try 8d-guru field name first, fall back to legacy name."""
    val = data.get(guru_key)
    if val is not None:
        return val
    return data.get(legacy_key, default)


def _step_question(step: dict[str, Any]) -> str:
    """8d-guru uses ``question``, legacy uses ``why``."""
    return str(step.get("question") or step.get("why", ""))


def _step_layer(step: dict[str, Any]) -> int | str:
    """8d-guru uses ``layer``, legacy uses ``level``."""
    return step.get("layer") or step.get("level", "?")


def _step_location(step: dict[str, Any]) -> str:
    """8d-guru uses ``detection_point``, legacy uses ``location``."""
    return str(step.get("detection_point") or step.get("location", ""))


def _extract_fact_string(item: Any) -> str:
    """8d-guru d2-q6 returns objects with ``statement``; legacy returns plain strings."""
    if isinstance(item, dict):
        return item.get("statement", str(item))
    return str(item)


class DeliverableBuilder:
    """Builds role-based deliverable drafts. Stateless."""

    def build_for_question(
        self, question_id: str, stage_output: dict[str, Any], case: SkillCaseState
    ) -> str:
        builders = {
            "d0-q3": self._build_d0q3,
            "d2-q6": self._build_d2q6,
            "d4-q2": self._build_d4q2,
            "d4-q3": self._build_d4q3,
            "d4-q4": self._build_d4q4,
            "d4-q6": self._build_d4q6,
        }
        builder = builders.get(question_id, self._build_generic)
        return builder(stage_output, case)

    def _build_generic(self, stage_output: dict[str, Any], case: SkillCaseState) -> str:
        lines = ["## 岗位交付物草案", ""]
        for key, value in stage_output.items():
            lines.append(f"- **{key}**: {value}")
        return "\n".join(lines)

    def _build_d0q3(self, stage_output: dict[str, Any], case: SkillCaseState) -> str:
        # 8d-guru nests under launch_decision; legacy is flat
        launch = stage_output.get("launch_decision", {})
        need = _guru_or_legacy(
            launch, "need_full_8d", "need_full_8d"
        ) or stage_output.get("need_full_8d", "未明确")
        reason = stage_output.get("reason", "")
        priority = stage_output.get("priority", "")
        return (
            "## D0-Q3 严重度评估草案\n\n"
            f"- 是否进入完整 8D: {need}\n"
            f"- 优先级: {priority}\n"
            f"- 判断理由: {reason}\n"
        )

    def _build_d2q6(self, stage_output: dict[str, Any], case: SkillCaseState) -> str:
        facts = stage_output.get("facts", [])
        inferences = stage_output.get("inferences", [])
        assumptions = stage_output.get("unverified_assumptions", [])
        hidden = stage_output.get("hidden_inferences", [])
        lines = ["## D2-Q6 事实与推断区分草案", ""]
        lines.append("**确认事实：**")
        for f in facts:
            lines.append(f"- {_extract_fact_string(f)}")
        lines.append("\n**当前推断（需验证）：**")
        for i in inferences:
            lines.append(f"- {_extract_fact_string(i)}")
        if assumptions:
            lines.append("\n**未被证实的假设：**")
            for a in assumptions:
                lines.append(f"- {_extract_fact_string(a)}")
        if hidden:
            lines.append("\n**隐藏推断（需特别警惕）：**")
            for h in hidden:
                lines.append(f"- ⚠️ {h}")
        return "\n".join(lines)

    def _build_d4q2(self, stage_output: dict[str, Any], case: SkillCaseState) -> str:
        causes = stage_output.get("candidate_causes", [])
        lines = ["## D4-Q2 候选原因草案", ""]
        for c in causes:
            cause_name = c.get("cause", "")
            category = c.get("category", "")
            confidence = c.get("confidence", "?")
            lines.append(f"- **{cause_name}**（{category}）置信度 {confidence}")
            evidence_for = c.get("evidence_for", [])
            if evidence_for:
                lines.append(f"  - 支持证据：{', '.join(str(e) for e in evidence_for)}")
            physical_chain = c.get("physical_chain", "")
            if physical_chain:
                lines.append(f"  - 物理链：{physical_chain}")
        return "\n".join(lines)

    def _build_d4q3(self, stage_output: dict[str, Any], case: SkillCaseState) -> str:
        chain = stage_output.get("why_chain", [])
        root = _guru_or_legacy(stage_output, "occurrence_root_cause", "root_cause", "")
        cp = stage_output.get("control_point_lost", "")
        critical = stage_output.get("critical_condition", "")
        lines = ["## D4-Q3 发生原因（5-Why）草案", ""]
        for step in chain:
            layer = _step_layer(step)
            question = _step_question(step)
            answer = step.get("answer", "")
            answer_type = step.get("answer_type", "")
            type_str = f" [{answer_type}]" if answer_type else ""
            lines.append(f"- Why {layer}: {question} → {answer}{type_str}")
        lines.append(f"\n**根因:** {root}")
        lines.append(f"**失守控制点:** {cp}")
        if critical:
            lines.append(f"**关键条件:** {critical}")
        return "\n".join(lines)

    def _build_d4q4(self, stage_output: dict[str, Any], case: SkillCaseState) -> str:
        chain = stage_output.get("escape_chain", [])
        primary = stage_output.get("primary_escape_point", "")
        earliest = stage_output.get("earliest_possible_detection", "")
        blind_spot = stage_output.get("detection_blind_spot", "")
        lines = ["## D4-Q4 流出原因（Escape Point）草案", ""]
        for step in chain:
            location = _step_location(step)
            why_escaped = step.get("why_escaped", "")
            escape_point = step.get("escape_point", "")
            lines.append(f"- **{location}**: {why_escaped} → {escape_point}")
        lines.append(f"\n**主要 Escape Point:** {primary}")
        if earliest:
            lines.append(f"**最早可检测点:** {earliest}")
        if blind_spot:
            lines.append(f"**检测盲区:** {blind_spot}")
        return "\n".join(lines)

    def _build_d4q6(self, stage_output: dict[str, Any], case: SkillCaseState) -> str:
        cp = stage_output.get("control_point", stage_output)
        mrc = stage_output.get("mrc", {})
        lines = ["## D4-Q6 控制点判断草案", "", str(cp)]
        if mrc:
            lines.append(f"\n**管理根因 (MRC):** {mrc}")
        return "\n".join(lines)

    def build_full_report(self, case: SkillCaseState, report_format: str = "8d") -> str:
        lines = [f"# {report_format.upper()} 报告草案", f"案件: {case.case_id}", ""]
        for stage in ["d0", "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8"]:
            lines.append(f"## {stage.upper()}")
            stage_answers = {qid: a for qid, a in case.answers.items() if qid.startswith(stage)}
            if not stage_answers:
                lines.append("（未填写）")
            for qid, ans in stage_answers.items():
                lines.append(f"- {qid}: {ans.value}")
            lines.append("")
        return "\n".join(lines)
