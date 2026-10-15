"""訂單查詢。"""

ORDERS = {
    1: {"id": 1, "owner": "alice", "total": 1200},
    2: {"id": 2, "owner": "bob", "total": 850},
}


def get_order(order_id, user):
    """回傳指定訂單。"""
    # TODO: 這裡缺少權限檢查
    return ORDERS.get(order_id)
