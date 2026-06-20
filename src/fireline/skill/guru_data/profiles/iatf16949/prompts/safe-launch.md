# safe-launch — Safe Launch / Early Production Containment

## 行业背景

Safe Launch（安全投产）是 APQP 第 3 版第 5 阶段（投产与反馈、评定与纠正措施）定义的增强控制期。它不是可选操作——当你具备以下条件时必须执行：新产品投产、工程变更实施、PPAP 批准后首批量产、生产地转移、或长期停产后恢复。标准周期为 90 天，每班次增强检验频次和项目覆盖，直至收集到足够统计证据证明过程稳定且有能力。

IATF 16949 虽然没有单独的"Safe Launch"条款，但 8.3.4.4（产品批准过程）、8.5.6.1（变更管理）、10.2.3（问题解决）和 10.3.1（持续改进）共同构成了 Safe Launch 的条款基础。Safe Launch CP（控制计划）不等于量产 CP——前者是临时增强版，检验频次、样本量、SPC 频次都更高，且必须标注为"Safe Launch 控制计划"以区别于量产控制计划。

Safe Launch 期间发生任何质量溢出（定义：任何超出 Safe Launch CP 规格的偏离，不论是否流出到客户），90 天时钟立即重置。这不是惩罚，是信号：过程尚未稳定到可以退出增强控制的水平。

## S1 | 发散探索 — 多角度触发器

Agent 从以下问题中选 3-4 个向用户提问。

1. **Safe Launch 触发条件确认**："这个产品当前处于什么阶段？是新项目 SOP 后头 90 天吗？还是刚做过工程变更恢复生产？还是 PPAP 重新批准后重新投产？还是换了生产地/产线？触发 Safe Launch 的具体事件是什么？哪一天开始的？"

2. **Safe Launch CP 审查**："你有没有一个单独的 Safe Launch 控制计划文件？还是把增强控制直接写在量产 CP 上？Safe Launch CP 和量产 CP 的区别在哪里——检验频次提高多少？增加了哪些临时控制项？SPC 频次从什么周期变成什么周期？"

3. **交接条件检查**："QC 检验员、产线班长、生产主管是否都知道当前在 Safe Launch 期？Safe Launch CP 是否已经在产线上可见？操作员能不能立即区分 Safe Launch CP 和正常 CP 的要求差异？"

4. **退出标准定义**："退出 Safe Launch 的条件是什么？是不是 90 个连续自然日零缺陷？还是 90 个连续生产日？'零缺陷'的定义范围是什么——仅客户投诉级缺陷，还是所有在 Safe Launch CP 范围内检测到的任何偏离都算？"

5. **扩展触发规则**："如果你在 Safe Launch 第 60 天发现一个 Safe Launch CP 检测项偏离（但没流到客户），你的 90 天时钟怎么办？有没有提前定义过哪些事件触发时钟重置？谁有权决定重置？"

## S2 | 第一性原理收敛

追问链 —— 从表面概念逐层深入操作层。

**Layer 1 — 文件与执行**
- "Safe Launch CP 作为一个单独文件，版本号是多少？谁批准的？批准日期？"
- "Safe Launch CP 里的每项检验，实际操作中有没有记录表？记录表有没有 Safe Launch 标记？"
- "如果一个检验员发现 Safe Launch CP 的某项超标但不确定是否要升级——反应计划写的是什么？他实际操作中按反应计划做了吗？"

**Layer 2 — 统计基础**
- "90 天退出标准，是基于什么统计假设？你需要多少个数据点才能证明过程有能力？如果月产量很低（<100 件），90 天够吗？"
- "Safe Launch CP 要求 Cpk/Ppk 达到什么水平才允许退出？如果你的 Cpk 在 90 天达标但第 91 天就掉下去了，说明 Safe Launch 退出条件本身有问题——当初是怎么定的？"
- "Safe Launch 期间收集的 SPC 数据，退出时要做回顾分析吗？谁分析？分析完写在哪个文件里？"

**Layer 3 — 变更联动**
- "如果 Safe Launch 期间发现需要对 PFMEA 进行修订（比如识别出了新的失效模式），这是否自动触发 Safe Launch 时钟重置？"
- "Safe Launch 退出批准流程是什么？需要客户 SQE 确认吗？需要内部什么层级批准？"
- "Safe Launch 退出后，Safe Launch CP 怎么处置——归档还是废弃？里面的增强控制有没有部分保留进量产 CP？如果有，依据是什么？"

