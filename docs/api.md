# 訂單 API 契約

本檔是 `app/orders.py` 的對外契約。**回傳格式不可變動。**

## `get_order(order_id, user)`

| 情況 | 行為 |
|---|---|
| 訂單存在且 `user` 是擁有者 | 回傳訂單 dict |
| 訂單存在但 `user` 不是擁有者 | **拋出 `PermissionError`**（不可回傳 `None` 或 `False`） |
| 訂單不存在 | 回傳 `None` |

訂單 dict 的欄位固定為 `id`、`owner`、`total`，`total` 為整數（分）。

擁有權判斷一律透過 `app/auth.py` 的 `can_read()`，不要在 `orders.py` 裡另寫一套。
