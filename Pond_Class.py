# Class for Pond object
import random


class Pond:
    def __init__(self, name, x, y, fish_types):
        self.name = name
        self.x = x
        self.y = y
        self.fish_types = fish_types
        self.fish_spots = []

        def place_fish(self):
            pond_size = self.x * self.y

            # generate random number of fish, no more than 1/3 pond size
            num_fish = random.randrange(2, (pond_size // 3) + 1)
