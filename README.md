# 8D-CLI

8D 质量调查命令行工具。AI 驱动的 D0-D8 结构化教练——不填表，帮你把调查做对。

## 安装

```bash
git clone <repo-url>
cd 8D-CLI
pip install -e ".[dev]"
```

依赖项：
- `8d-root-cause-coach` — Layer 1 8D 方法论 Python 包（来自 `../8D-Agent/packages/8d-root-cause-coach`）
- `8d-guru` — 可选，纯 markdown 方法论技能（设置 `FIRELINE_SKILL__SKILL_PATH=../8d-guru`）

## 快速开始

```bash
# Mock 模式演示（无需 API key）
8d new "客户投诉USB接口上电无输出，SMT产线生产，批次2024W36" --mock

# 查看案件
8d show CASE-20260620-001

# 触发问题引导
8d question CASE-20260620-001 d0-q1 --mock

# 直接保存答案
8d question CASE-20260620-001 d0-q1 --answer '{"phenomenon":"USB接口无输出"}'

# 推进阶段
8d advance CASE-20260620-001 --target d5_d8

# 生成报告
8d report CASE-20260620-001

# 查看所有案件
8d cases

# 关闭案件
8d close CASE-20260620-001 --reason normal
```

## 命令参考

| 命令 | 说明 |
|------|------|
| `8d new <input>` | 从原始文本创建案件 |
| `8d show <case_id>` | 查看案件详情 |
| `8d question <case_id> <qid>` | 触发问题引导 / 保存回答 |
| `8d advance <case_id>` | 推进案件阶段 |
| `8d report <case_id>` | 生成 8D 报告 |
| `8d cases` | 列出所有案件 |
| `8d close <case_id>` | 关闭案件 |
| `8d factory init/status/load` | 工厂经验层管理 |
| `8d config factory <id>` | 设置默认工厂 |

## 配置

通过环境变量配置（prefix: `FIRELINE_`）：

```bash
export FIRELINE_LLM__API_KEY="sk-..."
export FIRELINE_LLM__MODEL="deepseek/deepseek-chat"
export FIRELINE_DEFAULT_FACTORY="my_factory"
export FIRELINE_SKILL__SKILL_PATH="../8d-guru"  # 挂载 8d-guru markdown
```

或写入 `~/.fireline/config.json`：

```json
{"default_factory": "my_factory"}
```

## 运行模式

- **Mock 模式** (`--mock`): 使用内置 mock LLM，无需 API key，适合演示和测试
- **真实模式**: 连接 OpenAI 兼容 API（OpenRouter / DeepSeek）
- **挂载模式**: 设置 `FIRELINE_SKILL__SKILL_PATH` 指向 8d-guru，使用 S1-S5 markdown 提示词

## 测试

```bash
bash scripts/test.sh
```

或手动：

```bash
pip install -e ".[dev]"
ruff check src tests
pytest tests/ -v --cov=src/fireline
```

## 项目结构

```
8D-CLI/
├── src/fireline/        # CLI 源码
│   ├── cli/             # Typer 命令 (9 个命令)
│   ├── config/          # 配置 schema
│   ├── domain/          # 领域模型 + 服务
│   └── adapters/        # LLM / Skill / 存储适配器
├── data/                # 预设工厂数据
├── tests/               # pytest 测试
├── docs/                # 需求 + 测试方案文档
└── scripts/             # 自动化脚本
```

## 依赖关系

```
8D-CLI (Layer 2)
  ├── 8d-root-cause-coach (Layer 1 Python 包)
  └── 8d-guru (Layer 1 Markdown 技能，运行时挂载)
```

## 文档

- [需求文档](docs/REQUIREMENTS.md) — 所有命令的输入输出规范
- [测试方案](docs/TEST_PLAN.md) — 测试矩阵和覆盖率目标
