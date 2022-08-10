# Class for Pond object
import random
from general_functions import *


class Pond:

    def __init__(self, name, level, x, y, num_fish_range, deep_sea, fish_types, description):
        self.name = name
        self.level = level
        self.x = x
        self.y = y
        self.fish_types = fish_types
        self.description = description
        self.deep_sea = deep_sea
        self.fish_spots = []
        self.fish = []
        self.pond_size = self.x * self.y
        self.board = [i for i in range(self.pond_size)]
        self.num_fish_range = num_fish_range
        self.num_fish = random.randrange((self.pond_size // num_fish_range[0]),
                                         (self.pond_size // num_fish_range[1] + 1))

    def place_fish(self):

        # create list of valid fish based on normality
        normalized_fish = []
        for fish in self.fish_types:
            for _ in range(fish.NORMALITY):
                normalized_fish.append(fish)

        self.fish_spots = random.sample(range(self.pond_size), self.num_fish)
        for fish_spot in self.fish_spots:
            self.fish.append(random.choice(normalized_fish)(random.randrange(3) + 1, fish_spot))

        # place fish on the board
        for fish in self.fish:
            self.board[fish.pos] = fish

    def move_fish(self):
        list_of_options = []
        updated_fish_spots = []

        # calculate and make list of move options for each fish
        for fish_spot in self.fish_spots:
            # initialize list with fish object as first element
            options = [self.board[fish_spot]]
            # check left side
            if (fish_spot % self.x) != 0:
                options.append(fish_spot - 1)
            # check right side
            if ((fish_spot + 1) % self.x) != 0:
                options.append(fish_spot + 1)
            # check top
            if fish_spot + 1 > self.x:
                options.append(fish_spot - self.x)
            # check bottom
            if fish_spot < (self.x * (self.y - 1)):
                options.append(fish_spot + self.x)
            # always add same spot to options
            options.append(fish_spot)
            list_of_options.append(options)

        # sort list of options shortest to longest to increase chances of move availability
        list_of_options.sort(key=len)

        for options in list_of_options:
            # choose a random spot from list of options
            cur_fish = options[0]
            options = options[1:]
            choice = random.choice(options)
            # if spot already in the new fish spots, remove it and choose again
            while choice in updated_fish_spots and len(options) > 0:
                options.remove(choice)
                if len(options) > 0:
                    choice = random.choice(options)
            if len(options) > 0:
                updated_fish_spots.append(choice)
                cur_fish.pos = choice

        self.board = [i for i in range(self.x * self.y)]
        for fish in self.fish:
            self.board[fish.pos] = fish
        self.fish_spots = updated_fish_spots

    def display_pond(self):
        title_display(self.name)
        print("")
        for r in range(self.y):
            for c in range(self.x):
                row_letter = chr(ord('A') + r)
                spot = str(row_letter) + str(c + 1)
                print("| " + str(spot), end=" ")
            print("|")
        print('')

    def display_pond_info(self):
        print("\n" + self.name + ":")
        print("\tSize: " + str(self.x) + " x " + str(self.y))
        print("\tFish Density: 1/" + str(self.num_fish_range[0]) + " to 1/" + str(self.num_fish_range[1]))
        print("\tDescription: " + self.description)
        print("\tFish:")
        for fish in self.fish_types:
            print("\t\t- " + fish.NAME)
        if self.deep_sea:
            print("\n\t(i) Deep sea fishing rod required!")
