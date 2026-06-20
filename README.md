# 8D-CLI

> 给你的 AI Agent 一个质量工程师的大脑。不是填 8D 模板，是把 8D 调查做对。

Give your AI agent a quality engineer's brain. Not here to fill out your 8D report — here to help you do the investigation properly.

---

## 为什么需要 8D-CLI？

工厂出了质量问题，客户投诉来了，体系要求 24 小时内响应。现实是：

- **8D 模板到处都有，但没人敢追问你**。填完 D4 "根因：操作员失误"，报告就交了，问题下周复发。
- **质量团队人手不够**。有经验的 QE 在忙别的事，新人不知道怎么追 5-Why，不知道 Escape Point 是什么。
- **IATF 16949 审核会翻旧账**。三个月前的 8D 报告被审核员挑出来: "这个 5-Why 停在责任归属，不算根因。"

8D-CLI 做的事：挂载 [8d-guru](https://github.com/jilanfang/8d-guru) 的方法论技能，把 42 个问题点按 D0-D8 拆开，每一步都追问到底——从物理机制追到控制点失守，从发生原因追到流出原因，答得不够深就拦住不让过。

**一句话：你描述问题，它带着你调查。不跳过任何一步。**

---

## 和 8d-guru 的关系

**8D-CLI 是壳，8d-guru 是脑。**

```
8d-guru (纯 Markdown 技能)         8D-CLI (命令行工具)
┌────────────────────────┐        ┌──────────────────────┐
│ 42 个 S1-S5 提示词      │  挂载  │ 工厂数据 · 案件存储    │
│ 贝叶斯 · TRIZ · 门禁   │ ────→ │ LLM 对接 · 报告生成   │
│ IATF 16949 · ISO 9001  │  读取  │ 9 个 CLI 命令         │
│                        │        │                      │
│ 方法论怎么问、怎么追、    │        │ 管工厂上下文、调 LLM、  │
│ 怎么评分 —— 全在这里     │        │ 存结果 —— 不维护方法论  │
└────────────────────────┘        └──────────────────────┘
```

CLI 不自己写提示词。它的 `question` 命令做的事：从 8d-guru 读对应问题点的 markdown 文件 → 注入当前案件的工厂上下文 → 发给 LLM → 解析结果。8d-guru 更新方法论了，CLI 不用改代码，自动跟进。

另外依赖 `8d-root-cause-coach`（Python 包，藏在 8D-Agent 仓库里）做门禁校验和 5-Why 结构检查。pip install 时自动装，用户不用管。

---

## 快速上手

### 1. 安装

```bash
git clone https://github.com/jilanfang/8d-cli.git
cd 8d-cli
pip install -e ".[dev]"
```

依赖 `8d-root-cause-coach` 会自动从本地 `../8D-Agent/packages/8d-root-cause-coach` 安装。没有 8D-Agent 仓库的话，等它发布到 PyPI 后走 pip 直接装。

### 2. 配置 LLM（可选，不配也能 Mock 跑）

```bash
export FIRELINE_LLM__API_KEY="sk-your-key"
export FIRELINE_LLM__MODEL="deepseek/deepseek-chat"
```

### 3. 挂载 8d-guru（可选，但建议）

```bash
export FIRELINE_SKILL__SKILL_PATH="../8d-guru"
```

**设了之后**：CLI 从 8d-guru 的 42 个 markdown 提示词读取方法论，每个问题包含完整的 S1-S5 循环（发散探索方向、第一性追问链、证伪挑战题、答案评分量表）。

**不设**：CLI 用内置 Jinja2 模板，功能可用但提示词深度差约 10 倍。

### 4. 跑起来

```bash
# Mock 模式 —— 零成本，秒级响应
8d new "SMT产线USB接口上电无输出，批次2024W36，客户投诉" --mock

# 触发 D4 根因分析引导
8d question CASE-20260620-001 d4-q3 --mock

# 直接填答案（跳过 LLM）
8d question CASE-20260620-001 d0-q1 --answer '{"phenomenon":"USB接口无输出"}'

# 阶段推近
8d advance CASE-20260620-001 --target d5_d8

# 出报告
8d report CASE-20260620-001
```

---

## 命令一览

| 命令 | 做什么 | Mock 支持 |
|------|--------|----------|
| `8d new "原始输入"` | 从投诉/异常文本创建案件，LLM 自动提取关键信息 | ✅ |
| `8d show CASE-XXX` | 查看 D0-D8 全阶段问题点完成状态 | N/A |
| `8d question CASE-XXX d4-q3` | LLM 引导回答某个问题点 | ✅ |
| `8d question CASE-XXX d0-q1 -a '...'` | 直接保存答案，不走 LLM | N/A |
| `8d advance CASE-XXX` | 推进阶段，自动检查门禁条件 | N/A |
| `8d report CASE-XXX` | 生成 8D 报告草案（纯本地，不调 LLM） | N/A |
| `8d cases` | 列出工厂所有案件 | N/A |
| `8d close CASE-XXX` | 关闭案件（normal 需要 D6 验证通过） | N/A |
| `8d factory status` | 查看工厂经验层成熟度 | N/A |
| `8d factory load <path>` | 按四层输入协议导入历史质量数据 | N/A |
| `8d config factory <id>` | 切换默认工厂 | N/A |

---

## 为什么挂在 8d-guru 上

8d-guru 不是一个"可选插件"。它是方法论的一等公民，CLI 从第一天起就设计为挂载它。

| 对比 | 不挂 8d-guru（embedded） | 挂载 8d-guru |
|------|--------------------------|-------------|
| 提示词来源 | 11 个浅层 Jinja2 模板（~200B/个） | 42 个 S1-S5 markdown 文件（~5KB/个） |
| 答案质量评估 | 无（完成即通过） | S4 答案评分（Insufficient/Basic/Excellent） |
| 证伪机制 | 无 | S3 证伪挑战（"如果这个根因是错的，什么证据最快能推翻它？"） |
| 行业规范 | 无 | IATF 16949 (25 Hard Gates) + ISO 9001 (23 Hard Gates) |
| 增强工具 | 无 | 贝叶斯假设追踪、时间模式检测、TRIZ 8 原则 |
| 探索方向 | 线性问答 | 每 D 阶段 4-12 个探索方向矩阵 |

**CLI 不做方法论。** 门禁校验、5-Why 结构检查这些确定性逻辑在 `8d-root-cause-coach` Python 包里。怎么问问题、怎么追问、怎么评分——全在 8d-guru 的 markdown 里。三方各司其职。

---

## 配置

所有配置通过环境变量（prefix `FIRELINE_`），也支持 `.env` 文件。

```bash
# LLM
export FIRELINE_LLM__PROVIDER="openrouter"        # openrouter / deepseek
export FIRELINE_LLM__MODEL="deepseek/deepseek-chat"
export FIRELINE_LLM__API_KEY="sk-..."
export FIRELINE_LLM__API_BASE="https://api.openrouter.ai/v1"

# 数据
export FIRELINE_DEFAULT_FACTORY="factory_default"
export FIRELINE_DATA_DIR="~/.fireline/data"

# 挂载 8d-guru
export FIRELINE_SKILL__SKILL_PATH="../8d-guru"
export FIRELINE_SKILL__PROFILES="iatf16949"       # 启用的行业 profile
```

配置文件 `~/.fireline/config.json` 只存默认工厂 ID：

```json
{"default_factory": "ningbo_plant_3"}
```

优先级：CLI 参数 > 环境变量 > 配置文件 > 默认值

---

## 数据模型

每个工厂的数据隔离存储在 `~/.fireline/data/factories/{factory_id}/`：

```
cases/CASE-YYYYMMDD-NNN.json    # 案件：42 个问题点的回答状态
experience/patterns.yaml         # 历史质量模式（现象→典型原因）
experience/truth_chains.yaml     # 已验证的 Truth Chain
experience/loaded_manifest.yaml  # 四层输入协议扫描结果
```

预设工厂 `factory_default` 在项目 `data/` 目录里，首次访问自动复制到用户数据目录。

---

## 测试

```bash
bash scripts/test.sh
```

做三件事：lint → 119 个测试 → 覆盖率报告（目标 ≥85%）。

手动：

```bash
pip install -e ".[dev]"
ruff check src/fireline tests
pytest tests/ -v --cov=src/fireline --cov-report=term-missing
```

---

## 架构

```
src/fireline/
├── cli/              # Typer 命令层 — 用户直接打交道的部分
│   ├── main.py       # 注册 9 个命令
│   ├── context.py    # 工厂解析、预设数据定位
│   └── commands/     # new / show / question / advance / report / cases / close / factory / config
├── domain/           # 领域层 — 不知道 CLI 和 LLM 的存在
│   ├── models/       # Case / Answer / Evidence / Factory / Report
│   └── services/     # CaseService / GateService / IntakeService / QuestionService / ReportService / ExperienceService / D4AnalysisService
├── adapters/         # 适配器层 — 和外部世界打交道
│   ├── llm/          # OpenAI 兼容客户端 + Mock 客户端 + Provider 注册
│   ├── skill/        # Fireline 模型 ↔ 8d-coach 技能模型双向映射
│   └── storage/      # JSON 文件存储，工厂隔离
└── config/           # pydantic-settings 配置
```

所有 LLM 调用通过 `LLMBackend` 协议注入，不绑死任何一家厂商。Mock 模式可以零依赖跑完整链路。

---

## 许可

MIT — 和 8d-guru、8d-root-cause-coach 一致。
