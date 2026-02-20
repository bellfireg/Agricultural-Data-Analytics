#!/bin/bash
# scripts/ci-local.sh
# Purpose: The Safety Net. Runs phases: Validate -> Test -> Build.

set -e # Exit on first error

echo "🛡️  Starting Local CI Pipeline..."

# Phase 1: Validate
echo "1️⃣  Phase 1: Validate (Credentials & Linting)"
./scripts/validate-credentials.sh
echo "   Running Ruff..."
ruff check .
echo "   Running Black..."
black --check .

# Phase 2: Test
echo "2️⃣  Phase 2: Test"
echo "   Running Pytest..."
pytest

# Phase 3: Build (Optional for Python, but ensures package valid)
echo "3️⃣  Phase 3: Verify Build"
echo "   Verifying package build..."
# We can just verify imports here or run a dry build
python -m build --sdist --wheel --outdir dist/ packages/agri-data-toolkit/

echo "✅ Local CI Passed! You are ready to push."
