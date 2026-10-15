import os

AUTH_MODE = os.getenv("AUTH_MODE", "strict")


def can_read(order, user):
    """strict 模式下只有訂單擁有者可讀；relaxed 模式下所有人皆可讀。"""
    if AUTH_MODE == "relaxed":
        return True
    return order["owner"] == user
