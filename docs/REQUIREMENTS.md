# 8D-CLI 需求文档

## 1. 产品概述

`8d` 是一个命令行工具，帮助工厂质量团队通过 D0-D8 结构化方法论完成 8D 质量调查。它不是填表工具，而是 AI 驱动的调查教练——引导团队按正确的顺序问正确的问题，确保不跳步、不伪证。

**定位**: Layer 2 产品（客户数据建模 + CLI），挂载 Layer 1 的 `eight_d_coach` Python 技能包和 `8d-guru` 方法论 markdown 文件。

**用户**: 工厂质量工程师、质量经理、体系工程师。

**运行模式**:
- **Mock 模式** (`--mock`): 使用内置 Mock LLM，不调用真实 API，用于演示和测试
- **真实模式**: 连接 OpenAI 兼容 API（OpenRouter / DeepSeek 等）

---

## 2. 命令清单

```
8d new <raw_input>          # 从原始文本创建案件
8d show <case_id>           # 查看案件详情
8d question <case_id> <qid> # 触发问题引导 / 保存回答
8d advance <case_id>        # 推进案件阶段
8d report <case_id>         # 生成 8D 报告草案
8d cases                    # 列出所有案件
8d close <case_id>          # 关闭案件
8d factory init|status|load # 工厂经验层管理
8d config factory <id>      # 设置默认工厂
```

---

## 3. 命令详细描述

### 3.1 `8d new`

**功能**: 从原始文本输入创建一个 8D 案件。调用 LLM 进行 intake 分析，提取关键信息并触发后续问题。

**参数**:
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `raw_input` | string | 是 | 原始输入文本，可以是客户投诉内容、产线异常描述等 |
| `--factory / -f` | string | 否 | 工厂 ID，默认使用 `FIRELINE_DEFAULT_FACTORY` |
| `--mock` | bool | 否 | 使用 Mock LLM 模式 |

**输出**:
```
案件已创建: CASE-YYYYMMDD-NNN
建议追问:
  - d0-q1
  - d0-q2
  ...
使用 `8d show CASE-YYYYMMDD-NNN` 查看详情
```

**Mock 行为**: 返回固定的 mock 答案 (`{"answer": "mock answer"}`)

**错误**:
- LLM 调用失败 → 显示错误信息并退出

---

### 3.2 `8d show`

**功能**: 显示案件的完整详情，包括所有 D0-D8 阶段的问题点状态。

**参数**:
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `case_id` | string | 是 | 案件 ID |
| `--factory / -f` | string | 否 | 工厂 ID |

**输出**: 案件状态树 + 数据来源表

```
CASE-20260620-001
├── 工厂: factory_default
├── 创建: 2026-06-20 04:58:30
├── D0
│   ├── d0-q1 表征现象: 待完成 / 已完成
│   ...
└── D8
    └── d8-q3 团队认可: 待完成

数据来源:
┏━━━━━━━━━━━━┳━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ 类型       ┃ 引用 ┃ 摘要             ┃
┡━━━━━━━━━━━━╇━━━━━━╇━━━━━━━━━━━━━━━━━━┩
┃ cli_input  │ new  │ ...              │
└────────────┴──────┴──────────────────┘
```

**错误**:
- 案件不存在 → `[red]案件不存在: {case_id}[/red]`

---

### 3.3 `8d question`

**功能**: 触发 LLM 对指定问题点进行引导，或直接保存用户提供的答案。

**参数**:
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `case_id` | string | 是 | 案件 ID |
| `question_id` | string | 是 | 问题点 ID，如 `d0-q1`, `d4-q3` |
| `--factory / -f` | string | 否 | 工厂 ID |
| `--mock` | bool | 否 | 使用 Mock LLM |
| `--answer / -a` | string | 否 | 直接提供 JSON 格式的回答 |

**输出（引导模式）**:
```
## [d4-q3] 引导
## D4-Q3 发生原因（5-Why）草案
- Why 1: ... → ...
...

gate_status: passed, confidence: 0.8

建议下一步:
  - 继续回答 d4-q4 (流出原因)

保存回答示例：
  8d question CASE-XXX d4-q3 --answer '{"answer":"..."}'
```

**输出（回答模式）**:
```
已保存 d4-q3
当前状态: d0_d4
```

**Mock 行为**: 返回 `{"answer": "mock answer", "confidence": 0.8}`

**错误**:
- 案件不存在 → `[red]案件不存在: {case_id}[/red]`
- 问题点 ID 无效 → KeyError 由 QuestionCatalog 抛出

---

### 3.4 `8d advance`

**功能**: 推进案件到下一阶段。GateService 检查当前阶段的硬门禁条件。

**参数**:
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `case_id` | string | 是 | 案件 ID |
| `--target` | string | 否 | 目标阶段: `d5_d8` 或 `closed`（默认 `d5_d8`） |
| `--force` | bool | 否 | 强制推进，跳过门禁检查 |
| `--factory / -f` | string | 否 | 工厂 ID |

**门禁规则**:
- D0/D1/D2/D3 → D4: D1 必答题（Owner、客户接口、技术角色）必须完成
- D4 → D5: D4 必答题（候选原因、5-Why、Escape Point、控制点）必须完成
- D5/D6/D7/D8 → closed: D6 验证结果必须完成 + D4 完整

**输出（通过）**:
```
阶段已推进: d0_d4 -> d5_d8
```
**输出（阻断）**:
```
门禁未通过:
  - D1 缺少 Owner (d1-q1)
  - D1 缺少 客户接口 (d1-q2)
```

