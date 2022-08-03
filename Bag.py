# Bag class to hold items
from Rod import Rod
from general_functions import *
from Fish_Classes import *
from file_functions import display_options_from_list
from Item import Item


class Bag:
    contents = []

    def __init__(self, capacity=10):
        self.capacity = capacity

    def display_contents(self):
        title_display("bag")
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
                display_string = "[" + str(i + 1) + "]" + extra_space + " " + self.contents[i].to_string_plain()

            print(display_string, " " * (tab_dist - len(display_string)), end=end_line)
        print("\n")

    def select_item(self, is_fishing, type_requirement, is_deep_sea):
        while True:
            self.display_contents()
            num = input(">>> (press 'q' to quit) Enter a slot number: ")
            if num.isdigit() and (0 < int(num) <= self.capacity):
                num = int(num)
                if num <= len(self.contents):
                    item = self.contents[num - 1]
                    if type_requirement is None or issubclass(type_requirement, type(item)):
                        if self.item_options(item, is_fishing, is_deep_sea):
                            return item
                    else:
                        print("[!] Must select an item of type " + str(type_requirement))
                else:
                    print("[!] Slot is empty")
            elif num == 'q':
                return None
            else:
                print("[!] Invalid option")

    def item_options(self, item, is_fishing, is_deep_sea):
        options = ["Sell", "Info", "Go Back"]
        if is_fishing:
            options[0] = "Use"

        while True:
            print("> Selected: " + item.to_string())
            display_options_from_list(options)
            selection = input(">>> Select an option: ")
            if selection.isdigit() and (0 < int(selection) <= len(options)):
                selection = int(selection)
                if selection == 1:
                    if is_deep_sea and not item.deep_sea:
                        print("[!] A deep sea fishing rod is required to fish at this location!")
                    else:
                        if is_fishing:
                            self.use_item(item)
                            return True
                        else:
                            self.sell_item(item)
                elif selection == 2:
                    item.display_info()
                else:
                    break
            else:
                print("[!] Invalid option")

    def sell_item(self, item):
        while True:
            confirm_sell = input(">>> Are you sure you want to sell "
                                 + item.to_string() + " for " + str(item.value) + " coins? (y/n): ")
            if confirm_sell == 'y':
                # remove item at specified index
                self.contents.remove(item)
                # give coins of item to player

                print("Sold " + item.to_string() + " for " + str(item.value) + " coins!")
                break
            elif confirm_sell == 'n':
                break
            else:
                print("[!] Invalid option")

    def add_item(self, item):
        # check if item is NOT a child of fish class
        if issubclass(type(item), Item):
            # check if item has capacity to be added
            if len(self.contents) <= self.capacity:
                self.contents.append(item)
                print("> Added " + item.to_string() + " to the bag")
                return True
            else:
                print("[!] Bag is full")
                return False
        else:
            print("(i) Fish can only be stored in the fishing bucket")

    def use_item(self, item):
        print("> Now using " + item.to_string())
        item.use()
        self.contents.remove(item)
