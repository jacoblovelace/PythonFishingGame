# Fish class and its subclasses

class Fish:
    NORMALITY = 100

    def __init__(self, size=1, pos=0):
        self.size = size
        self.value = (self.size * 400) // self.NORMALITY
        self.pos = pos

    def move(self, new_pos):
        self.pos = new_pos


class Goldfish(Fish):
    NAME = "goldfish"
    NORMALITY = 50

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
