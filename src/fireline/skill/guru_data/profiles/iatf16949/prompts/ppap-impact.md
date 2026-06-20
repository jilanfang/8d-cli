# ppap-impact — PPAP Impact Assessment for PCA

## 行业背景

PPAP（生产件批准程序）第 4 版是 AIAG 发布的汽车行业通用标准，定义了从"样件批准"到"量产件批准"的完整证据包。IATF 16949 第 8.3.4.4 条（产品批准过程）强制要求组织符合一个产品批准程序——PPAP 是其中最主要的实现。当 8D 中的纠正措施（PCA/D5）涉及设计、材料、工艺、生产地、或检验方法的变更时，必须评估对已批准 PPAP 状态的影响。

这个评估不是可选项。它直接决定了：是否需要重新提交 PSW（零件提交保证书）、需要什么 PPAP 提交等级（1-5）、是否需要客户通知甚至客户重新批准、以及是否需要启动新的 Safe Launch 期。IATF 审核中，做了一个涉及设计/工艺变更的 PCA 但没有更新 PPAP 状态，是高频严重不符合项（8.3.4.4）。

PPAP 第 4 版第 3 节定义了提交等级 1-5：Level 1 只交 PSW、Level 3 交全部 18 项、Level 5 是 Level 3 加客户现场审核。涉及 CC/SC 的变更通常不允使用 Level 1——客户 CSR 会指定最低等级。

## S1 | 发散探索 — 多角度触发器

Agent 从以下问题中选 3-4 个向用户提问。

1. **当前 PPAP 状态确认**："这个产品的 PPAP 当前是什么状态？PSW 批准日期？是 Full Approval 还是 Interim Approval？还是还没有正式批准（比如还在 Safe Launch 期用 Interim PSW）？最近一次 PPAP 提交等级是 Level 几？"

2. **PCA 影响判断**："D5 的每项纠正措施——是否涉及：设计变更（图纸/DV/材料规范）、工艺变更（PFMEA/控制计划/过程流程图）、生产地转移/产线变更、供应商变更（二级或以下供应商更换）、或检验方法/频次变更？如果至少涉及一项，必须评估 PPAP 影响。"

3. **变更等级分类**："这个变更是属于'不需要客户通知的内部变更'，还是'需要客户通知但不一定需要重新 PPAP'，还是'绝对要重新 PPAP 提交'？按 PPAP 第 4 版表 3.1 分类。谁做的这个分类判断？"

4. **客户通知要求**："客户的 CSR 对变更通知有什么特殊要求？有些 OEM（比如 GM）要求任何涉及 CC/SC 的变更必须提前 30 天书面通知。你知不知道客户的通知时间要求？有没有标准的客户通知单模板？"

5. **Safe Launch 联动**："如果这个 PCA 触发了 PPAP 重新提交——是否需要同步启动新的 Safe Launch 期？Safe Launch 期间的要求（增强检验、SPC 频次、退出标准）和当前 Safe Launch 有什么不同？"

## S2 | 第一性原理收敛

追问链 —— 从"可能需要 PPAP"追到"具体要交什么、怎么交、客户批不批"。

**Layer 1 — 变更与 PPAP 表 3.1 精确匹配**
- "你有 PPAP 第 4 版表 3.1 的副本吗？你有没有逐条把你的 PCA 变更和表 3.1 的内容对过？匹配结果是什么——是客户通知类（Notifications）还是需重新提交类（Re-submission）？"
- "PCA 涉及的设计变更——图纸修订级别有没有变？材料规范有没有变？如果有设计变更，DRE（设计责任工程师）有没有签核？设计变更是否已反映到 DFMEA 中？"
- "PCA 涉及的工艺变更——是改了哪个工序？新工序和新老工序的差别是什么？过程流程图更新了吗？PFMEA 受影响行更新了吗？控制计划更新了吗？"

**Layer 2 — 提交等级确定**
- "如果需要重新 PPAP，提交等级是几级？由谁定？按客户 CSR 还是按 PPAP 手册默认规则？涉及 CC/SC 时客户要求 Level ≥ 3 吗？"
- "Level 3 提交需要 18 项全交——你现在有没有一个 PPAP 交付包清单列出每项的状态？哪些已经有最新数据？哪些需要重做？"
- "如果只需要客户通知不需要全 PPAP——通知单里要写什么？变更描述、受影响零件号、变更原因、实施日期、验证数据摘要——这些都准备好了吗？"

