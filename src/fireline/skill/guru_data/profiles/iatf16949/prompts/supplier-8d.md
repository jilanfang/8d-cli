# supplier-8d — Supplier 8D Flow-Down Management

## 行业背景

IATF 16949 第 8.4.2.4 条（供应商纠正措施）和第 8.4.2.4.1 条（供应商问题解决）明确要求：当供应商交付的产品或服务出现不符合时，组织必须确保供应商启动结构化问题解决流程（即 8D 或等效方法）。这不仅仅是"给供应商发一个 SCAR 然后等他们回复"——组织有责任验证供应商的根因分析质量、措施有效性、以及闭环的持久性。

常见陷阱（也是 IATF 审核中最常被开不符合项的做法）：收到供应商 8D 报告后直接存档，没有独立验证供应商的根因结论、没有核对供应商的过程能力数据是否支持他们的结论、没有检查供应商的 8D 闭合日期是否逾期。当你的 8D 涉及 Tier 2 供应商（甚至 Tier 3、Tier 4），供应链的可追溯性变弱但合规责任不减——供应商 8D 的深度逐级传导。

IATF 第 8.4.2.4.1 条增加了"第二方审核"的要求：当供应商反复发生问题或问题严重时，组织应进行现场过程审核，不仅看 8D 报告还要看措施是否真的在产线上落地。

## S1 | 发散探索 — 多角度触发器

Agent 从以下问题中选 3-4 个向用户提问。

1. **触发判断**："当前 8D 是否涉及供应商来料/服务？如果是——供应商是在哪个环节被确认的？是来料检验、产线发现、还是客户退回的故障件分析后追溯到供应商？"

2. **供应商 8D 启动状态**："你有没有给供应商发正式的 SCAR 或 8D 请求？什么时候发的？供应商有没有确认收到？供应商有没有给出 8D 团队名单和时间计划？供应商的 deadline 是什么？"

3. **供应商报告验证机制**："供应商的 8D 报告你怎么验证？是看了报告就签字，还是会去现场做第二方过程审核？你有没有供应商 PFMEA 和控制计划的副本可以交叉核对他们的根因结论？"

4. **Tier N 管理**："如果这个供应商的问题根源又来自他的供应商（Tier 3），你对 Tier 3 有可见性吗？你能不能要求 Tier 2 把他 Tier 3 的 8D 报告流转给你？合同里有没有这个权利？"

5. **来料检验联动**："供应商的这个缺陷在你的来料检验中是否应该被发现但没被发现？如果是——你的来料检验计划是否需要更新？来料检验标准是否需要覆盖这个新失效模式？"

## S2 | 第一性原理收敛

追问链 —— 从"供应商给我报告了"追到"我独立确认了供应商的结论是真的"。

**Layer 1 — 供应商 8D 请求质量**
- "你发给供应商的不是一句'请做 8D'吧？你的 SCAR 里有没有附上你的失效分析数据、D2 问题定义、缺陷照片/测量数据、你的初步判断？供应商收到的输入够具体吗？"
- "你要求的供应商 8D 格式——是你给他一个标准格式，还是他用自己的格式？你检查过他的格式是否符合 AIAG CQI-20 / IATF 16949 最低要求吗？"
- "你给供应商的 deadline 是什么？这个 deadline 和你的客户给你的 deadline 是什么关系？供应商晚交会不会影响你向客户按时提交 8D？"

**Layer 2 — 根因分析质量验证**
- "供应商的 D4 5-Why——能不能追到控制点失守？还是停在了'操作员失误'或'设备老化'？你能不能独立判断供应商的根因深度够不够？还是你只会看有没有填完表格？"
- "供应商有没有对每一个根因做了主动验证（如 Red Rabbit、让根因"开/关"确认因果关系）？还是只是'根据经验判断'？"
- "供应商的 D5 PCA 是否对应了每个根因？措施是 Poka-Yoke 消除级还是增强检测？对 CC/SC 特性是否有特殊控制？"

**Layer 3 — 实施验证独立确认**
- "供应商提交了 D6 验证数据——你核对过原始数据吗（SPC 图、测量日志、检查记录）还是只看汇总数据？你怎么知道数据不是编的？"
- "你来料检验能不能独立验证供应商的 PCA 有效？来料检验的频次/方法是否已经更新以验证供应商的措施？"
- "供应商有没有把这次 8D 的结果更新到他的 PFMEA 和控制计划？你有没有要求提供更新后的文件？你有没有检查更新是否合理（比如 RPN 是否真的降了）？"

**Layer 4 — 闭环与持续**
- "供应商的 8D 关闭后，你有什么跟踪机制保证措施不会倒退？供应商的后续交付批次的来料检验数据有改善吗？如果 6 个月内复发有什么升级机制？"
- "在供应商年度评审/过程审核中，你是否将此 8D 纳入审核检查表进行现场验证？"

## S3 | 反事实挑战

