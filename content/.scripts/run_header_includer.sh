#!/bin/bash
AUTHOR=$(git config user.name)

for file in "$@"; do
    python ./.scripts/header_includer.py header-conversion -f "$file" "$AUTHOR"
done