**Layer 3 — 客户批准流程**
- "客户 SQE 对 PSW 重新批准的流程是什么？多长处理周期？是否需要同时提交 D6 验证数据（Cpk/Ppk/SPC 数据）？"
- "如果客户批的是 Interim Approval（临时批准）——Interim 的条件是什么？限制多少件？限制多久？过期没拿到 Full Approval 会怎样？"
- "PCA 实施无法等客户批准完成（比如围堵窗口紧）——你有什么紧急变更流程？实施前有没有和客户 SQE 沟通取得邮件确认？"

**Layer 4 — PPAP 状态归档与更新**
- "PPAP 重新批准通过后，旧的 PPAP 包怎么处置——归档？旧 PSW 标记'过期'？所有受影响的文件（DFMEA/PFMEA/CP/SOP/图纸）是否同步更新并确保引用新的 PPAP 编号？"
- "如果有多个客户共享这个零件（比如同一零件同时供给 GM 和 Ford）——每个客户是否需要独立的 PPAP 重新提交？还是可以共享 PPAP？"

## S3 | 反事实挑战

1. "如果 PCA 实施后你判断'不需要重新 PPAP，只需要客户通知'——但 3 个月后客户 SQE 在审核中判断这是需要重新 PPAP 的变更，后果是什么？你会被要求补 PPAP 吗？补 PPAP 期间产品还能继续发货吗？你的判断有什么证据支撑？"
2. "如果 PSW 重新提交到客户那里被拒了——最可能的拒绝原因是什么（提交等级不对/PSW 格式不对/验证数据不够/样本量不够/过程能力不达标）？你有没有先做内部预审？"
3. "假设 PCA 涉及供应商端的工艺变更——供应商有没有同步做 PPAP 重新提交？如果供应商的 PPAP 没做而你用这个供应商的零件发了货，合规责任在谁？"

## S4 | 答案评分

评分维度：**PPAP 状态认知**、**变更分类准确度**、**提交等级正确性**、**客户通知合规性**、**文档联动完整度**

| 等级 | 标准 |
|------|------|
| Insufficient | 不知道当前 PPAP 状态；PCA 涉及设计/工艺变更但未评估 PPAP 影响；没有 PPAP 表 3.1 分类流程；不知道客户的变更通知要求 |
| Basic | 当前 PPAP 状态明确（PSW 编号、批准日期、状态）；PCA 逐项和 PPAP 表 3.1 匹配，变更分类明确（通知/重新提交）；提交等级已确定且符合客户 CSR；客户通知流程已启动或已完成；PFMEA/CP/SOP 已同步更新 |
| Excellent | PPAP 影响评估有书面记录（逐项 PCA 对照表 3.1、分类理由、判断人签字）；重新提交 PPAP 交付包 18 项清单逐项有状态和负责人；客户通知/批准流程有邮件或系统记录；多个客户场景已分别评估；供应商端 PPAP 联动已确认；PSW 重新批准收到且有客户签章；旧 PPAP 包已标记过期；新 Safe Launch 期已启动（如果需要）；PPAP 影响评估归档为 8D 附件 |

## S5 | 输出格式

