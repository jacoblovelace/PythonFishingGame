# Fishing bucket class
# Fishing bucket holds fish up to a specified quantity

from general_functions import *
from Fish_Classes import *
from file_functions import display_options_from_list


class Fishing_Bucket:

    def __init__(self, capacity=25, contents=None):
        if contents is None:
            self.contents = []
        else:
            self.contents = contents
        self.capacity = capacity

    def display_contents(self):
        title_display("fishing bucket")
        print("")

        tab_dist = 30
        for i in range(self.capacity):
            end_line = ""
            extra_space = " " * (3 - (len(str(i + 1))))

            if (i + 1) % 3 == 0:
                end_line = "\n"

            if i + 1 > len(self.contents):
                display_string = "[" + str(i + 1) + "]" + extra_space + " {empty}"
            else:
                display_string = "[" + str(i + 1) + "]" + extra_space + " " + self.contents[i].NAME

            print(display_string, " " * (tab_dist - len(display_string)), end=end_line)
        print("\n")

    def select_fish(self, save_obj):
        while True:
            self.display_contents()
            num = input(">>> (press 'q' to quit) Enter a slot number: ")
            if num.isdigit() and (0 < int(num) <= self.capacity):
                num = int(num)
                if num <= len(self.contents):
                    self.fish_options(save_obj, num)
                else:
                    print("[!] Slot is empty")
            elif num == 'q':
                break
            else:
                print("[!] Invalid option")

    def fish_options(self, save_obj, index):
        fish = self.contents[index-1]
        print("Selected: " + fish.to_string() + " (" + str(fish.value) + " coins)")
        options = ["Release", "Sell", "Add to Aquarium", "Go Back"]
        display_options_from_list(options)
        while True:
            selection = input(">>> Select an option: ")
            if selection.isdigit() and (0 < int(selection) <= len(options)):
                selection = int(selection)
                if selection == 1:
                    self.release_fish(index - 1)
                    return
                elif selection == 2:
                    self.sell_fish(save_obj, index - 1)
                    return
                elif selection == 3:
                    print("I added it to the aquarium (not actually lol)!")
                    return
                else:
                    break
            else:
                print("[!] Invalid option")

    def release_fish(self, index):
        while True:
            fish = self.contents[index]
            confirm_release = input(">>> Are you sure you want to release "
                                    + fish.to_string() + " ? (y/n): ")
            if confirm_release == 'y':
                # remove item at specified index
                released_fish = self.contents.pop(index)
                print("Released " + released_fish.to_string())
                break
            elif confirm_release == 'n':
                break
            else:
                print("[!] Invalid option")

    def sell_fish(self, save_obj, index):
        fish_to_sell = self.contents[index]
        while True:
            confirm_sell = input(">>> Are you sure you want to sell "
                                 + fish_to_sell.to_string() + ", worth " + str(fish_to_sell.value) + " coins? (y/n): ")
            if confirm_sell == 'y':
                # remove item at specified index
                self.contents.pop(index)
                # give coins of fish to player
                save_obj.coins += fish_to_sell.value
                print("Sold " + fish_to_sell.to_string() + " for " + str(fish_to_sell.value) + " coins!")
                break
            elif confirm_sell == 'n':
                break
            else:
                print("[!] Invalid option")

    def add_fish(self, item):
        # check if item is a child of fish class
        if issubclass(type(item), Fish):
            # check if item has capacity to be added
            if len(self.contents) < self.capacity:
                self.contents.append(item)
                print("\t> Added " + item.NAME + " to the bucket")
            else:
                print("[!] Bucket is full")
        else:
            print("(i) Only fish can be added to a fishing bucket")
