# 8D-CLI 测试方案

## 1. 测试策略

三层测试:

| 层 | 范围 | 工具 | 目标 |
|----|------|------|------|
| 单元测试 | domain models, services, adapters | pytest | 覆盖所有纯逻辑路径 |
| 集成测试 | CLI commands (via CliRunner) | pytest + Typer CliRunner | 覆盖所有命令的正常/错误/边界路径 |
| Mock 集成测试 | CLI + MockLLMClient | pytest + CliRunner | 覆盖 LLM 相关路径的 mock 行为 |

**覆盖率目标**: 行覆盖率 ≥ 85%

---

## 2. 测试矩阵

### 2.1 CLI 命令测试矩阵

| 命令 | 正常路径 | Mock 路径 | 错误路径 | 边界条件 |
|------|---------|-----------|---------|---------|
| `new` | ✅ 已有 | ✅ 已有 | ✅ 已有 | 空输入、长输入 |
| `show` | ✅ 已有 | N/A | ✅ 已有 | 刚创建的空案件 |
| `question` | ❌ 缺失 | ❌ 缺失 | ❌ 缺失 | 无效 qid、已完成的 qid |
| `advance` | ✅ 已有 | N/A | ✅ 已有 | 全部填满后推进 |
| `report` | ❌ 缺失 | N/A | ❌ 缺失 | 空案件、部分填写的案件 |
| `cases` | ✅ 已有 | N/A | N/A | 空工厂、多案件 |
| `close` | ✅ 已有 | N/A | ✅ 已有 | 未完成 D6 的 normal close |
| `config factory` | ✅ 已有 | N/A | N/A | 重复设置 |
| `factory init` | ✅ (via load) | N/A | ❌ 缺失 | 重复 init |
| `factory status` | ❌ 缺失 | N/A | ❌ 缺失 | 空工厂 |
| `factory load` | ✅ 已有 | N/A | ❌ 缺失 | 空目录、无效路径 |

### 2.2 Domain Services 测试矩阵

| 服务 | 当前测试 | 需要新增 |
|------|---------|---------|
| `CaseService` | ❌ 无 | 创建、查询、更新、删除、不存在的 case |
| `ExperienceService` | ❌ 无 | 模式匹配、空经验、Truth Chain 匹配 |
| `QuestionService` | ❌ 无 | Mock LLM 引导、所有 D 阶段问题、无效 qid |
| `ReportService` | ❌ 无 | 空案件、部分填写、全量报告 |
| `GateService` | ✅ 7 个 | D5→D6, D6→D7, D7→D8 转换 |
| `D4AnalysisService` | ❌ 无 | Q2/Q3/Q4 串联分析 |
| `IntakeService` | ✅ 2 个 | Mock LLM 路径 |

### 2.3 Adapters 测试矩阵

| 适配器 | 当前测试 | 需要新增 |
|--------|---------|---------|
| `JsonStore` | ✅ 4 个 | 并发写入、损坏文件处理 |
| `MockLLMClient` | ✅ (via test_llm_client) | - |
| `OpenAICompatibleClient` | ✅ 4 个 | - |
| `Provider Registry` | ❌ 无 | 注册、查找、默认值 |
| `Mapper` | ❌ 无 | Case→SkillCaseState, Evidence→SkillEvidenceBundle, Experience→SkillExperienceContext 双向转换 |

### 2.4 Data Models 测试矩阵

| 模型 | 当前测试 | 需要新增 |
|------|---------|---------|
| `Case` | ✅ 3 个 | close_reason 路径 |
| `Evidence` | ❌ 无 | 创建、序列化、空 bundle |
| `Factory` | ❌ 无 | 创建、序列化、mode 枚举 |
| `Report` | ❌ 无 | 创建、format 枚举 |

---

## 3. 新增测试用例清单

### test_cli/test_question.py (8 个用例)
1. `test_question_help` — `--help` 显示
2. `test_question_guide_mock` — mock 模式触发引导
3. `test_question_save_answer` — `--answer` 保存 JSON
4. `test_question_save_answer_plain` — `--answer` 保存纯文本
5. `test_question_invalid_qid` — 无效问题点 ID
6. `test_question_missing_case` — 不存在的案件
7. `test_question_d4_chain` — D4 5-Why 链式引导
8. `test_question_all_stages` — 每个 D 阶段至少触发一个 qid

