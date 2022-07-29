# Fishing bucket class
# Fishing bucket holds fish up to a specified quantity

from Fish_Classes import *
from file_functions import display_options_from_list
from Save_File_Class import *


class Fishing_Bucket:
    contents = []

    def __init__(self, capacity=25):
        self.capacity = capacity

    def display_contents(self):
        print("--- FISHING BUCKET ---")
        for i in range(len(self.contents)):
            for j in range(3):
                print("[" + str(i+1) + "] - " + self.contents[i], end="\t")
            print("")

    def select_fish(self):
        self.display_contents()
        while True:
            num = input("(press 'q' to quit) Enter a slot number: ")
            if num.isdigit() and (0 < int(num) <= len(self.contents)):
                self.fish_options(num)
            elif num == 'q':
                break
            else:
                print("[!] Invalid option")

    def fish_options(self, index):
        options = ["Release", "Sell", "Add to Aquarium", "Go Back"]
        display_options_from_list(options)
        while True:
            selection = input("Select an option: ")
            if selection.isdigit() and (0 < int(selection) <= len(options)):
                selection = int(selection)
                if selection == 1:
                    self.release_fish(index-1)
                elif selection == 2:
                    pass
                elif selection == 3:
                    pass
                else:
                    break
            else:
                print("[!] Invalid option")

    def release_fish(self, index):
        while True:
            confirm_release = input("Are you sure you want to release this fish:" + self.contents[index].NAME + " (y/n)?")
            if confirm_release == 'y':
                # remove item at specified index
                released_fish = self.contents.pop(index)
                print("Released " + released_fish.NAME)
                break
            elif confirm_release == 'n':
                break
            else:
                print("[!] Invalid option")

    def sell_fish(self, index):
        fish_to_sell = self.contents[index]
        while True:
            confirm_sell = input("Are you sure you want to sell this fish:"
                                 + fish_to_sell.NAME + ", worth " + fish_to_sell.value + " coins (y/n)?")
            if confirm_sell == 'y':
                # remove item at specified index
                sold_fish = self.contents.pop(index)
                # give coins of fish to player

                print("Sold " + sold_fish.NAME + " for " + sold_fish.value + " coins")
                break
            elif confirm_sell == 'n':
                break
            else:
                print("[!] Invalid option")

    def add_fish(self, item):
        # check if item is a child of fish class
        if issubclass(item, Fish):
            # check if item has capacity to be added
            if len(self.contents) <= self.capacity:
                self.contents.append(item)
                print("Added " + item.NAME + " to the bag")
            else:
                print("[!] Bucket is full")
        else:
            print("(i) Only fish can be added to a fishing bucket")
