"""Hard gate rules for pseudo-progress blocking."""

from __future__ import annotations

from dataclasses import dataclass

from fireline.skill.models import SkillCaseState


@dataclass
class GateResult:
    passed: bool
    blockers: list[str]


class GateValidator:
    """Pure-logic gate checks. Does not call LLM."""

    def check_d1(self, case: SkillCaseState) -> GateResult:
        blockers = []
        ans = case.answers
        required = {
            "d1-q1": "Owner",
            "d1-q2": "客户接口",
            "d1-q3": "技术角色",
        }
        for qid, name in required.items():
            if qid not in ans or ans[qid].status != "complete" or not ans[qid].value:
                blockers.append(f"D1 缺少 {name} ({qid})")
        return GateResult(passed=len(blockers) == 0, blockers=blockers)

    def check_d2(self, case: SkillCaseState) -> GateResult:
        blockers = []
        ans = case.answers
        required = ["d2-q1", "d2-q4", "d2-q5"]
        for qid in required:
            if qid not in ans or ans[qid].status != "complete" or not ans[qid].value:
                blockers.append(f"D2 问题定义不完整: {qid}")
        if "d2-q6" in ans and ans["d2-q6"].status == "complete":
            val = ans["d2-q6"].value or {}
            facts = val.get("facts", []) if isinstance(val, dict) else []
            inferences = val.get("inferences", []) if isinstance(val, dict) else []
            if not facts and inferences:
                blockers.append("D2 只有推断没有事实")
        return GateResult(passed=len(blockers) == 0, blockers=blockers)

    def check_d3(self, case: SkillCaseState) -> GateResult:
        blockers = []
        ans = case.answers
        windows = ["d3-q1", "d3-q2", "d3-q3", "d3-q4", "d3-q5"]
        filled = [qid for qid in windows if qid in ans and ans[qid].status == "complete"]
        if len(filled) < 2:
            blockers.append("D3 风险窗口识别不足（至少需识别客户现场/在途/库存/WIP/上游中的 2 项）")
        return GateResult(passed=len(blockers) == 0, blockers=blockers)

    def check_d4(self, case: SkillCaseState) -> GateResult:
        blockers = []
        ans = case.answers
        if "d4-q2" not in ans or ans["d4-q2"].status != "complete":
            blockers.append("D4 缺少候选原因")
        if "d4-q3" not in ans or ans["d4-q3"].status != "complete":
            blockers.append("D4 缺少发生原因（5-Why）")
        if "d4-q4" not in ans or ans["d4-q4"].status != "complete":
            blockers.append("D4 缺少流出原因（Escape Point）")
        if "d4-q6" not in ans or ans["d4-q6"].status != "complete":
            blockers.append("D4 缺少控制点判断")
        return GateResult(passed=len(blockers) == 0, blockers=blockers)

    def check_d6(self, case: SkillCaseState) -> GateResult:
        blockers = []
        ans = case.answers
        if "d6-q4" not in ans or ans["d6-q4"].status != "complete":
            blockers.append("D6 缺少验证结果，不能 final")
        return GateResult(passed=len(blockers) == 0, blockers=blockers)

    def check(self, case: SkillCaseState, target_stage: str) -> GateResult:
        """Run the gate check appropriate for the target stage."""
        if target_stage in ("d2", "d3", "d4"):
            return self.check_d1(case)
        if target_stage == "d5":
            return self.check_d4(case)
        if target_stage == "closed":
            d6 = self.check_d6(case)
            d4 = self.check_d4(case)
            return GateResult(
                passed=d6.passed and d4.passed,
                blockers=d6.blockers + d4.blockers,
            )
        return GateResult(passed=True, blockers=[])
