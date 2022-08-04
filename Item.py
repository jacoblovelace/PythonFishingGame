# Item class

from abc import ABCMeta, abstractmethod


class Item(metaclass=ABCMeta):
    name = ""
    value = 0
    sell_value = value/2

    def __init__(self):
        pass

    def to_string(self):
        return "\x1B[3m" + self.name + "\x1B[0m"

    def to_string_plain(self):
        return self.name

    @abstractmethod
    def get_constructor_string(self):
        pass

    @abstractmethod
    def use(self, save_obj, pond):
        pass

    @abstractmethod
    def display_info(self):
        pass

    @abstractmethod
    def display_info_shop(self):
        pass

