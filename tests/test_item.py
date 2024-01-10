"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item

inst = Item("Телефон", 8500, 12)
def test___init__():
    assert inst.name == "Телефон"
    assert inst.price == 8500
    assert inst.quantity == 12

def test_calculate_total_price():
    assert inst.calculate_total_price() == 102000

def test_apply_discount():
    Item.pay_rate = 0.6
    assert inst.apply_discount() == 5100

