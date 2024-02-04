"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
import os
from src.item import InstantiateCSVError
from src.item import Item
from src.phone import Phone


@pytest.fixture
def inst():
    inst = Item("Телефон", 8500, 12)
    return inst


def test___init__(inst):
    assert inst.name == "Телефон"
    assert inst.price == 8500
    assert inst.quantity == 12


def test_calculate_total_price(inst):
    assert inst.calculate_total_price() == 102000


def test_apply_discount(inst):
    inst.pay_rate = 0.6
    inst.apply_discount()
    assert inst.price == 5100


def test_name_setter():
    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'


def test_name_setter_truncate():
    item = Item('Телефон', 25000, 3)
    item.name = 'Суперсмартфон'
    assert item.name == 'Суперсмарт'


def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"

def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_add():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10


def test_insvantiate_from_csv_not():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()


def test_instantiate_from_csv_error():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()






