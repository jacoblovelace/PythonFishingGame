# Fish class and its subclasses
from abc import abstractmethod, ABC
from math import sqrt
from numpy.random import choice


class Fish:
    NAME = ""
    NORMALITY = 100
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

    def catch_status(self, rod):
        statuses = ["caught", "fled", "broke"]

        if choice([True, False], p=[self.cactchability, 1.0 - self.cactchability]):
            # calculate new fish breakability given rod resistance
            breakability = self.breakability - rod.resistance
            if breakability < 0.0:
                breakability = 0.0

            if choice([True, False], p=[1.0 - breakability, breakability]):
                return statuses[0]
            else:
                print("\t\x1B[3mThe fish broke your rod!\x1B[0m")
                return statuses[2]
        else:
            print("\t\x1B[3mThe fish got away!\x1B[0m")
        return statuses[1]

    @abstractmethod
    def get_constructor_string(self):
        pass


class Goldfish(Fish):
    NAME = "goldfish"
    NORMALITY = 70

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.breakability = -0.5

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Koi(Fish):
    NAME = "koi"
    NORMALITY = 90

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.breakability = -0.2

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Catfish(Fish):
    NAME = "catfish"
    NORMALITY = 50

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.8

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Trout(Fish):
    NAME = "trout"
    NORMALITY = 70

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Bass(Fish):
    NAME = "bass"
    NORMALITY = 60

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.8

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Salmon(Fish):
    NAME = "salmon"
    NORMALITY = 40

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.7

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Carp(Fish):
    NAME = "carp"
    NORMALITY = 55
    LEVEL = 2

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Pike(Fish):
    NAME = "pike"
    NORMALITY = 30
    LEVEL = 2

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.7

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Crappie(Fish):
    NAME = "crappie"
    NORMALITY = 70
    LEVEL = 2

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.8

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Perch(Fish):
    NAME = "perch"
    NORMALITY = 55
    LEVEL = 2

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.9

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Shad(Fish):
    NAME = "shad"
    NORMALITY = 50
    LEVEL = 2

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.8

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Herring(Fish):
    NAME = "herring"
    NORMALITY = 40
    LEVEL = 2

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.6

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Dead_Fish(Fish):
    NAME = "dead fish"
    NORMALITY = 70

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.value = 2

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Mutant_Minnow(Fish):
    NAME = "mutant minnow"
    NORMALITY = 40
    LEVEL = 2

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Glowfish(Fish):
    NAME = "glowfish"
    NORMALITY = 15
    LEVEL = 3

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.5

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Electric_Eel(Fish):
    NAME = "electric eel"
    NORMALITY = 35
    LEVEL = 3

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.6

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Piranha(Fish):
    NAME = "piranha"
    NORMALITY = 70
    LEVEL = 3

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.breakability = 0.2

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Bull_Shark(Fish):
    NAME = "bull shark"
    NORMALITY = 15
    LEVEL = 7

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.5
        self.breakability = 0.7

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Payara(Fish):
    NAME = "payara"
    NORMALITY = 40
    LEVEL = 4

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.7
        self.breakability = 0.3

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Jellyfish(Fish):
    NAME = "jellyfish"
    NORMALITY = 55
    LEVEL = 3

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.6

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Sardine(Fish):
    NAME = "sardine"
    NORMALITY = 65
    LEVEL = 2

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.9

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Anchovy(Fish):
    NAME = "anchovy"
    NORMALITY = 60
    LEVEL = 1

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Great_White_Shark(Fish):
    NAME = "great white shark"
    NORMALITY = 25
    LEVEL = 8

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.2
        self.breakability = 0.8

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Tuna(Fish):
    NAME = "tuna"
    NORMALITY = 55
    LEVEL = 5

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.4
        self.breakability = 0.3

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Flounder(Fish):
    NAME = "flounder"
    NORMALITY = 30
    LEVEL = 4

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.7
        self.breakability = 0.1

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Mullet(Fish):
    NAME = "mullet"
    NORMALITY = 55
    LEVEL = 3

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.9

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Redfish(Fish):
    NAME = "redfish"
    NORMALITY = 40
    LEVEL = 4

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.8

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Mackerel(Fish):
    NAME = "mackerel"
    NORMALITY = 60
    LEVEL = 3

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.breakability = 0.1

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Croaker(Fish):
    NAME = "croaker"
    NORMALITY = 30
    LEVEL = 3

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Clownfish(Fish):
    NAME = "clownfish"
    NORMALITY = 60
    LEVEL = 4

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.8

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Snapper(Fish):
    NAME = "snapper"
    NORMALITY = 50
    LEVEL = 3

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.9

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Angelfish(Fish):
    NAME = "angelfish"
    NORMALITY = 40
    LEVEL = 4

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.8

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Triggerfish(Fish):
    NAME = "triggerfish"
    NORMALITY = 40
    LEVEL = 5

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.5

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Tang(Fish):
    NAME = "tang"
    NORMALITY = 45
    LEVEL = 4

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.9

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Pufferfish(Fish):
    NAME = "pufferfish"
    NORMALITY = 20
    LEVEL = 4

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.4

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Sea_Turtle(Fish):
    NAME = "sea turtle"
    NORMALITY = 30
    LEVEL = 4

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.7
        self.breakability = 0.2

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Piece_of_Kelp(Fish):
    NAME = "piece of kelp"
    NORMALITY = 40
    LEVEL = 1

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.value = 1

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Giant_Kelpfish(Fish):
    NAME = "giant kelpfish"
    NORMALITY = 50
    LEVEL = 5

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.8

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Rockfish(Fish):
    NAME = "rockfish"
    NORMALITY = 35
    LEVEL = 5

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.6

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Bonito(Fish):
    NAME = "bonito"
    NORMALITY = 45
    LEVEL = 4

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.9

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Desert_Sucker(Fish):
    NAME = "desert sucker"
    NORMALITY = 40
    LEVEL = 5

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Loach_Minnow(Fish):
    NAME = "loach minnow"
    NORMALITY = 60
    LEVEL = 5

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.5

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Pupfish(Fish):
    NAME = "pupfish"
    NORMALITY = 45
    LEVEL = 6

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.6

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Bonytail_Chub(Fish):
    NAME = "bonytail chub"
    NORMALITY = 30
    LEVEL = 6

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.9
        self.breakability = 0.2

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Squawfish(Fish):
    NAME = "squawfish"
    NORMALITY = 20
    LEVEL = 7

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.8
        self.breakability = 0.3

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Hammerhead_Shark(Fish):
    NAME = "hammerhead shark"
    NORMALITY = 30
    LEVEL = 7

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.4
        self.breakability = 0.7

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Whale_Shark(Fish):
    NAME = "whale shark"
    NORMALITY = 10
    LEVEL = 9

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.2
        self.breakability = 0.9

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Tiger_Shark(Fish):
    NAME = "tiger shark"
    NORMALITY = 25
    LEVEL = 8

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.2
        self.breakability = 0.8

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Mako_Shark(Fish):
    NAME = "mako shark"
    NORMALITY = 30
    LEVEL = 7

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.2
        self.breakability = 0.6

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Blue_Shark(Fish):
    NAME = "blue shark"
    NORMALITY = 45
    LEVEL = 7

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.2
        self.breakability = 0.7

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"


class Kraken(Fish):
    NAME = "kraken"
    NORMALITY = 5
    LEVEL = 10

    def __init__(self, size=1, pos=0):
        super().__init__(size, pos)
        self.cactchability = 0.0
        self.breakability = 2.0

    def get_constructor_string(self):
        return self.NAME + f"('{self.size}', {self.pos})"
