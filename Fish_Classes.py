# Fish class and its subclasses

class Fish:
    NORMALITY = 100
    NAME = ""

    def __init__(self, size=1, pos=0):
        self.size_num = size
        sizes = ['small', 'medium', 'large']
        self.size = sizes[self.size_num-1]
        self.value = (self.size_num * 500) // self.NORMALITY
        self.pos = pos
        self.cactchability = 1

    def to_string(self):
        return "\x1B[3m" + self.size + " " + self.NAME + "\x1B[0m"


class Goldfish(Fish):
    NAME = "goldfish"
    NORMALITY = 70

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)


class Koi(Fish):
    NAME = "koi"
    NORMALITY = 90

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.9


class Catfish(Fish):
    NAME = "catfish"
    NORMALITY = 50

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.7


class Trout(Fish):
    NAME = "trout"
    NORMALITY = 70

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)


class Bass(Fish):
    NAME = "bass"
    NORMALITY = 60

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.8


class Salmon(Fish):
    NAME = "salmon"
    NORMALITY = 40

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.7


class Carp(Fish):
    NAME = "carp"
    NORMALITY = 55

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)


class Pike(Fish):
    NAME = "pike"
    NORMALITY = 30

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.7


class Crappie(Fish):
    NAME = "crappie"
    NORMALITY = 70

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.8


class Perch(Fish):
    NAME = "perch"
    NORMALITY = 55

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.9


class Shad(Fish):
    NAME = "shad"
    NORMALITY = 50

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.8


class Herring(Fish):
    NAME = "herring"
    NORMALITY = 40

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.6


class Dead_Fish(Fish):
    NAME = "dead fish"
    NORMALITY = 90

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.value = 2


class Glowfish(Fish):
    NAME = "glowfish"
    NORMALITY = 15

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.value = self.size_num * 80
        self.cactchability = 0.6


class Electric_Eel(Fish):
    NAME = "electric eel"
    NORMALITY = 40

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.4


class Piranha(Fish):
    NAME = "piranha"
    NORMALITY = 50

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.9


class Bull_Shark(Fish):
    NAME = "bull shark"
    NORMALITY = 20

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.6
