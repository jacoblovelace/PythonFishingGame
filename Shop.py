# Shop class
from general_functions import *
from Rod import *


def display_coins(save_obj):
    print("Coins: " + str(save_obj.coins))


def display_items(item_list):
    print("")
    tab_dist = 40
    for i in range(len(item_list)):
        end_line = ""
        extra_space = " " * (3 - (len(str(i + 1))))

        if (i + 1) % 2 == 0:
            end_line = "\n"

        display_string = "[" + str(i + 1) + "]" + extra_space + " "\
                         + item_list[i].to_string_plain() + " - " + str(item_list[i].value) + " coins"

        print(display_string, " " * (tab_dist - len(display_string)), end=end_line)
    print("\n")


def buy_item(save_obj, item):
    # check if player's current amount of coins is equal to or greater than item.value
    if save_obj.coins >= item.value:
        # check if bag has space for item
        if save_obj.bag.add_item(item):
            # subtract item.value from player's total coins
            save_obj.coins -= item.value
            print("> " + item.to_string() + " successfully purchased for " + str(item.value) + " coins!")
        else:
            print("[!] Cannot purchase item! Bag is full!")
    else:
        print("[!] Not enough coins!")


def item_options(save_obj, item):
    item.display_info_shop()
    options = ["Buy", "Go Back"]
    while True:
        display_options_from_list(options)
        selection = input(">>> Enter an option: ")
        if selection.isdigit() and (0 < int(selection) <= len(options)):
            selection = int(selection)
            if selection == 1:
                buy_item(save_obj, item)
                break
            else:
                break
        else:
            print("[!] Invalid option")


def select_item(save_obj, item_list, title):
    while True:
        title_display("shop - " + title)
        display_coins(save_obj)
        display_items(item_list)
        num = input(">>> (press 'q' to quit) Enter a number: ")
        if num.isdigit() and (0 < int(num) <= len(item_list)):
            num = int(num)
            item = item_list[num - 1]
            print("> Selected: " + item.to_string())
            item_options(save_obj, item)
        elif num == 'q':
            return None
        else:
            print("[!] Invalid option")


def powerups_menu():
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


class Shop:
    RODS = [
        Rod("Cheap Rod", 10, 5, 0.0, False),
        Rod("Beginner Rod", 30, 10, 0.0, False),
        Rod("Robust Rod", 100, 20, 0.3, False),
        Rod("Heavy Duty Rod", 30, 10, 0.8, False),
        Rod("Deep Sea Rod", 250, 20, 0.2, True)
    ]

    BAIT = [
        Rod("This isn't actually bait haha", 999, 10, 0.0, False)
    ]

    AURAS = []
    TRACKERS = []
    NETS = []

    def main_menu(self, save_obj):
        options = ["Rods", "Bait", "Powerups", "Bucket Upgrade", "Bag Upgrade", "Go Back"]

        while True:
            title_display("shop")
            display_coins(save_obj)
            display_options_from_list(options)
            selection = input(">>> Enter an option: ")
            if selection.isdigit() and (0 < int(selection) <= len(options)):
                selection = int(selection)
                if selection == 1:
                    select_item(save_obj, self.RODS, options[0])
                elif selection == 2:
                    select_item(save_obj, self.BAIT, options[1])
                elif selection == 3:
                    powerups_menu()
                elif selection == 4:
                    pass
                elif selection == 5:
                    pass
                else:
                    break
            else:
                print("[!] Invalid option")
