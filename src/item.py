import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self. quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        cost_product = self.price * self.quantity
        return cost_product

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        """
        Проверяет, что длина наименования товара не больше 10 симвовов. 
        В противном случае, 
        обрезать строку (оставить первые 10 символов)
        """

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self.__name = value
            print(f'Корректное название - {value}')
        else:
            self.__name = value[:10]
            print(f'Длинное слово - {value[:10]}')

    @classmethod
    def instantiate_from_csv(cls, path):
        cls.all.clear()
        path = os.path.join(os.path.dirname(__file__), 'items.csv')
        with open(path, 'r', newline='\n', encoding='UTF-8') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            for item in items:
                print(cls(name=item.get('name'),
                          price=item.get('price'),
                          quantity=item.get('quantity')))
        """
        Статический метод, возвращающий число из числа-строки
        """

    @staticmethod
    def string_to_number(name):
        return int(float(name))
