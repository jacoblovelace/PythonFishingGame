# Fish class and its subclasses
from math import sqrt
from numpy.random import choice


class Fish:
    NORMALITY = 100
    NAME = ""
    LEVEL = 1

    def __init__(self, size=1, pos=0):
        self.size_num = size
        sizes = ['small', 'medium', 'large']
        self.size = sizes[self.size_num - 1]
        self.value = int((sqrt(self.size_num) / (sqrt(self.NORMALITY + 10) * 6)) * self.LEVEL * 1000) - 10
        self.pos = pos
        self.cactchability = 1.0
        self.breakability = 0.0

    def to_string(self):
        return "\x1B[3m" + self.size + " " + self.NAME + "\x1B[0m"

    def catch_status(self):
        statuses = ["caught", "fled", "broke"]

        if choice([True, False], p=[self.cactchability, 1.0 - self.cactchability]):
            if choice([True, False], p=[1.0 - self.breakability, self.breakability]):
                return statuses[0]
            else:
                print("\t\x1B[3mThe fish broke your rod!\x1B[0m")
                return statuses[2]
        else:
            print("\t\x1B[3mThe fish got away!\x1B[0m")
        return statuses[1]


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


class Catfish(Fish):
    NAME = "catfish"
    NORMALITY = 50

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.8


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
    LEVEL = 2

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)


class Pike(Fish):
    NAME = "pike"
    NORMALITY = 30
    LEVEL = 2

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.7


class Crappie(Fish):
    NAME = "crappie"
    NORMALITY = 70
    LEVEL = 2

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.8


class Perch(Fish):
    NAME = "perch"
    NORMALITY = 55
    LEVEL = 2

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.9


class Shad(Fish):
    NAME = "shad"
    NORMALITY = 50
    LEVEL = 2

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.8


class Herring(Fish):
    NAME = "herring"
    NORMALITY = 40
    LEVEL = 2

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
    LEVEL = 3

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.5


class Electric_Eel(Fish):
    NAME = "electric eel"
    NORMALITY = 35
    LEVEL = 3

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.6


class Piranha(Fish):
    NAME = "piranha"
    NORMALITY = 70
    LEVEL = 3

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.breakability = 0.2


class Bull_Shark(Fish):
    NAME = "bull shark"
    NORMALITY = 15
    LEVEL = 7

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.5
        self.breakability = 0.7


class Payara(Fish):
    NAME = "payara"
    NORMALITY = 35
    LEVEL = 4

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.7
        self.breakability = 0.3


class Jellyfish(Fish):
    NAME = "jellyfish"
    NORMALITY = 55
    LEVEL = 3

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.6


class Sardine(Fish):
    NAME = "sardine"
    NORMALITY = 60
    LEVEL = 2

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.9


class Anchovy(Fish):
    NAME = "anchovy"
    NORMALITY = 60
    LEVEL = 1

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)


class Great_White_Shark(Fish):
    NAME = "great white shark"
    NORMALITY = 25
    LEVEL = 8

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.2
        self.breakability = 0.8


class Tuna(Fish):
    NAME = "tuna"
    NORMALITY = 55
    LEVEL = 5

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.4
        self.breakability = 0.3


class Clownfish(Fish):
    NAME = "clownfish"
    NORMALITY = 60
    LEVEL = 4

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.8


class Snapper(Fish):
    NAME = "snapper"
    NORMALITY = 50
    LEVEL = 3

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.9


class Angelfish(Fish):
    NAME = "angelfish"
    NORMALITY = 40
    LEVEL = 4

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.8


class Triggerfish(Fish):
    NAME = "triggerfish"
    NORMALITY = 40
    LEVEL = 5

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.5


class Tang(Fish):
    NAME = "tang"
    NORMALITY = 45
    LEVEL = 4

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.9


class Pufferfish(Fish):
    NAME = "pufferfish"
    NORMALITY = 20
    LEVEL = 4

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.4


class Sea_Turtle(Fish):
    NAME = "sea turtle"
    NORMALITY = 30
    LEVEL = 4

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.7
        self.breakability = 0.2


class Piece_of_Kelp(Fish):
    NAME = "piece of kelp"
    NORMALITY = 40
    LEVEL = 1

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.value = 0


class Giant_Kelpfish(Fish):
    NAME = "giant kelpfish"
    NORMALITY = 50
    LEVEL = 5

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.8


class Rockfish(Fish):
    NAME = "rockfish"
    NORMALITY = 35
    LEVEL = 5

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.6


class Bonito(Fish):
    NAME = "bonito"
    NORMALITY = 45
    LEVEL = 4

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.9


class Hammerhead_Shark(Fish):
    NAME = "hammerhead shark"
    NORMALITY = 30
    LEVEL = 7

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.4
        self.breakability = 0.7


class Whale_Shark(Fish):
    NAME = "whale shark"
    NORMALITY = 10
    LEVEL = 9

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.2
        self.breakability = 0.9


class Tiger_Shark(Fish):
    NAME = "tiger shark"
    NORMALITY = 25
    LEVEL = 8

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.2
        self.breakability = 0.8


class Mako_Shark(Fish):
    NAME = "mako shark"
    NORMALITY = 30
    LEVEL = 7

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.2
        self.breakability = 0.6


class Blue_Shark(Fish):
    NAME = "blue shark"
    NORMALITY = 45
    LEVEL = 7

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.2
        self.breakability = 0.7


class Kraken(Fish):
    NAME = "kraken"
    NORMALITY = 5
    LEVEL = 10

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.0
        self.breakability = 2.0