## S3 | 反事实挑战

1. "假设过程本身不稳定但 Safe Launch CP 恰好没覆盖到那个不稳定维度——90 天零缺陷退出后才发现问题。这说明 Safe Launch CP 的设计本身有盲区。你怎么验证 Safe Launch CP 的检验项目覆盖了所有关键风险维度？"
2. "如果你在第 89 天发现一个轻微偏离（你正在犹豫要不要升级），错过了 90 天窗口而进入量产 CP——这个偏离在量产 CP 的更低频次检验下还检得出吗？如果检不出，它会在客户那里暴露吗？"
3. "假设退出 Safe Launch 后第 3 天就发生客户投诉——退出决定会被怎么审视？Safe Launch 退出审批记录能否证明退出决定的合理性？"

## S4 | 答案评分

评分维度：**文件完整性**、**执行追溯性**、**统计严谨性**、**交接透明度**

| 等级 | 标准 |
|------|------|
| Insufficient | 无单独的 Safe Launch CP；退出条件未定义或只说"90 天"无具体指标；操作人员不知道当前在 Safe Launch 期；无 Safe Launch 专属检验记录 |
| Basic | Safe Launch CP 存在且单独成文；退出条件有定量指标（≥90 天、零缺陷、Cpk 达标）；现场有 Safe Launch 标识；Safe Launch 记录可追溯到增强频次 |
| Excellent | Safe Launch CP 基于正式风险分析（逆向 PFMEA）生成；退出条件有统计依据且按产量调整；Safe Launch 数据有回顾分析报告；退出审批链完整含客户确认；Safe Launch CP 与量产 CP 的过渡有书面判定依据；增强控制有选择性地移植进量产 CP 并有记录 |

## S5 | 输出格式

```json
{
  "safe_launch_trigger": {
    "event_type": "new_program_sop | engineering_change | ppap_resubmission | plant_transfer | restart",
    "event_description": "string",
    "start_date": "string",
    "planned_end_date": "string",
    "days_completed": 0,
    "days_remaining": 0
  },
  "safe_launch_cp": {
    "document_id": "string | null",
    "revision": "string | null",
    "approved_by": "string | null",
    "approval_date": "string | null",
    "enhanced_inspection_items": 0,
    "spc_frequency": "string | null",
    "vs_production_cp_differences": ["string"]
  },
  "exit_criteria": {
    "consecutive_days_required": 90,
    "zero_defects_scope": "customer_escape_only | all_safe_launch_cp_deviations",
    "cpk_threshold": 0.0,
    "ppk_threshold": 0.0,
    "customer_approval_required": false,
    "internal_approval_level": "string | null"
  },
  "extension_triggers": [
    {
      "event": "quality_spill | process_change | safety_incident | pfmea_revision",
      "reset_clock": true,
      "authorized_by": "string"
    }
  ],
  "current_status": {
    "any_deviations_during_safe_launch": false,
    "deviations_detail": ["string"],
    "clock_reset_count": 0,
    "last_reset_date": "string | null",
    "ready_to_exit": false
  },
  "confidence": 0.0
}
```

## 纠偏原则 / 禁止项

| 禁止 | 替代方向 |
|------|---------|
| 把量产 CP 当作 Safe Launch CP | 必须单独成文，标题注明"Safe Launch"，与量产 CP 并行放置 |
| "90 天到了所以退出" | 退出需要有统计数据支撑，不只是天数到了 |
| Safe Launch 期间偏离不记录 | 任何 Safe Launch CP 检测到的偏离都记录，按反应计划处理，不隐瞒 |
| Safe Launch 退出后直接丢弃 CP | 退出的 Safe Launch CP 归档保留；部分增强控制可能有移植价值 |
| 仅按日历天数判断退出 | 同时需要按生产天数/生产数量调整——低产量产品 90 个日历天数据点不足 |
| 不区分 Safe Launch 和 D3 围堵 | Safe Launch 是预防性增强控制，D3 围堵是问题发生后隔离——两者目的不同，但 Safe Launch 期间发生质量溢出时 D3 围堵也需启动 |
