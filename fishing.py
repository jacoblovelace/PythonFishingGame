import random
from Rod import *


def do_fish(pond, bucket, rod):
    pond.display_pond()

    while True:
        spot_input = input(">>> enter spot (press 'q' to leave pond): ")
        if spot_input == 'q':
            confirm_quit = 'y'
            while confirm_quit != 'n':
                confirm_quit = input("Are you sure you want to leave this fishing location? [y/n]: ")
                if confirm_quit == 'y':
                    return False
                elif confirm_quit != 'n':
                    print("[!] invalid option\n")
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

    fish_found = False
    if spot in pond.fish_spots:
        pond.fish_spots.remove(spot)
        for fish in pond.fish:
            if spot == fish.pos:
                status = fish.catch_status()
                if status == "caught":
                    print("\t\x1B[3mYou caught a fish!\x1B[0m")
                    print("\t\x1B[3mFish Info: {} {} ({} coins)\x1B[0m".format(fish.size, fish.NAME, fish.value))
                    bucket.add_fish(fish)
                    pond.fish.remove(fish)
                    break
                elif status == "fled":
                    break
                else:
                    rod.cur_durability = 0
                    return False
        fish_found = True

    if not fish_found:
        print("\t\x1B[3m...Nothin' caught...\x1B[0m")

    rod.use_rod()

    return True
