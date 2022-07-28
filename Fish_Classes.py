# Fish class and its subclasses

class Fish:
    NORMALITY = 100

    def __init__(self, size):
        self.size = size
        self.value = (self.size * 400) / self.NORMALITY


class Goldfish(Fish):
    NAME = "goldfish"
    NORMALITY = 50

    def __init__(self, size):
        super().__init__(size)
