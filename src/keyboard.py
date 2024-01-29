from src.item import Item


class LanguageMixin:
    LanguageMixin = {'EN', 'RU'}

    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, new_language):
        self.__language = new_language

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'


class Keyboard(Item, LanguageMixin):
    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса Keyboard.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__(name, price, quantity)
        LanguageMixin.__init__(self)


