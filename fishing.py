# function to manage fishing input and checks

from general_functions import *
from ponds import PONDS
from Rod import Rod


def fish_caught_options(bucket, fish):
    options = ["Add to Bucket", "Release"]
    while True:
        display_options_from_list(options)
        selection = input(">>> Add to bucket or relase: ")
        if selection.isdigit() and (0 < int(selection) <= len(options)):
            selection = int(selection)
            if selection == 1:
                bucket.add_fish(fish)
                break
            else:
                print("Released " + fish.to_string())
                break
        else:
            print("[!] Invalid option")


def do_fish(pond, save_obj):
    save_obj.equipped_rod.display_stats()
    pond.display_pond()

    # get input
    while True:
        spot_input = input(">>> enter spot (press 'q' to leave pond, press 'b' to view bag): ")
        if spot_input == 'q':
            confirm_quit = 'y'
            while confirm_quit != 'n':
                confirm_quit = input(">>> Are you sure you want to leave this fishing location? (y/n): ")
                if confirm_quit == 'y':
                    return False
                elif confirm_quit != 'n':
                    print("[!] invalid option\n")
        elif spot_input == 'b':
            save_obj.bag.select_item(save_obj, True, None, pond)
        else:
            if spot_input != "" and spot_input[0].isalpha() and spot_input[1:].isdigit():
                if (0 <= int(ord(spot_input[0].upper()) - 65) < pond.y) and (0 <= int(spot_input[1:]) <= pond.x):
                    r = ord(spot_input[0].upper()) - 65
                    c = int(spot_input[1]) - 1
                    spot = (pond.x * r) + c
                    break
                else:
                    print("[!] Invalid move")
            else:
                print("[!] Invalid move")

    # update durability
    save_obj.equipped_rod.decrease_duraility()

    # get and display catch result
    fish_found = False
    if spot in pond.fish_spots:
        pond.fish_spots.remove(spot)
        for fish in pond.fish:
            if spot == fish.pos:
                status = fish.catch_status(save_obj.equipped_rod)
                if status == "caught":
                    print("\t> You caught a {} ({} coins)".format(fish.to_string(), fish.value))

                    fish_caught_options(save_obj.bucket, fish)
                    pond.fish.remove(fish)
                    break
                elif status == "fled":
                    break
                else:
                    print("> The fish broke your rod!")
                    save_obj.equipped_rod.break_rod()
                    return False
        fish_found = True
    if not fish_found:
        print("\t\x1B[3m...Nothin' caught...\x1B[0m")

    # return False if rod breaks
    if save_obj.equipped_rod.cur_durability <= 0:
        save_obj.equipped_rod.break_rod()
        return False
    # else return true
    return True


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


def select_pond(save_obj):
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

            choosing_option = True
            while choosing_option:
                options = ['Fish Here', 'Pond Info', 'Go Back']
                display_options_from_list(options)

                pond_options_select = input(">>> Enter an option: ")
                if pond_options_select.isdigit() and (0 < int(pond_options_select) <= len(options)):
                    pond_options_select = int(pond_options_select)
                    if pond_options_select == 1:
                        # require rod
                        while True:
                            print("(i) Select a rod to equip")
                            if save_obj.bag.select_item(save_obj, True, Rod, PONDS[pond_selection - 1]):
                                choosing_option = False
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


def fishing(save_obj):
    selected_pond = select_pond(save_obj)
    if selected_pond:

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
