# csr-check — Customer-Specific Requirements Check

## 行业背景

IATF 16949 第 4.3.2 条明确规定：组织必须识别、评估并满足客户特定要求（CSR）。这不是"参考一下"——它是认证审核的强制项。每家 OEM 和 Tier 1 都有自己的 8D 格式、提交流程、时效要求、升级规则、以及特定的质量门户系统。如果你给 Stellantis 提交了一份 AIAG CQI-20 标准 8D 但没有用 Amadeus 系统、没有按他们要求的三重根因格式、没有在 14 天内结案——8D 再好也是不合格。

CSR 的难度在于每个 OEM 的规则不同且不定期更新。Stellantis 有 CSB-Seller 门户 + Amadeus + 强制 NTF 追踪。GM 用 SQP 系统 + GP-5 格式 + PR/R 闭环。BMW 有 GQTS + VDA 8 标准 + QZ 评分体系。Ford 有 Q1 + G8D 格式 + NTF 流程。Toyota 有 TMC 8D 格式 + Hoshin + NCT 系统。而 Tier 1（Bosch、Continental、ZF、Magna 等）通常在自己 OEM CSR 基础上再加一层内部要求。

IATF 16949 第 10.2.3 条进一步要求问题解决过程必须包含"分析并消除根本原因"，CSR 则具体规定了分析格式和深度。如果你不知道客户的特殊要求，你不可能合规做 8D。

## S1 | 发散探索 — 多角度触发器

Agent 从以下问题中选 3-4 个向用户提问。

1. **OEM/Tier 1 识别**："你的客户是谁？是 OEM（Stellantis/GM/BMW/Ford/VW/Toyota/Honda/Nissan/Volvo/JLR/Geely...）还是 Tier 1 供应商（Bosch/Continental/ZF/Magna/Denso/...）？有没有一个以上的客户涉及？不同客户的 CSR 可能不同。"

2. **CSR 文档获取**："你有没有客户的供应商质量手册（Supplier Quality Manual / SQE Requirements Manual）？你知不知道客户的 CSR 文件在哪个系统里？最新版是哪年哪月发布的？你有没有读过与本 8D 相关的具体章节？"

3. **8D 格式与模板**："客户有没有指定 8D 报告必须用特定格式？比如 GM 用 GP-5、Ford 用 G8D、BMW 用 VDA 8 格式、Stellantis 用 Amadeus 里的 8D 模板？还是客户接受 AIAG CQI-20 标准格式？你手上有没有这个模板？"

4. **提交门户与时效**："客户要求通过什么系统提交 8D？是 Amadeus？SQP？GQTS？NCT？还是邮件发 PDF？首次响应（D1-D3）的 deadline 是多少小时？完整 8D（D0-D8）的 deadline 是多少天？从什么问题确认时间开始算的？"

5. **升级规则**："客户有没有规定——什么情况下需要升级到 SQE 经理？什么情况升级到采购总监？什么情况升级到 VP 级别？升级触发条件是什么（安全/重大质量/延迟关单/重复发生）？目前的 8D 需要升级吗？"

6. **PCA 预批准**："客户的 CSR 是否要求 PCA 实施前必须先交客户批准？如果不经批准实施了 PCA，客户会怎么处理？有没有要求 PCA 必须包含 Poka-Yoke？还是可以接受增强检测？"

## S2 | 第一性原理收敛

追问链 —— 把"客户要求"从口头说法追到文件证据。

**Layer 1 — CSR 文档证据**
- "你说客户的 CSR 是 XX——能不能把客户供应商质量手册的那一页或那个章节内容发给我？或者引用具体条款号？"
- "客户的 CSR 文件版本号和发布日期是什么？自上次 8D 以来有没有更新过？你怎么跟踪 CSR 更新的？"
- "客户的 8D 相关 CSR 里，有没有提到'不一致处理''问题解决''纠正措施'之外的隐藏要求？比如要求用 SCAR 还是 CAR？"

**Layer 2 — 格式与内容具体化**
- "客户要求的三重根因格式——是要求分别写 Occurrence + Non-Detection + Systemic？还是按 VDA 区分 Technical Root Cause + Managerial Root Cause？还是客户有自己独特的三分类系统？"
- "客户要求的证据链——是只要 PCA 验证数据？还是要求 Red Rabbit 结果？还是要求过程能力报告？还是三者都要？"
- "客户的 8D 评分标准是什么？有没有类似 BMW QZ（Qualitaetszahl）的评分体系？你的 8D 会被打分吗？这个分数会影响供应商评级吗？"

