#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
RUN_CONTRACT=1 uv run --with pytest python -m pytest -q
