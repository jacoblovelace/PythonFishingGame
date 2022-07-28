from file_functions import *
from fishing import *


def start_game(save_files):
    # options list
    print("")
    options = ['Go Fishing', 'Shop', 'Puzzle', 'Save & Quit']
    display_options_from_list(options)

    # autosave
    save_the_save_files(save_files)

    test_pond = Pond('test_pond', 4, 4, [Goldfish])
    test_pond.place_fish()

    # fish until either durability runs out or no more fish left in pond
    fish_spots = test_pond.fish_spots
    cols, rows = test_pond.x, test_pond.y
    durability = int(input("Set durability value: "))
    max_durability = durability
    while durability > 0 and len(fish_spots) > 0:
        durability = do_fish(test_pond, max_durability, durability)
        if durability != 0:
            fish_spots = move_fish(fish_spots, rows, cols)


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
                    start_game(save_file_list)

# test comment
