"""Question-point catalog for D0-D8."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel


class Question(BaseModel):
    id: str
    stage: str
    name: str
    purpose: str
    core_question: str
    trigger_condition: str = ""
    output_schema: dict | None = None


class QuestionCatalog:
    """Registry of all D0-D8 question points."""

    QUESTIONS: dict[str, Question] = {
        # D0
        "d0-q1": Question(
            id="d0-q1",
            stage="d0",
            name="表征现象",
            purpose="理解实际看到的是什么",
            core_question="到底看到了什么？",
            output_schema={
                "phenomenon": "str",
                "clarification_needed": ["str"],
                "confidence": "float",
            },
        ),
        "d0-q2": Question(
            id="d0-q2",
            stage="d0",
            name="发现信息",
            purpose="记录时间地点人物",
            core_question="什么时候、哪里、谁发现的？",
            output_schema={"when": "str", "where": "str", "who": "str", "how_found": "str"},
        ),
        "d0-q3": Question(
            id="d0-q3",
            stage="d0",
            name="严重度评估",
            purpose="判断是否值得投入完整 8D",
            core_question="这个问题有多大？需要完整 8D 吗？",
            output_schema={
                "need_full_8d": "bool",
                "reason": "str",
                "priority": "str",
                "alternatives": ["str"],
            },
        ),
        "d0-q4": Question(
            id="d0-q4",
            stage="d0",
            name="紧急动作",
            purpose="搞清楚前要做什么",
            core_question="在搞清楚之前，有什么紧急要做的？",
            output_schema={
                "emergency_actions": [{"action": "str", "owner": "str", "deadline": "str"}]
            },
        ),
        # D1
        "d1-q1": Question(
            id="d1-q1",
            stage="d1",
            name="Owner",
            purpose="指定负责人",
            core_question="谁负责推动这个案子？",
        ),
        "d1-q2": Question(
            id="d1-q2",
            stage="d1",
            name="客户接口",
            purpose="指定客户窗口",
            core_question="谁和客户对接？",
        ),
        "d1-q3": Question(
            id="d1-q3",
            stage="d1",
            name="技术角色",
            purpose="指定技术判断人",
            core_question="谁来做技术决策？",
        ),
        "d1-q4": Question(
            id="d1-q4",
            stage="d1",
            name="现场执行",
            purpose="指定现场执行人",
            core_question="谁去现场获取信息？",
        ),
        "d1-q5": Question(
            id="d1-q5",
            stage="d1",
            name="证据管理",
            purpose="指定证据负责人",
            core_question="谁负责收集证据？",
        ),
        # D2
        "d2-q1": Question(
            id="d2-q1",
            stage="d2",
            name="客户视角",
            purpose="明确客户看到的现象",
            core_question="客户到底看到了什么？",
        ),
        "d2-q2": Question(
            id="d2-q2",
            stage="d2",
            name="厂内视角",
            purpose="确认内部是否复现",
            core_question="厂内有复现吗？",
        ),
        "d2-q3": Question(
            id="d2-q3",
            stage="d2",
            name="时间边界",
            purpose="锁定时间范围",
            core_question="什么时候开始的？持续多久？",
        ),
        "d2-q4": Question(
            id="d2-q4",
            stage="d2",
            name="对象边界",
            purpose="锁定对象范围",
            core_question="哪个 SKU/批次/订单？",
        ),
        "d2-q5": Question(
            id="d2-q5",
            stage="d2",
            name="影响量化",
            purpose="量化影响",
            core_question="影响多少？失效率多少？",
        ),
        "d2-q6": Question(
            id="d2-q6",
            stage="d2",
            name="事实vs推断",
            purpose="区分事实与猜测",
            core_question="哪些是看到的，哪些是推测的？",
            output_schema={
                "facts": ["str"],
                "inferences": ["str"],
                "unverified_assumptions": ["str"],
            },
        ),
        # D3
        "d3-q1": Question(
            id="d3-q1",
            stage="d3",
            name="客户现场",
            purpose="处理客户现场",
            core_question="客户那边有多少？怎么处理？",
        ),
        "d3-q2": Question(
            id="d3-q2",
            stage="d3",
            name="在途货物",
            purpose="处理在途货物",
            core_question="发出去的路上有多少？",
        ),
        "d3-q3": Question(
            id="d3-q3",
            stage="d3",
            name="成品库存",
            purpose="处理成品库存",
            core_question="厂内成品仓有多少？",
        ),
        "d3-q4": Question(
            id="d3-q4", stage="d3", name="WIP", purpose="处理在制品", core_question="产线上有多少？"
        ),
        "d3-q5": Question(
            id="d3-q5",
            stage="d3",
            name="上游来源",
            purpose="处理供应商侧",
            core_question="供应商/物料源头有没有问题？",
        ),
        # D4
        "d4-q1": Question(
            id="d4-q1",
            stage="d4",
            name="失效描述",
            purpose="具体描述失效",
            core_question="具体是什么失效了？",
        ),
        "d4-q2": Question(
            id="d4-q2",
            stage="d4",
            name="候选原因",
            purpose="列出候选原因及证据",
            core_question="可能的原因有哪些？证据是什么？",
            output_schema={
                "candidate_causes": [
                    {
                        "cause": "str",
                        "category": "str",
                        "evidence_for": ["str"],
                        "evidence_against": ["str"],
                        "confidence": "float",
                    }
                ]
            },
        ),
        "d4-q3": Question(
            id="d4-q3",
            stage="d4",
            name="发生原因",
            purpose="追到根本原因",
            core_question="为什么会发生？追到根因了吗？",
            output_schema={
                "why_chain": [{"level": "int", "why": "str", "answer": "str"}],
                "root_cause": "str",
                "control_point_lost": "str",
            },
        ),
        "d4-q4": Question(
            id="d4-q4",
            stage="d4",
            name="流出原因",
            purpose="识别 Escape Point",
            core_question="为什么流出时没拦住？",
            output_schema={
                "escape_chain": [{"location": "str", "why_escaped": "str", "escape_point": "str"}],
                "primary_escape_point": "str",
            },
        ),
        "d4-q5": Question(
            id="d4-q5",
            stage="d4",
            name="系统原因",
            purpose="追问系统为什么没防住",
            core_question="为什么系统没有防住？",
        ),
        "d4-q6": Question(
            id="d4-q6",
            stage="d4",
            name="控制点",
            purpose="定位失守控制点",
            core_question="哪个控制点失守了？",
        ),
        # D5
        "d5-q1": Question(
            id="d5-q1",
            stage="d5",
            name="对应根因",
            purpose="措施针对根因",
            core_question="措施针对哪个根因？",
        ),
        "d5-q2": Question(
            id="d5-q2",
            stage="d5",
            name="对应Escape Point",
            purpose="措施针对Escape Point",
            core_question="措施针对哪个Escape Point？",
        ),
        "d5-q3": Question(
            id="d5-q3",
            stage="d5",
            name="措施具体化",
            purpose="把措施写具体",
            core_question="具体做什么？不是加强管理",
        ),
        "d5-q4": Question(
            id="d5-q4",
            stage="d5",
            name="可行性",
            purpose="评估可行性",
            core_question="技术上可行吗？成本呢？",
        ),
        "d5-q5": Question(
            id="d5-q5",
            stage="d5",
            name="责任时间",
            purpose="明确责任人和时间",
            core_question="谁来做？什么时候完成？",
        ),
        # D6
        "d6-q1": Question(
            id="d6-q1",
            stage="d6",
            name="验证方法",
            purpose="确定验证方法",
            core_question="怎么验证措施有效？",
        ),
        "d6-q2": Question(
            id="d6-q2",
            stage="d6",
            name="验证范围",
            purpose="确定验证范围",
            core_question="验证多少样本？多长时间？",
        ),
        "d6-q3": Question(
            id="d6-q3",
            stage="d6",
            name="判定标准",
            purpose="确定通过标准",
            core_question="什么算通过？",
        ),
        "d6-q4": Question(
            id="d6-q4",
            stage="d6",
            name="验证结果",
            purpose="记录验证结果",
            core_question="实际结果是什么？",
        ),
        # D7
        "d7-q1": Question(
            id="d7-q1",
            stage="d7",
            name="同类检查",
            purpose="检查同类产品",
            core_question="同类产品/型号有没有问题？",
        ),
        "d7-q2": Question(
            id="d7-q2",
            stage="d7",
            name="供应商检查",
            purpose="检查同供应商",
            core_question="同供应商物料有没有问题？",
        ),
        "d7-q3": Question(
            id="d7-q3",
            stage="d7",
            name="系统更新",
            purpose="更新文件",
            core_question="PFMEA/Control Plan/SOP更新了吗？",
        ),
        "d7-q4": Question(
            id="d7-q4",
            stage="d7",
            name="横向展开",
            purpose="横向展开",
            core_question="还有什么需要检查的？",
        ),
        # D8
        "d8-q1": Question(
            id="d8-q1",
            stage="d8",
            name="结案条件",
            purpose="确认结案条件",
            core_question="所有条件都满足了吗？",
        ),
        "d8-q2": Question(
            id="d8-q2",
            stage="d8",
            name="经验积累",
            purpose="积累可复用经验",
            core_question="这次学到了什么？",
        ),
        "d8-q3": Question(
            id="d8-q3",
            stage="d8",
            name="团队认可",
            purpose="团队确认",
            core_question="团队都确认了吗？",
        ),
    }

    @classmethod
    def get(cls, question_id: str) -> Question:
        if question_id not in cls.QUESTIONS:
            raise KeyError(f"Unknown question_id: {question_id}")
        return cls.QUESTIONS[question_id]

    @classmethod
    def list_by_stage(cls, stage: str) -> list[Question]:
        return [q for q in cls.QUESTIONS.values() if q.stage == stage]

    @classmethod
    def next_incomplete(
        cls, case_answers: dict[str, Any], stage: str | None = None
    ) -> Question | None:
        questions = cls.QUESTIONS.values() if stage is None else cls.list_by_stage(stage)
        for q in questions:
            answer = case_answers.get(q.id)
            if answer is None or answer.get("status") != "complete":
                return q
        return None
