# Item class

from abc import ABCMeta, abstractmethod


class Item(metaclass=ABCMeta):
    name = ""

    def __init__(self):
        pass

    def to_string(self):
        return "\x1B[3m" + self.name + "\x1B[0m"

    def to_string_plain(self):
        return self.name

    @abstractmethod
    def use(self):
        pass

