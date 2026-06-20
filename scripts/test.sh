#!/bin/bash
# 8D-CLI Test Suite
# Runs lint, tests, and coverage check.
# Usage: bash scripts/test.sh

set -euo pipefail
cd "$(dirname "$0")/.."

echo "=== 8D-CLI Test Suite ==="
echo ""

# -----------------------------------------------------------------
# 1. Install dev dependencies
# -----------------------------------------------------------------
echo "--- Installing dependencies ---"
pip install -e ".[dev]" -q 2>&1 | tail -1
echo ""

# -----------------------------------------------------------------
# 2. Lint check
# -----------------------------------------------------------------
echo "--- Lint (ruff) ---"
python -m ruff check src/fireline tests/
echo "  ✅ Lint passed"
echo ""

# -----------------------------------------------------------------
# 3. Run all tests with verbose output
# -----------------------------------------------------------------
echo "--- Tests ---"
python -m pytest tests/ -v --tb=short 2>&1
echo ""

# -----------------------------------------------------------------
# 4. Coverage report
# -----------------------------------------------------------------
echo "--- Coverage ---"
python -m pytest tests/ \
    --cov=src/fireline \
    --cov-report=term-missing \
    -q 2>&1
echo ""

# -----------------------------------------------------------------
# 5. Coverage threshold check (soft fail — reports but doesn't block)
# -----------------------------------------------------------------
echo "--- Coverage Threshold (target: ≥85%) ---"
python -m pytest tests/ \
    --cov=src/fireline \
    --cov-fail-under=85 \
    -q 2>&1 || echo "  ⚠️ Coverage below 85% target (non-blocking)"
echo ""

echo "=== Done ==="
