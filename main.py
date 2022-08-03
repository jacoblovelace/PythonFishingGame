from time import sleep

from file_functions import *
from fishing import *
from ponds import *
from Bucket_Class import Fishing_Bucket
from Bag import Bag
from general_functions import *
from Rod import *
from Shop import Shop


def select_pond():
    choosing_location = True
    pond_selection = 1
    while choosing_location:
        title_display("fishing locations")

        print("\n[1] Go Back\n")
        for i in range(len(PONDS)):
            print("[" + str(i + 2) + "] - " + PONDS[i].name)
        print('')

        pond_selection = input(">>> Select a pond: ")
        if pond_selection.isdigit() and (1 <= int(pond_selection) < len(PONDS) + 2):
            pond_selection = int(pond_selection)

            if pond_selection == 1:
                return None

            while True:
                options = ['Fish Here', 'Pond Info', 'Go Back']
                display_options_from_list(options)

                pond_options_select = input(">>> Enter an option: ")
                if pond_options_select.isdigit() and (0 < int(pond_options_select) <= len(options)):
                    pond_options_select = int(pond_options_select)
                    if pond_options_select == 1:
                        choosing_location = False
                        break
                    elif pond_options_select == 2:
                        PONDS[pond_selection - 2].display_pond_info()
                    else:
                        break
                else:
                    print("[!] Invalid Option")
        else:
            print("[!] Invalid Option")

    print("Now fishing at " + str(PONDS[pond_selection - 2].name) + "...")
    return PONDS[pond_selection - 2]


def main_menu(shop, bucket, bag):
    options = ["Go Fishing", "Shop", "My Bucket", "My Bag", "My Aquarium", "Puzzle", "Exit"]
    while True:
        title_display("main menu")
        display_options_from_list(options)
        selection = input(">>> Enter an option: ")
        if selection.isdigit() and (0 < int(selection) <= len(options)):
            selection = int(selection)

            if selection == 1:

                selected_pond = select_pond()
                if selected_pond:

                    # require rod
                    while True:
                        print("(i) Select a rod to equip")
                        equipped_rod = bag.select_item(True, Rod)
                        if equipped_rod is not None:
                            break

                    # if equipped_rod.cur_durability <= 0:
                    #     print("[!] Unable to fish without a fishing rod!")

                    selected_pond.place_fish()

                    # fish until no more fish left in pond
                    while len(selected_pond.fish_spots) > 0:

                        # if rod breaks, stop fishing
                        if not do_fish(selected_pond, bucket, equipped_rod, bag):
                            break
                        # if still fishing, move the fish
                        selected_pond.move_fish()

                    # if the rod did not break, add it to the bag
                    if equipped_rod.exists:
                        bag.add_item(equipped_rod)
            elif selection == 2:
                shop.main_menu(bag)
            elif selection == 3:
                bucket.select_fish()
            elif selection == 4:
                bag.select_item(False, None)
            elif selection == 5:
                pass
            elif selection == 6:
                pass
            else:
                return False
        else:
            print("[!] Invalid option")


def start_game(save_files):
    # autosave
    save_the_save_files(save_files)

    # set up shop
    shop = Shop()

    # set up storage and items
    my_bucket = Fishing_Bucket(20)
    my_bag = Bag(20)

    rods = [Rod("Cheap Rod", 10, 5, 0.0, False), Rod("God Rod", 5000, 100, 2.0, True)]

    for rod in rods:
        my_bag.add_item(rod)

    # display main activity menu
    if not main_menu(shop, my_bucket, my_bag):
        return False


def title_sequence():
    lines = [" ______         ______                __", "|   __ \.--.--.|   __ \.-----..-----.|  |",
             "|    __/|  |  ||      <|  -__||  -__||  |", "|___|   |___  ||___|__||_____||_____||__|",
             "        |_____|"]
    for line in lines:
        print(line)
        sleep(0.3)

    sleep(0.7)
    print("Game Created by: Coby and Angelo")
    sleep(1.5)
    print("...\x1B[1m\x1B[3mEnjoy!\x1B[0m")
    sleep(1.5)


if __name__ == '__main__':

    # title_sequence()

    choosing_file = True
    while choosing_file:
        # choose file
        game_file, save_file_list = choose_file()

        # if file does not exist, ask to create file
        if not check_if_file_exists(game_file):
            create_new_file(game_file, save_file_list)

        # if file exists, get options
        if check_if_file_exists(game_file):
            # if options returns True, start the game
            if file_options(game_file, save_file_list):

                game_running = True
                while game_running:
                    if not start_game(save_file_list):
                        game_running = False
