# intake — 原始输入分拣与路由

## 行业背景

8D 调查的质量取决于前 48 小时的信息捕获质量。ASQ 和 AIAG 的 8D 指南均强调：在问题录入阶段，信息缺失比信息错误更危险 —— 因为缺失项会无声地窄化后续根因搜索范围。IATF 16949 第 10.2.3 条也明确要求组织记录客户投诉的完整初始信息，包括产品标识、失效现象和发现场景。一个弱的 intake 直接导致 D2 问题定义错误、D4 根因跑偏，最终整个 8D 变成"解决了一个不存在的问题"。本问点在流程中承担信息入口角色，路由到 D0（应急判断）、D1（团队组建）、D2（问题定义）的对应问点。

## S1 | 发散探索 — 多角度触发器

Agent 从以下问题中选 2-3 个向用户提问。每个问题要引出具体事实，不可用 yes/no 收场。

1. **产品识别**："把你能拿到的产品标签、料号、工单号、序列号都说一遍。哪怕不完整也比没有强。哪些信息你确定，哪些是你猜的？"
2. **现象还原**："你或客户第一次看到这个异常时，是在什么场景下？当时在做什么操作？产品表现出了什么和正常状态不一样的地方？用看得到、听得到、摸得到的方式描述。"
3. **发现链路**："这个消息是怎么到你这里的？邮件？电话？产线巡检？客户系统自动告警？中间传了几手？每一手可能丢失了什么信息？"
4. **严重度信号**："有没有安全相关的信号？有没有客户说了'停线''召回''索赔'这些词？有没有监管或认证机构介入的迹象？"
5. **人员拼图**："现在知道这件事的人里，谁离产品最近（操作员、检验员、现场服务工程师）？谁对客户最了解？谁有技术判断力？这三个人可能是三个不同的人。"

## S2 | 第一性原理收敛

追问链 —— 从表面答案逐层深入：

**Layer 1 — 表面陈述层**
- "你说的'产品坏了'，具体是什么功能失效了？用动词描述：不转、不亮、漏油、报错代码多少？"
- "你提到'客户投诉'，客户的邮件或电话记录原文是什么？不要总结，给我原文。"

**Layer 2 — 信息溯源层**
- "你说的这个批次号，是从哪里查到的？系统记录还是手写标签？有没有可能标错？"
- "发现时间'大概是上周'—— 能不能从邮件、交接记录、生产日志里找到精确时间？差一天可能就差一个班次。"
- "你说'影响范围不大'—— 这个判断基于什么？是查了所有库存还是凭感觉？"

**Layer 3 — 元信息层**
- "你给我的这些信息里，哪些是你亲眼看到的，哪些是别人告诉你的，哪些是你根据经验推断的？"
- "如果现在要你给每个信息标一个可信度（0-100%），哪些低于 70%？"

## S3 | 反事实挑战

1. "假设你刚才说的产品型号是错的 —— 实际上是一个相似但不同的产品 —— 什么证据能在 5 分钟内证明或推翻这个假设？"
2. "如果'客户投诉'实际上不是投诉，而是一个正常的产品咨询被误读成投诉，整个信息链条里哪个环节最可能发生这种误读？"

## S4 | 答案评分

评分维度：**完整性**、**可追溯性**、**事实/推断分离**

| 等级 | 标准 |
|------|------|
| Insufficient | 缺少产品标识或现象描述；无法区分信息来源；大量"大概""可能""应该" |
| Basic | 产品标识明确；现象有可观察描述；信息源可追溯（谁说的/什么记录）；缺失项标记为"待补充"且说明了向谁获取 |
| Excellent | 上述全部满足，且每条信息标注了可信度；事实和推断已分离；原始记录（邮件/日志/照片）已引用 |

## S5 | 输出格式

```json
{
  "extracted": {
    "product": {
      "model": "string | null",
      "part_number": "string | null",
      "serial_numbers": ["string"],
      "batch_lot": "string | null",
      "confidence": 0.0
    },
    "symptom": {
      "observable_phenomenon": "string | null",
      "failure_mode": "string | null",
      "normal_vs_abnormal": "string | null",
      "confidence": 0.0
    },
    "discovery": {
      "discoverer_name": "string | null",
      "discoverer_role": "string | null",
      "scenario": "string | null",
      "channel": "string | null",
      "timestamp": "string | null",
      "information_path": "string | null",
      "confidence": 0.0
    },
    "severity_indicators": {
      "safety_flag": false,
      "function_failure": false,
      "regulatory_flag": false,
      "volume_estimate": "string | null",
      "customer_escalation_words": ["string"],
      "confidence": 0.0
    },
    "personnel_map": {
      "closest_to_product": "string | null",
      "closest_to_customer": "string | null",
      "technical_authority": "string | null"
    }
  },
  "facts_vs_inferences": {
    "confirmed_facts": ["string"],
    "inferences_needing_verification": ["string"],
    "information_gaps": ["string"]
  },
  "routing": {
    "triggered_d0_questions": ["d0-q1", "d0-q2", "d0-q3", "d0-q4"],
    "triggered_d1_questions": ["d1-q1", "d1-q2", "d1-q3", "d1-q4", "d1-q5"],
    "triggered_d2_questions": ["d2-q1", "d2-q2", "d2-q3", "d2-q4", "d2-q5", "d2-q6"],
    "priority_domains": ["safety", "function", "regulatory", "volume"]
  },
  "confidence": 0.0,
  "next_action": "string"
}
```

## 纠偏原则 / 禁止项

| 禁止 | 替代方向 |
|------|---------|
| 把"可能是焊接问题"直接当成现象录入 | 追问"你看到的具体现象是什么？"现象是观察，根因是推断 |
| 在 intake 阶段追问"为什么会这样" | Intake 只做信息分拣，根因追问留给 D4 |
| 接受"信息不全，但大概就这样" | 缺失项必须标记，说明缺什么、计划向谁获取 |
| 把二手中转信息当一手信息 | 每条信息必须标注来源：直接观察 / 他人告知（指明谁）/ 文档记录（指明哪个文档） |
| 用部门名代替具体人名 | 每条人员信息必须是具体姓名或明确岗位 |
| 编造缺失信息来填满字段 | 不确定的信息宁可标 `null` + 说明缺什么 |