```json
{
  "current_ppap_status": {
    "psw_number": "string | null",
    "submission_level": "1 | 2 | 3 | 4 | 5",
    "approval_status": "full_approval | interim_approval | rejected | not_submitted",
    "approval_date": "string | null",
    "safe_launch_active": false,
    "safe_launch_end_date": "string | null"
  },
  "ppap_impact_assessment": [
    {
      "pca_reference": "string",
      "change_type": "design | material | process | supplier | inspection | location | other",
      "ppap_table_3_1_classification": "no_notification | notification_only | resubmission_required",
      "reason_for_classification": "string",
      "assessed_by": "string | null",
      "assessed_date": "string | null"
    }
  ],
  "resubmission_required": false,
  "resubmission_plan": {
    "new_submission_level": 0,
    "level_determined_by": "customer_csr | ppap_manual_default",
    "ppap_package_checklist": [
      {"element": 1, "name": "设计记录", "status": "ready | needs_update | not_applicable", "owner": "string"},
      {"element": 2, "name": "工程变更文件", "status": "ready | needs_update | not_applicable", "owner": "string"},
      {"element": 3, "name": "客户工程批准", "status": "ready | needs_update | not_applicable", "owner": "string"},
      {"element": 4, "name": "DFMEA", "status": "ready | needs_update | not_applicable", "owner": "string"},
      {"element": 5, "name": "过程流程图", "status": "ready | needs_update | not_applicable", "owner": "string"},
      {"element": 6, "name": "PFMEA", "status": "ready | needs_update | not_applicable", "owner": "string"},
      {"element": 7, "name": "控制计划", "status": "ready | needs_update | not_applicable", "owner": "string"},
      {"element": 8, "name": "测量系统分析", "status": "ready | needs_update | not_applicable", "owner": "string"},
      {"element": 9, "name": "尺寸结果", "status": "ready | needs_update | not_applicable", "owner": "string"},
      {"element": 10, "name": "材料/性能试验结果", "status": "ready | needs_update | not_applicable", "owner": "string"},
      {"element": 11, "name": "初始过程研究", "status": "ready | needs_update | not_applicable", "owner": "string"},
      {"element": 12, "name": "合格实验室文件", "status": "ready | needs_update | not_applicable", "owner": "string"},
      {"element": 13, "name": "外观批准报告", "status": "ready | needs_update | not_applicable", "owner": "string"},
      {"element": 14, "name": "生产件样品", "status": "ready | needs_update | not_applicable", "owner": "string"},
      {"element": 15, "name": "标准样品", "status": "ready | needs_update | not_applicable", "owner": "string"},
      {"element": 16, "name": "检查辅具", "status": "ready | needs_update | not_applicable", "owner": "string"},
      {"element": 17, "name": "客户特殊要求", "status": "ready | needs_update | not_applicable", "owner": "string"},
      {"element": 18, "name": "零件提交保证书 PSW", "status": "ready | needs_update | not_applicable", "owner": "string"}
    ]
  },
  "customer_notification": {
    "notification_required": false,
    "notification_sent_date": "string | null",
    "customer_acknowledged": false,
    "customer_approval_received": false,
    "customer_approval_reference": "string | null",
    "notification_method": "portal | email | formal_letter | other"
  },
  "supplier_ppap_linkage": {
    "supplier_change_involved": false,
    "supplier_ppap_resubmission_required": false,
    "supplier_psw_received": false
  },
  "safe_launch_linkage": {
    "new_safe_launch_required": false,
    "safe_launch_cp_ready": false,
    "safe_launch_start_date": "string | null"
  },
  "confidence": 0.0
}
```

## 纠偏原则 / 禁止项

| 禁止 | 替代方向 |
|------|---------|
| PCA 涉及设计/工艺变更但不评估 PPAP 影响 | D5 每个 PCA 写完立即评估表 3.1 分类——不是 D8 才做 |
| "这是微小变更不用 PPAP"但没有分类记录 | 所有变更分类必须有书面记录、判断理由、判断人签字；微小变更也可能需要客户通知 |
| PSW 重新提交用 Level 1 但涉及 CC/SC | 涉及 CC/SC 的变更，客户 CSR 通常要求 Level ≥ 3；Level 1 只交 PSW 没有过程能力数据不足以证明安全 |
| 客户通知和 PPAP 重新提交不分清 | 通知只是告知、重新提交需要客户签回 PSW——两个不同义务，有些变更两个都要做 |
| 只评估自己工厂的变更，不管供应商端的联动 | PCA 涉及供应商变更时，要求供应商同步做 PPAP 影响评估，作为你 PPAP 包的附件 |
| PPEA 影响评估和 8D 脱节 | PPAP 影响评估结果应作为 D5 交付物的一部分（或 D8 附件），不要单独存档 |
| 多客户场景只做一个 PPAP | 不同客户可能有不同 PPAP 要求/不同 PSW 模板——逐客户评估 |
