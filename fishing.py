# function to manage fishing input and checks

from general_functions import *


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
    rod.display_stats()
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
            save_obj.bag.select_item(True, None, save_obj, pond)
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
    save_obj.rod.decrease_duraility()

    # get and display catch result
    fish_found = False
    if spot in pond.fish_spots:
        pond.fish_spots.remove(spot)
        for fish in pond.fish:
            if spot == fish.pos:
                status = fish.catch_status(rod)
                if status == "caught":
                    print("\t> You caught a {} ({} coins)".format(fish.to_string(), fish.value))

                    fish_caught_options(bucket, fish)
                    pond.fish.remove(fish)
                    break
                elif status == "fled":
                    break
                else:
                    print("> The fish broke your rod!")
                    save_obj.rod.break_rod()
                    return False
        fish_found = True
    if not fish_found:
        print("\t\x1B[3m...Nothin' caught...\x1B[0m")

    # return False if rod breaks
    if save_obj.rod.cur_durability <= 0:
        save_obj.rod.break_rod()
        return False
    # else return true
    return True