**Layer 3 — 系统与流程细节**
- "客户门户提交 8D 有没有附件格式/大小限制？是否需要同时上传 PDF 版本？是否需要将原始数据（SPC 图、测量原始数据）一并打包上传？"
- "客户 8D 审批流程是什么——SQE 初审 → SQE 经理复审 → QA 终审？每个环节的典型处理时间是多少？你有没有跟踪每一个审批节点？"
- "如果在审批中被驳回——客户是退回整份 8D 还是只退回某个 D？驳回有书面理由吗？驳回后的重新提交 deadline 比首次 deadline 更紧吗？"

## S3 | 反事实挑战

1. "如果你的 8D 在 D5 阶段发现客户其实要求 PCA 必须加 Poka-Yoke（但你没有计划加），这份 8D 会被拒到什么程度？客户的后果是什么——新业务暂停？Q-Status 降级？CSR 里有写吗？"
2. "如果客户 SQE 换了人（新 SQE 对格式/深度的要求和老 SQE 不同），你之前按老 SQE 偏好做的 8D 会不会被新 SQE 打回？你们内部有没有标准化的 CSR 合规检查表，不依赖个人关系？"
3. "假设你按 AIAG CQI-20 标准做了 8D，但客户 CSR 说'不接受 AIAG 格式，必须用我们自己的模板'——现在你已经投入了 5 天，怎么补救？你怎么确保下次一开始就对了？"

## S4 | 答案评分

评分维度：**CSR 获取完整度**、**格式匹配度**、**时效合规性**、**系统操作能力**

| 等级 | 标准 |
|------|------|
| Insufficient | 不知道客户哪里写了 CSR；没有客户供应商质量手册；不知道用什么格式/系统提交；不知道 deadline；假设"客户接受标准格式" |
| Basic | 已获取客户供应商质量手册或等效 CSR 文档；明确知道提交格式/模板；明确知道首次响应和完整 8D 的 deadline；知道要用什么系统提交（Amadeus/SQP/GQTS/NCT 等）；CSR 文档版本号已知 |
| Excellent | CSR 文档已精读且匹配到本 8D 的具体 D；格式模板已加载且填写中；提交 deadline 已记录且建立了倒计时提醒；升级触发条件已评估且当前状态不需升级；客户 SQE 已沟通且确认了要求；PCA 预批准要求已明确；有内部 CSR 合规检查表确保不遗漏 |

## S5 | 输出格式

```json
{
  "customer": {
    "name": "string",
    "type": "OEM | Tier_1 | Aftermarket",
    "sqe_name": "string | null",
    "sqe_contact": "string | null"
  },
  "csr_document": {
    "title": "string | null",
    "document_id": "string | null",
    "revision_date": "string | null",
    "revision_version": "string | null",
    "relevant_sections": ["string"],
    "obtained": false
  },
  "8d_submission": {
    "required_format": "GP-5 | G8D | VDA_8 | AIAG_CQI-20 | customer_custom",
    "template_available": false,
    "submission_system": "Amadeus | SQP | GQTS | NCT | email | other",
    "system_access_confirmed": false,
    "initial_response_deadline_hours": 0,
    "full_8d_deadline_days": 0,
    "deadline_clock_start": "string | null",
    "attachments_required": ["string"]
  },
  "escalation": {
    "triggers_defined": false,
    "current_level": "SQE | SQE_Manager | Purchasing_Director | VP | none",
    "escalation_needed_now": false
  },
  "pca_pre_approval": {
    "required_by_customer": false,
    "pokayoke_required_for_cc": false,
    "approval_status": "not_required | pending | approved | rejected"
  },
  "csr_compliance_ready": false,
  "confidence": 0.0
}
```

## 纠偏原则 / 禁止项

| 禁止 | 替代方向 |
|------|---------|
| 假设客户接受标准 AIAG 格式 | 逐客户核对：Stellantis → Amadeus 模板、GM → GP-5、Ford → G8D、BMW → VDA 8 |
| 不知道 CSR 在哪就不查 | 客户供应商门户、采购合同附件、质量协议附件、SQE 直接问——四个渠道至少走一个 |
| 不管时效 | D0 一启动就设计时器：24h 首次响应、14d/21d/30d 完整 8D（依客户要求） |
| 不跟踪 CSR 版本更新 | CSR 定期（至少年度）重读检查是否有版本更新；OEM 不定期改规则 |
| 忽视升级规则 | 安全/法规/重大金额/重复发生——四类事件必须逐一评估是否触发升级 |
| 用"客户没说"当不做的理由 | 客户不主动说的 CSR 也是最容易在审核中被发现的不符合项——主动问、主动要 |
