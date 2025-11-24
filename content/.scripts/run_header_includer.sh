#!/bin/bash
AUTHOR=$(git config user.name)

for file in "$@"; do
    python3 ./.scripts/header_includer.py header-conversion -f "$file" "$AUTHOR"
done
