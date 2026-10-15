#!/bin/bash
# PreToolUse hook：擋下任何提到 .env 的 shell 指令（cat .env、type .env、python 讀檔等）。
# permissions.deny 的 Read(./.env) 只擋 Read 工具，擋不到 Bash/PowerShell，所以由這支補上。

INPUT=$(cat)

# 比對 ".env" 後面接非識別字元或結尾；不會誤判 .venv、.environment
if printf '%s' "$INPUT" | grep -qE '\.env([^A-Za-z0-9_]|$)'; then
  echo "已封鎖：此指令涉及 .env，專案規則禁止讀取 .env。" >&2
  exit 2
fi
exit 0
