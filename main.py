from time import sleep

from file_functions import *
from fishing import *
from ponds import *
from Bucket_Class import Fishing_Bucket
from Bag import Bag
from general_functions import *
from Rod import *


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


def fishing_options(my_bag):
    options = ["Cast", "Bag"]
    while True:
        display_options_from_list(options)
        selection = input(">>> Enter an option: ")
        if selection.isdigit() and (0 < int(selection) <= len(options)):
            selection = int(selection)
            if selection == 1:
                break
            else:
                my_bag.select_item(True)
        else:
            print("[!] Invalid option")


def main_menu(bucket, rod, my_bag):
    options = ["Go Fishing", "My Bucket", "My Bag", "My Aquarium", "Puzzle", "Exit"]
    while True:
        title_display("main menu")
        display_options_from_list(options)
        selection = input(">>> Enter an option: ")
        if selection.isdigit() and (0 < int(selection) <= len(options)):
            if selection == '1':
                if rod.cur_durability <= 0:
                    print("[!] Unable to fish without a fishing rod!")
                else:
                    selected_pond = select_pond()
                    if selected_pond:
                        selected_pond.place_fish()

                        # fish until either durability runs out or no more fish left in pond
                        while rod.cur_durability > 0 and len(selected_pond.fish_spots) > 0:
                            fishing_options(my_bag)

                            if not do_fish(selected_pond, bucket, rod):
                                break
                            if rod.cur_durability != 0:
                                selected_pond.move_fish()

            elif selection == '2':
                bucket.select_fish()
            elif selection == '3':
                my_bag.select_item()
            elif selection == '4':
                pass
            elif selection == '5':
                pass
            else:
                return False
        else:
            print("[!] Invalid option")


def start_game(save_files):
    # autosave
    save_the_save_files(save_files)

    my_bucket = Fishing_Bucket(20)

    my_rod = Rod("boring rod", 20, 0.2, False)

    my_bag = Bag(20)
    my_bag.add_item(my_rod)

    # display main activity menu
    if not main_menu(my_bucket, my_rod, my_bag):
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
