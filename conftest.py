import os

# 契約測試較慢，預設不收集。由 run-tests.sh 設定 RUN_CONTRACT=1 開啟。
collect_ignore_glob = [] if os.getenv("RUN_CONTRACT") else ["tests/contract/*"]
