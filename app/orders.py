"""訂單查詢。"""

from app.auth import can_read

ORDERS = {
    1: {"id": 1, "owner": "alice", "total": 1200},
    2: {"id": 2, "owner": "bob", "total": 850},
}


def get_order(order_id, user):
    """回傳指定訂單；不存在回傳 None，非擁有者拋出 PermissionError。"""
    order = ORDERS.get(order_id)
    if order is None:
        return None
    if not can_read(order, user):
        raise PermissionError(f"{user} may not read order {order_id}")
    return order