1. "如果供应商的 D4 根因是错的——他们追到了'设备精度不足'但实际上是模具温度波动——你怎么能发现这个错误？你独立分析过他们的工艺吗？还是你没有数据/能力去挑战他们的结论？"
2. "如果供应商嘴上说 PCA 已实施但实际上产线什么也没改——你怎么验证？你的第二方审核能不能覆盖这个具体工序？你的来料检验能不能测出 PCA 没实施的效果？"
3. "假设供应商提交了完美的 8D 报告但 3 个月后同样问题复发——你们当初的闭环节点检查了什么？有没有留下来什么证据能证明你们当时的验收是合理的？"

## S4 | 答案评分

评分维度：**触发及时性**、**输入充分性**、**验证独立度**、**Tier N 追溯深度**、**闭环持久性**

| 等级 | 标准 |
|------|------|
| Insufficient | 未给供应商发正式 SCAR/8D 请求；供应商 8D 报告直接存档未验证；供应商根因深度未评估；无来料检验联动；无供应商审核计划 |
| Basic | 供应商正式收到 SCAR 且回复了 8D 报告；供应商 8D 的每个 D 经过书面审查，根因≥3 层深；来料检验已根据失效模式调整了检验项目；供应商 PCA 验证数据已收到并核对 |
| Excellent | 供应商 8D 每 D 独立评估打分，不达标发回重做；对关键供应商（涉及 CC/SC/重复发生）已进行现场第二方审核验证 PCA 落地；来料检验有独立证据证明供应商措施有效（至少 3 批连续合格 + 过程能力数据）；Tier 3 及更深 8D 已列入合同且向下传导；供应商 8D 已登记到供应商质量管理系统中并关联到年度过程审核计划；供应商 PFMEA/CP 更新已获取并核实 |

## S5 | 输出格式

```json
{
  "supplier_identification": {
    "supplier_name": "string",
    "supplier_code": "string",
    "supplier_tier": "T1 | T2 | T3 | beyond",
    "part_number_supplied": "string",
    "characteristic_involved": "CC | SC | HIC | standard",
    "discovered_at": "incoming_inspection | production_line | customer_return | field_failure"
  },
  "scar_issuance": {
    "scar_id": "string | null",
    "issued_date": "string | null",
    "format_provided": "8D | SCAR | customer_template",
    "supporting_data_attached": false,
    "deadline_assigned": "string | null",
    "deadline_met": false
  },
  "supplier_8d_quality_review": {
    "d1_status": "pass | fail | not_reviewed",
    "d2_status": "pass | fail | not_reviewed",
    "d3_status": "pass | fail | not_reviewed",
    "d4_depth_layers": 0,
    "d4_root_cause_verified_independently": false,
    "d5_pca_pokayoke_level": "elimination | detection | mitigation | none",
    "d6_cp_evidence_type": "spc_chart | measurement_log | red_rabbit | attestation_only",
    "d7_pfmea_cp_updated": false,
    "d8_closure_signed": false,
    "overall_rating": "Insufficient | Basic | Excellent"
  },
  "tier_n_cascade": {
    "deeper_tier_involved": false,
    "tier_n_supplier_name": "string | null",
    "tier_n_8d_requested": false,
    "tier_n_8d_received": false,
    "cascade_contractual_right": false
  },
  "incoming_inspection_linkage": {
    "inspection_plan_updated": false,
    "new_inspection_characteristic_added": false,
    "sampling_frequency_increased": false,
    "consecutive_ok_batches": 0
  },
  "second_party_audit": {
    "planned": false,
    "completed": false,
    "audit_date": "string | null",
    "pca_verified_on_site": false,
    "findings": ["string"]
  },
  "confidence": 0.0
}
```

## 纠偏原则 / 禁止项

| 禁止 | 替代方向 |
|------|---------|
| 收到供应商 8D 报告直接存档 | 逐 D 评估供应商 8D 质量；根因停在"操作员"或"设备老化"等表层的发回重做；验证数据只看汇总不看原始数据的追问 |
| 不给供应商提供你的失效分析数据 | 供应商收不到完整信息不可能追到真根因——附上缺陷照片、测量数据、你做的初步分析 |
| 把供应商 8D 当作你自己 8D 的 D4 | 你的 D4 要分析的是"为什么你的供应商管理体系允许这个缺陷进入"，不是"供应商的根因是什么" |
| Tier 3 及以下不可见就不管 | 合同更新时加入供应商 8D 向下传导条款；关键特性（CC/SC）的 Tier N 必须可见 |
| 供应商措施验证只看报告不检查实物 | 来料检验独立验证；有条件的做 Red Rabbit 测试（故意放入已知缺陷品看能否被拦截）；高风险项做现场第二方审核 |
| 供应商端闭环后你的来料检验不调整 | 来料检验标准和频次根据本次失效模式调整；增加覆盖该失效模式的检验项，至少保持 3 批增强检验 |
