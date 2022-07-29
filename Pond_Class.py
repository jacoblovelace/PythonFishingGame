# Class for Pond object
import random


class Pond:
    def __init__(self, name, x, y, fish_types):
        self.name = name
        self.x = x
        self.y = y
        self.fish_types = fish_types
        self.fish_spots = []
        self.fish = []

    def create_pond_board(self):
        board = []
        for i in range(self.x):
            for j in range(self.y):
                board.append((self.y * i) + j)
        print(board)
        return board

    def place_fish(self):
        pond_size = self.x * self.y

        # generate random number of fish, no more than 1/3 pond size
        num_fish = random.randrange(2, (pond_size // 3) + 1)

        # create list of valid fish based on normality
        normalized_fish = []
        for fish in self.fish_types:
            for _ in range(fish.NORMALITY):
                normalized_fish.append(fish)

        for _ in range(num_fish):
            fish_spot = random.randrange(pond_size)
            self.fish_spots.append(fish_spot)
            self.fish.append(random.choice(normalized_fish)(random.randrange(3), fish_spot))

    def display_pond(self):
        print("\n||| " + ("-" * 25) + " THE POND " + ("-" * 25) + " |||")
        for r in range(self.y):
            for c in range(self.x):
                row_letter = chr(ord('A') + r)
                spot = str(row_letter) + str(c + 1)
                print("| " + str(spot), end=" ")
            print("|")
