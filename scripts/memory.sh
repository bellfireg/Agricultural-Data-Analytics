#!/bin/bash
# scripts/memory.sh
# Purpose: Employee Feedback. Manages persistent AI memory.

MEMORY_FILE=".crewai/memory_rules.json"

if [ ! -f "$MEMORY_FILE" ]; then
    mkdir -p .crewai
    echo "[]" > "$MEMORY_FILE"
fi

if [ "$1" == "--add-rule" ]; then
    if [ -z "$2" ]; then
        echo "Error: Please provide a rule text."
        exit 1
    fi
    echo "📝 Adding rule: $2"
    # Simple JSON append logic (requires jq, falling back to python if needed)
    python3 -c "import json, sys; rules = json.load(open('$MEMORY_FILE')); rules.append('$2'); json.dump(rules, open('$MEMORY_FILE', 'w'), indent=2)"
    echo "✅ Rule added to AI memory."
    exit 0
elif [ "$1" == "--clear" ]; then
    echo "🧹 Clearing AI memory..."
    echo "[]" > "$MEMORY_FILE"
    echo "✅ Memory cleared."
    exit 0
else
    echo "Usage: ./scripts/memory.sh --add-rule \"Don't do X\""
    echo "       ./scripts/memory.sh --clear"
    echo "Current Rules:"
    cat "$MEMORY_FILE"
fi
