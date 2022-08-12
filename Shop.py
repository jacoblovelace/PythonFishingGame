# Shop class
from file_functions import save
from general_functions import *
from Rod import *


def display_items(item_list):
    print("")
    tab_dist = 40
    for i in range(len(item_list)):
        end_line = ""
        extra_space = " " * (3 - (len(str(i + 1))))

        if (i + 1) % 2 == 0:
            end_line = "\n"

        display_string = "[" + str(i + 1) + "]" + extra_space + " " \
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


def buy_storage_upgrade(save_obj, container):
    upgrade_cost = int((container.capacity ** 2.5) * 0.5)
    # check if player's current amount of coins is equal to or greater than cost to buy
    if save_obj.coins >= upgrade_cost:
        while True:
            confirm = input(" >>> Increase capacity from " + str(container.capacity)
                            + "->" + str(container.capacity + 5) + " for " + str(upgrade_cost) + " coins? [y/n]: ")
            if confirm == 'y':
                # subtract item.value from player's total coins
                save_obj.coins -= upgrade_cost
                container.capacity += 5
                print("> Capacity upgrade successfully purchased for "
                      + str(upgrade_cost) + " coins!")
                break
            elif confirm == 'n':
                break
            else:
                print("[!] Invalid option")
    else:
        print("[!] Not enough coins!")


def storage_upgrade_menu(save_obj, title):

    while True:
        title_display("shop - " + title)
        storage_upgrade_options(save_obj)

        selection = input("Enter an option: ")
        if selection.isdigit() and (0 < int(selection) <= 2):
            if selection == '1':
                buy_storage_upgrade(save_obj, save_obj.bucket)
            else:
                buy_storage_upgrade(save_obj, save_obj.bag)
        elif selection == 'q':
            break
        else:
            print("[!] Invalid option")


def storage_upgrade_options(save_obj):
    print("\n[1] Increase bucket capacity (" + str(save_obj.bucket.capacity)
          + "->" + str(save_obj.bucket.capacity + 5) + ") - "
          + str(int((save_obj.bucket.capacity ** 2.5) * 0.5)) + " coins")
    print("[2] Increase bag capacity (" + str(save_obj.bag.capacity) +
          "->" + str(save_obj.bag.capacity + 5) + ") - "
          + str(int((save_obj.bag.capacity ** 2.5) * 0.5)) + " coins")
    print("\n[q] Go Back\n")


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
        save_obj.display_stats()
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


def powerups_menu(save_obj, title):
    options = ["Auras", "Trackers", "Nets", "Go Back"]
    while True:
        title_display("shop - " + title)
        save_obj.display_stats()
        display_options_from_list(options)
        selection = input(">>> Enter an option: ")
        if selection.isdigit() and (0 < int(selection) <= len(options) - 1):
            selection = int(selection)
            if selection == 1:
                select_item(save_obj, Shop.AURAS, "AURAS")
            elif selection == 2:
                select_item(save_obj, Shop.TRACKERS, "TRACKERS")
            else:
                select_item(save_obj, Shop.NETS, "NETS")
        elif selection == 'q':
            break
        else:
            print("[!] Invalid option")


class Shop:
    RODS = [
        Rod("Cheap Rod", 10, 5, -0.2, False),
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
        options = ["Rods", "Bait", "Powerups", "Bucket & Bag Upgrades", "Go Back"]

        while True:
            # SAVE POINT
            save(save_obj)

            title_display("shop")
            save_obj.display_stats()
            display_options_from_list(options)
            selection = input(">>> Enter an option: ")
            if selection.isdigit() and (0 < int(selection) <= len(options) - 1):
                selection = int(selection)
                if selection == 1:
                    select_item(save_obj, self.RODS, options[0])
                elif selection == 2:
                    select_item(save_obj, self.BAIT, options[1])
                elif selection == 3:
                    powerups_menu(save_obj, options[2])
                else:
                    storage_upgrade_menu(save_obj, options[3])
            elif selection == 'q':
                break
            else:
                print("[!] Invalid option")
