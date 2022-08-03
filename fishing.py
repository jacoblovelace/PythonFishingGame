# function to manage fishing input and checks

from general_functions import *


def do_fish(pond, bucket, rod, bag):
    rod.display_stats()
    pond.display_pond()

    # get input
    while True:
        spot_input = input(">>> enter spot (press 'q' to leave pond, press 'b' to view bag): ")
        if spot_input == 'q':
            confirm_quit = 'y'
            while confirm_quit != 'n':
                confirm_quit = input(">>> Are you sure you want to leave this fishing location? [y/n]: ")
                if confirm_quit == 'y':
                    return False
                elif confirm_quit != 'n':
                    print("[!] invalid option\n")
        elif spot_input == 'b':
            bag.select_item(True, None)
        else:
            if spot_input[0].isalpha() and spot_input[1:].isdigit():
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
    rod.decrease_duraility()

    # get and display catch result
    fish_found = False
    if spot in pond.fish_spots:
        pond.fish_spots.remove(spot)
        for fish in pond.fish:
            if spot == fish.pos:
                status = fish.catch_status()
                if status == "caught":
                    print("\t> You caught a {} ({} coins)".format(fish.to_string(), fish.value))
                    bucket.add_fish(fish)
                    pond.fish.remove(fish)
                    break
                elif status == "fled":
                    break
                else:
                    print("> The fish broke your rod!")
                    rod.break_rod()
                    return False
        fish_found = True
    if not fish_found:
        print("\t\x1B[3m...Nothin' caught...\x1B[0m")

    # return False if rod breaks
    if rod.cur_durability <= 0:
        rod.break_rod()
        return False
    # else return true
    return True
