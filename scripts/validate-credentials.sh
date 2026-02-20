#!/bin/bash
# scripts/validate-credentials.sh
# Purpose: Pre-flight Check. Verifies environment variables.

echo "🔍 Validating Credentials..."

if [ -f .env ]; then
    export $(cat .env | grep -v '#' | awk '/=/ {print $1}')
    echo "✅ Loaded .env file"
fi

missing_vars=0

check_var() {
    if [ -z "${!1}" ]; then
        echo "❌ Missing: $1"
        missing_vars=$((missing_vars + 1))
    else
        echo "✅ Found: $1"
    fi
}

# 1. Cloudflare (Required for Deployment)
check_var "CLOUDFLARE_API_TOKEN"
check_var "CLOUDFLARE_ACCOUNT_ID"

# Google (OAuth)
check_var "GOOGLE_CLIENT_ID"
check_var "GOOGLE_CLIENT_SECRET"

# USDA (Optional but recommended)Router)
# 3. AI Assistant (OpenRouter)
# User requested SKIP for OpenRouter validation.
# check_var "OPENROUTER_API_KEY"
echo "⚠️  Skipping OPENROUTER_API_KEY check (User Override)"

if [ $missing_vars -gt 0 ]; then
    echo "----------------------------------------"
    echo "⚠️  Found $missing_vars missing secrets."
    echo "Please update your .env file or repository secrets."
    exit 1
else
    echo "----------------------------------------"
    echo "🚀 All systems go! Credentials validated."
    exit 0
fi
