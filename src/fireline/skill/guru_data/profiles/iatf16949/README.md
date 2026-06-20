# IATF 16949 Profile for 8d-guru

将此 profile 叠加到 8d-guru 基础 skill 上，Agent 会自动融合汽车行业的专属要求。

## 适用场景

- 你是 Tier-1/2 汽车零部件供应商
- 你的客户是 OEM（Stellantis/GM/BMW/Ford/VW/Toyota 等）
- 你的质量管理体系需满足 IATF 16949:2016 审核
- 客户投诉需要通过 Amadeus/SQP/GQTS/NCT 等门户系统提交 8D

## 核心差异（vs 基础 8d-guru）

| 领域 | 基础 8d-guru | + IATF 16949 Profile |
|------|------------|---------------------|
| 根因分析 | TRC + MRC + Escape Point（3 轨） | Occurrence + Non-Detection + Systemic（3 轨）+ PFMEA 行追溯 |
| 特殊特性 | 不涉及 | CC（▽）/SC（◇）/HIC 全链标记和管控 |
| 围堵时效 | 方法驱动 | 24hr 初次回应 + 48hr 围堵计划提交（OEM CSR） |
| 验证 | 统计证据推荐 | Cpk≥1.33（SC）/Ppk≥1.67（CC）强制 + Red Rabbit 强制 |
| PPAP | 不涉及 | PCA 对 PPAP/PSW 的影响评估 + 客户通知/重新批准 |
| 防错 | Poka-Yoke 三级推荐 | CC → 消除级强制（IATF 10.2.4） |
| 预防 | Yokoten | Yokoten + PFMEA RPN 降低 + APQP 检查清单 + 年度评审 |
| 供应商 | 不涉及 | 供应商 8D 流延 + Tier N 管理（IATF 8.4.2.4.1） |
| 结案 | 团队签核 | 客户签核 + PPAP 状态确认 + Safe Launch 退出 + 供应商闭环 |

## 文件结构

```
profiles/iatf16949/
├── SKILL.md                 ← 激活 manifest：触发词、IATF 条款识别
├── overlay.md               ← D0-D8 每个阶段的 IATF 叠加要求表（含条款号）
├── prompts/
│   ├── safe-launch.md       ← Safe Launch 90 天强化遏制
│   ├── special-chars.md     ← CC/SC/HIC 特殊特性管理
│   ├── csr-check.md         ← 客户特殊要求（CSR）检查
│   ├── supplier-8d.md       ← 供应商 8D 流延
│   └── ppap-impact.md       ← PCA 对 PPAP 影响评估
├── references/
│   ├── clauses.md           ← IATF 16949 条款速查
│   ├── oem-timelines.md     ← 主流 OEM 8D 响应时限
│   └── characteristic-types.md ← 特殊特性分类和标准
└── examples/
    └── auto-8d-walkthrough.md ← 汽车行业完整 8D 走查
```

## 使用方式

```
Agent 检测到：用户提到"IATF""16949""PPAP""OEM""特殊特性"等 → 自动加载此 profile
Agent 在每个 D 做：先查 overlay.md 看本 D 有无 IATF 特化要求 → 有则追问 → 按基础流程推进
```
