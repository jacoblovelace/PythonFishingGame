# Class for Pond object
import random


class Pond:

    def __init__(self, name, x, y, num_fish_range, fish_types, description):
        self.name = name
        self.x = x
        self.y = y
        self.fish_types = fish_types
        self.description = description
        self.fish_spots = []
        self.fish = []
        self.pond_size = self.x * self.y
        self.board = [i for i in range(self.pond_size)]
        self.num_fish = random.randrange((self.pond_size // num_fish_range[0]), (self.pond_size // num_fish_range[1] + 1))

    def place_fish(self):

        # create list of valid fish based on normality
        normalized_fish = []
        for fish in self.fish_types:
            for _ in range(fish.NORMALITY):
                normalized_fish.append(fish)

        self.fish_spots = random.sample(range(self.pond_size), self.num_fish)
        for fish_spot in self.fish_spots:
            self.fish.append(random.choice(normalized_fish)(random.randrange(3)+1, fish_spot))

        # place fish on the board
        for fish in self.fish:
            self.board[fish.pos] = fish

    def display_pond(self):
        print("\n||| " + ("-" * 20) + " " + self.name.upper() + " " + ("-" * 20) + " |||\n")
        for r in range(self.y):
            for c in range(self.x):
                row_letter = chr(ord('A') + r)
                spot = str(row_letter) + str(c + 1)
                print("| " + str(spot), end=" ")
            print("|")
        print('')
