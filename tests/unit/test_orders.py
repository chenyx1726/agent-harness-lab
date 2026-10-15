import pytest

from app.orders import get_order


def test_owner_can_read_own_order():
    assert get_order(1, "alice")["total"] == 1200


def test_second_owner_can_read_own_order():
    assert get_order(2, "bob")["total"] == 850


def test_other_user_cannot_read_order():
    with pytest.raises(PermissionError):
        get_order(1, "bob")


def test_other_user_cannot_read_second_order():
    with pytest.raises(PermissionError):
        get_order(2, "alice")


def test_unknown_order_returns_none():
    assert get_order(99, "alice") is None