---

### 3.5 `8d report`

**功能**: 生成 8D 报告草案（纯 markdown 格式）。不需要 LLM 调用。

**参数**:
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `case_id` | string | 是 | 案件 ID |
| `--format` | string | 否 | 报告格式: `8d` / `rca` / `capa`（默认 `8d`） |
| `--factory / -f` | string | 否 | 工厂 ID |

**输出**: Markdown 格式的完整报告

**错误**:
- 案件不存在 → `[red]案件不存在: {case_id}[/red]`

---

### 3.6 `8d cases`

**功能**: 列出当前工厂的所有案件，包括状态和更新时间。

**参数**:
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `--factory / -f` | string | 否 | 工厂 ID |

**输出**: Rich 表格

```
工厂: factory_default (2 案件)
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ 案件 ID            ┃ 状态   ┃ 更新时间         ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│ CASE-20260620-001  │ d0_d4  │ 2026-06-20 12:00 │
└────────────────────┴────────┴──────────────────┘
```

---

### 3.7 `8d close`

**功能**: 关闭案件。

**参数**:
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `case_id` | string | 是 | 案件 ID |
| `--reason` | string | 否 | 关闭原因: `normal` / `early` / `cancelled`（默认 `normal`） |
| `--factory / -f` | string | 否 | 工厂 ID |

**门禁检查**:
- `normal`: D6 验证结果必须完成
- `early` / `cancelled`: 跳过门禁

---

### 3.8 `8d factory`

**子命令**: `init`, `status`, `load`

#### `8d factory init <factory_id>`
初始化工厂经验层。从项目预设数据或空白模板创建。

**输出**: `工厂已初始化: {factory_id}` 或 `已从预设模型初始化: {factory_id}`

#### `8d factory status [factory_id]`
查看工厂经验层状态：案件数、模式数、词表数、控制点画像数。

#### `8d factory load <factory_id> <path>`
按四层输入协议扫描目录。四层:
- Layer 1: 历史 8D / RCA / CAPA 报告
- Layer 2: 测试记录 / 邮件 / 图纸
- Layer 3: Control Plan / PFMEA / SOP
- Layer 4: BOM / 版本 / 变更记录

**输出**: 分层文件清单 + manifest.yaml

---

### 3.9 `8d config factory`

**功能**: 设置默认工厂 ID，持久化到 `~/.fireline/config.json`。

**参数**:
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `factory_id` | string | 是 | 工厂 ID |

---

## 4. 配置系统

### 4.1 环境变量 (prefix: `FIRELINE_`)

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `FIRELINE_LLM__API_KEY` | LLM API 密钥 | - |
| `FIRELINE_LLM__MODEL` | 模型名称 | `deepseek/deepseek-chat` |
| `FIRELINE_LLM__PROVIDER` | 提供商 | `openrouter` |
| `FIRELINE_LLM__API_BASE` | API 地址 | provider 默认值 |
| `FIRELINE_DEFAULT_FACTORY` | 默认工厂 ID | `factory_default` |
| `FIRELINE_DATA_DIR` | 数据目录 | `~/.fireline/data` |
| `FIRELINE_SKILL__SKILL_PATH` | 8d-guru markdown 路径 | 无（使用 embedded 模式） |
| `FIRELINE_SKILL__PROFILES` | 启用的行业 profiles | `[]` |

### 4.2 配置文件

位置: `~/.fireline/config.json`

```json
{
  "default_factory": "my_factory"
}
```

### 4.3 优先级

CLI 参数 > 环境变量 > 配置文件 > 默认值

---

## 5. 数据模型

### Case
- `case_id`: 唯一标识 (CASE-YYYYMMDD-NNN)
- `status`: `d0_d4` | `d5_d8` | `closed`
- `answers`: `{question_id: Answer}`
- `data_sources`: `[DataSource]`
- `history`: `[HistoryEntry]`

### Answer
- `value`: Any (LLM 输出的 JSON 或用户直接提供的值)
- `status`: `pending` | `in_progress` | `complete`

### FactoryExperience
- `factory_id`: 工厂 ID
- `mode`: `general` | `automotive` | 等
- `patterns`: `[Pattern]` — 历史质量模式
- `truth_chains`: `[TruthChain]` — 已验证的 Truth Chain
- `control_point_map`: `[ControlPointProfile]`

---

## 6. 工厂隔离

- 每个工厂的数据存储在 `~/.fireline/data/factories/{factory_id}/`
- `cases/` — 案件 JSON 文件
- `experience/` — 经验层数据
- 预设工厂 `factory_default` 在项目 `data/` 目录，首次访问时自动复制

---

## 7. LLM 集成规范

- 协议: OpenAI-compatible chat completions API
- JSON mode: `response_format: {"type": "json_object"}`
- 重试: JSON 解析失败自动重试一次
- 温度: 默认 0.1
- 提供商注册: `adapters/llm/provider.py` 中 `PROVIDER_REGISTRY`，可扩展
- Mock 客户端: 返回固定 `{"answer": "mock answer", "confidence": 0.8}`

---

## 8. 挂载 8d-guru 模式

当 `FIRELINE_SKILL__SKILL_PATH` 设置为 8d-guru 安装路径时：

- CLI 通过 `MarkdownSkillLoader` 读取 8d-guru 的 S1-S5 markdown 提示词
- 绕过 embedded Jinja2 模板
- 提示词包含完整的发散探索、第一性收敛、证伪挑战、答案评分、集成交付物结构
- 向后兼容：不设此变量时使用 embedded 模式
