# Shop class
from general_functions import *
from Rod import *


def display_items(item_list):
    print("")
    tab_dist = 30
    for i in range(len(item_list)):
        end_line = ""
        extra_space = " " * (3 - (len(str(i + 1))))

        if (i + 1) % 3 == 0:
            end_line = "\n"

        display_string = "[" + str(i + 1) + "]" + extra_space + " " + item_list[i].to_string_plain()

        print(display_string, " " * (tab_dist - len(display_string)), end=end_line)
    print("\n")


class Shop:
    RODS = [
        Rod("Cheap Rod", 5, 0.0, False),
        Rod("Beginner Rod", 10, 0.0, False)
    ]

    BAIT = [
        Rod("This isn't actually bait haha", 0, 0.0, False)
    ]

    AURAS = []
    TRACKERS = []
    NETS = []

    def select_item(self, item_list, title):
        title_display("shop - " + title)
        while True:
            display_items(item_list)
            num = input(">>> (press 'q' to quit) Enter a number: ")
            if num.isdigit() and (0 < int(num) <= len(item_list)):
                num = int(num)
            elif num == 'q':
                return None
            else:
                print("[!] Invalid option")

    def main_menu(self):
        title_display("shop")

        options = ["Rods", "Bait", "Powerups", "Bucket Upgrade", "Bag Upgrade", "Go Back"]

        while True:
            display_options_from_list(options)
            selection = input(">>> Enter an option: ")
            if selection.isdigit() and (0 < int(selection) <= len(options)):
                selection = int(selection)
                if selection == 1:
                    self.select_item(self.RODS, options[0])
                elif selection == 2:
                    self.select_item(self.BAIT, options[1])
                elif selection == 3:
                    self.powerups_menu()
                elif selection == 4:
                    pass
                elif selection == 5:
                    pass
                else:
                    break
            else:
                print("[!] Invalid option")

    def powerups_menu(self):
        options = ["Auras", "Trackers", "Nets", "Go Back"]
        while True:
            display_options_from_list(options)
            selection = input(">>> Enter an option: ")
            if selection.isdigit() and (0 < int(selection) <= len(options)):
                selection = int(selection)
                if selection == 1:
                    pass
                else:
                    break
            else:
                print("[!] Invalid option")
