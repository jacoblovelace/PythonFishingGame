import math
from time import sleep
from file_functions import *
from fishing import *
from general_functions import *
from Shop import Shop


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


def start_game(save_obj):

    # display main activity menu
    if not main_menu(save_obj):
        return False


def main_menu(save_obj):
    # set up shop
    shop = Shop()
    options = ["Go Fishing", "Shop", "My Bucket", "My Bag", "My Aquarium", "Exit"]
    while True:
        save(save_obj)
        title_display("main menu")
        save_obj.display_stats()
        display_options_from_list(options)
        selection = input(">>> Enter an option: ")
        if selection.isdigit() and (0 < int(selection) <= len(options)-1):
            selection = int(selection)

            if selection == 1:
                fishing(save_obj)
            elif selection == 2:
                shop.main_menu(save_obj)
            elif selection == 3:
                save_obj.bucket.select_fish(save_obj)
            elif selection == 4:
                save_obj.bag.select_item(save_obj, False, None, None)
            else:
                pass
        elif selection == 'q':
            return False
        else:
            print("[!] Invalid option")


if __name__ == '__main__':
    # title_sequence()

    choosing_file = True
    while choosing_file:
        # choose file
        save_obj = choose_file()

        # if options returns True, start the game
        if file_options(save_obj):

            game_running = True
            while game_running:
                if not start_game(save_obj):
                    game_running = False
