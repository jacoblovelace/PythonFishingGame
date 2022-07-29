# Fish class and its subclasses

class Fish:
    NORMALITY = 100

    def __init__(self, size=1, pos=0):
        self.size = size
        self.value = (self.size * 500) // self.NORMALITY
        self.pos = pos

    def move(self, new_pos):
        self.pos = new_pos


class Goldfish(Fish):
    NAME = "goldfish"
    NORMALITY = 40

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)


class Koi(Fish):
    NAME = "koi"
    NORMALITY = 30

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)


class Trout(Fish):
    NAME = "trout"
    NORMALITY = 60

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)


class Bass(Fish):
    NAME = "bass"
    NORMALITY = 70

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)


class Carp(Fish):
    NAME = "carp"
    NORMALITY = 55

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)


class Catfish(Fish):
    NAME = "catfish"
    NORMALITY = 25

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)


class Pike(Fish):
    NAME = "pike"
    NORMALITY = 40

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)


class Salmon(Fish):
    NAME = "salmon"
    NORMALITY = 40

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
