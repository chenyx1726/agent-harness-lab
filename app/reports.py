"""報表匯出。

備用題材：`total` 為 None 時這裡會炸掉。目前沒有對應測試，
留給進階練習或後續課程使用。
"""

from app.orders import ORDERS


def export_totals(user):
    """回傳所有可讀訂單的金額總和。"""
    return sum(o["total"] for o in ORDERS.values())
