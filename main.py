from time import sleep
from file_functions import *
from fishing import *
from ponds import *
from general_functions import *
from Rod import *
from Shop import Shop


def display_ponds():
    print("")
    tab_dist = 40
    for i in range(len(PONDS)):
        end_line = ""
        extra_space = " " * (3 - (len(str(i + 1))))

        if (i + 1) % 2 == 0:
            end_line = "\n"

        display_string = "[" + str(i + 1) + "] " + extra_space + "- " + PONDS[i].name

        print(display_string, " " * (tab_dist - len(display_string)), end=end_line)


def select_pond():
    choosing_location = True
    pond_selection = 1
    while choosing_location:
        title_display("fishing locations")

        display_ponds()
        print("\n[0] Go Back\n")

        pond_selection = input(">>> Select a pond: ")
        if pond_selection.isdigit() and (0 <= int(pond_selection) <= len(PONDS) + 1):
            pond_selection = int(pond_selection)

            if pond_selection == 0:
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
                        PONDS[pond_selection - 1].display_pond_info()
                    else:
                        break
                else:
                    print("[!] Invalid Option")
        else:
            print("[!] Invalid Option")

    print("Now fishing at " + str(PONDS[pond_selection - 1].name) + "...")
    return PONDS[pond_selection - 1]


def main_menu(save_obj, shop):
    save(save_obj)

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
                        if save_obj.bag.select_item(True, Rod, save_obj, selected_pond):
                            break

                    print("ROD:", save_obj.equipped_rod)
                    selected_pond.place_fish()

                    # fish until no more fish left in pond
                    while len(selected_pond.fish_spots) > 0:

                        # if rod breaks, stop fishing
                        if not do_fish(selected_pond, save_obj):
                            break
                        # if still fishing, move the fish
                        selected_pond.move_fish()

                    # if the rod did not break, add it to the bag
                    if save_obj.equipped_rod.cur_durability > 0:
                        save_obj.bag.add_item(save_obj.equipped_rod)
            elif selection == 2:
                shop.main_menu(save_obj.bag)
            elif selection == 3:
                save_obj.bucket.select_fish()
            elif selection == 4:
                save_obj.bag.select_item(False, None, False, None)
            elif selection == 5:
                pass
            elif selection == 6:
                pass
            else:
                return False
        else:
            print("[!] Invalid option")


def start_game(save_file):

    # set up shop
    shop = Shop()

    # display main activity menu
    if not main_menu(save_file, shop):
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
        game_file = choose_file()

        # if options returns True, start the game
        if file_options(game_file):

            game_running = True
            while game_running:
                if not start_game(game_file):
                    game_running = False