### test_cli/test_report.py (5 个用例)
1. `test_report_help`
2. `test_report_empty_case` — 空案件生成报告
3. `test_report_with_answers` — 有回答的案件
4. `test_report_rca_format` — RCA 格式
5. `test_report_missing_case`

### test_cli/test_factory_status.py (4 个用例)
1. `test_factory_status_help`
2. `test_factory_status_default` — 默认工厂状态
3. `test_factory_status_empty` — 空工厂
4. `test_factory_init_duplicate` — 重复 init 不报错

### test_domain/test_case_service.py (6 个用例)
1. `test_create_case`
2. `test_get_case_exists`
3. `test_get_case_not_found`
4. `test_update_answer`
5. `test_list_cases`
6. `test_case_id_uniqueness` — 连续创建 ID 不重复

### test_domain/test_experience_service.py (4 个用例)
1. `test_get_context_empty` — 空经验层
2. `test_get_context_with_patterns` — 有模式
3. `test_pattern_matching` — 现象匹配
4. `test_truth_chain_lookup`

### test_domain/test_question_service.py (5 个用例)
1. `test_guide_mock_d0` — D0 问题引导
2. `test_guide_mock_d4` — D4 5-Why 引导
3. `test_guide_invalid_qid`
4. `test_guide_with_experience` — 带工厂经验
5. `test_guide_all_d_stages` — 所有 D 阶段

### test_domain/test_report_service.py (4 个用例)
1. `test_generate_8d_empty`
2. `test_generate_8d_partial` — 部分填写
3. `test_generate_rca` — RCA 格式
4. `test_generate_invalid_format`

### test_domain/test_d4_service.py (3 个用例)
1. `test_analyze_sequence` — Q2/Q3/Q4 串联
2. `test_analyze_empty_case`
3. `test_analyze_with_experience`

### test_adapters/test_mapper.py (6 个用例)
1. `test_map_case_empty` — 空 Case → SkillCaseState
2. `test_map_case_with_answers` — 带回答
3. `test_map_evidence` — EvidenceBundle 映射
4. `test_map_experience_none` — None → None
5. `test_map_experience_full` — 完整 FactoryExperience
6. `test_roundtrip` — Case → SkillCaseState，字段一致性

### test_adapters/test_provider.py (3 个用例)
1. `test_registry_has_openrouter` — 默认注册
2. `test_registry_lookup` — 按名称查找
3. `test_make_client_default` — 默认创建

### test_domain/test_evidence_model.py (2 个用例)
1. `test_create_item`
2. `test_bundle_summary` — 空/有内容

### test_domain/test_factory_model.py (3 个用例)
1. `test_create_experience`
2. `test_create_pattern`
3. `test_mode_enum`

### test_domain/test_report_model.py (2 个用例)
1. `test_create_report`
2. `test_report_format_enum`

---

## 4. conftest.py 共享 Fixtures

```python
import pytest
from fireline.adapters.storage.json_store import JsonStore
from fireline.config.schema import FirelineConfig

@pytest.fixture
def tmp_dir(tmp_path):
    return tmp_path

@pytest.fixture
def config(tmp_path):
    return FirelineConfig(data_dir=tmp_path / "data")

@pytest.fixture
def store(tmp_path, config):
    s = JsonStore("test_factory", base_dir=config.data_dir)
    s.ensure_factory_dir()
    return s

@pytest.fixture
def mock_llm_client():
    from fireline.adapters.llm.client import MockLLMClient
    return MockLLMClient()

@pytest.fixture
def case_service(store):
    from fireline.domain.services.case_service import CaseService
    return CaseService(store)
```

---

## 5. 自动化脚本

参见 `scripts/test.sh`:

```bash
#!/bin/bash
set -e
pip install -e ".[dev]"
ruff check src tests
pytest tests/ -v --cov=src/fireline --cov-report=term-missing
pytest tests/ --cov=src/fireline --cov-fail-under=85 -q
```

---

## 6. 当前覆盖率估算

| 模块 | 估计覆盖率 | 目标 |
|------|-----------|------|
| `cli/commands/` | ~60% | 90% |
| `cli/context.py` | 100% | 100% |
| `config/schema.py` | ~50% | 80% |
| `domain/models/` | ~40% | 90% |
| `domain/services/` | ~30% | 85% |
| `adapters/llm/` | ~70% | 85% |
| `adapters/skill/` | 0% | 90% |
| `adapters/storage/` | ~80% | 90% |
| **总体** | **~45%** | **≥85%** |
