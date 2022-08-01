from file_functions import *
from fishing import *
from ponds import *
from Bucket_Class import Fishing_Bucket


def select_pond():
    choosing_location = True
    pond_selection = 1
    while choosing_location:
        print("")
        for i in range(len(PONDS)):
            print("[" + str(i + 1) + "] - " + PONDS[i].name)
        print('')

        pond_selection = input("Select a pond: ")
        if pond_selection.isdigit() and (0 < int(pond_selection) <= len(PONDS)):
            pond_selection = int(pond_selection)

            while True:
                options = ['Fish Here', 'Pond Info', 'Go Back']
                display_options_from_list(options)

                pond_options_select = input("Enter an option: ")
                if pond_options_select.isdigit() and (0 < int(pond_options_select) <= len(options)):
                    pond_options_select = int(pond_options_select)
                    if pond_options_select == 1:
                        choosing_location = False
                        break
                    elif pond_options_select == 2:
                        PONDS[pond_selection-1].display_pond_info()
                    else:
                        break
                else:
                    print("[!] Invalid Option")
        else:
            print("[!] Invalid Option")

    print("Now fishing at " + str(PONDS[pond_selection-1].name) + "...")
    return PONDS[pond_selection-1]


def main_menu(bucket):
    options = ["Go Fishing", "My Bucket", "My Bag", "My Aquarium", "Puzzle", "Exit"]
    while True:
        display_options_from_list(options)
        selection = input("Enter an option: ")
        if selection.isdigit() and (0 < int(selection) <= len(options)):
            if selection == '1':
                selected_pond = select_pond()
                selected_pond.place_fish()

                # fish until either durability runs out or no more fish left in pond
                durability = int(input("Set durability value: "))
                max_durability = durability
                while durability > 0 and len(selected_pond.fish_spots) > 0:
                    durability = do_fish(selected_pond, max_durability, durability, bucket)
                    if durability != 0:
                        move_fish(selected_pond)

            elif selection == '2':
                bucket.select_fish()
            elif selection == '3':
                pass
            elif selection == '4':
                pass
            elif selection == '5':
                pass
            else:
                return False


def start_game(file, save_files):
    # autosave
    save_the_save_files(save_files)

    my_bucket = Fishing_Bucket(20)

    # display main activity menu
    if not main_menu(my_bucket):
        return False




if __name__ == '__main__':

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
                    if not start_game(game_file, save_file_list):
                        game_running = False
