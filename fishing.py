from Fish_Classes import *
from Pond_Class import *


def do_fish(pond, max_durability, cur_durability):
    pond.display_pond()

    sizes = ['small', 'medium', 'large']

    get_spot = input(">>> enter spot: ")

    # convert input into int
    r = ord(get_spot[0]) - 65
    c = int(get_spot[1]) - 1
    spot = (pond.x * r) + c

    fish_found = False
    if spot in pond.fish_spots:
        pond.fish_spots.remove(spot)
        for fish in pond.fish:
            print('spot:', spot, 'fish.pos', fish.pos)
            if spot == fish.pos:
                print("\t\x1B[3mYou caught a fish!\x1B[0m")
                print("\t\x1B[3mFish Info: {} {} ({} coins)\x1B[0m".format(sizes[fish.size-1], fish.NAME, fish.value))
                pond.fish.remove(fish)
                break
        fish_found = True
    if not fish_found:
        print("\t\x1B[3m...Nothin' caught...\x1B[0m")

    # update durability and return
    cur_durability -= 1
    print("\t> ROD DURABILITY:\t", end="")
    if cur_durability > 0:
        print("[" + (cur_durability * "#") + ((max_durability - cur_durability) * "_")
              + "] (" + str(cur_durability) + "/" + str(max_durability) + ")")
    else:
        print("[!] (" + str(cur_durability) + "/" + str(max_durability) + ")")
    return cur_durability


def move_fish(pond, rows, cols):
    list_of_options = []
    moved_fish_spots = []
    fish_to_options = {}

    # calculate and make list of move options for each fish
    for fish_spot in pond.fish_spots:
        options = []
        # check left side
        if (fish_spot % cols) != 0:
            options.append(fish_spot-1)
        # check right side
        if (fish_spot+1 % cols) != 0:
            options.append(fish_spot+1)
        # check top
        if fish_spot+1 > cols:
            options.append(fish_spot - cols)
        # check bottom
        if fish_spot < (cols * (rows-1)):
            options.append(fish_spot + cols)
        # always add same spot to options
        options.append(fish_spot)
        list_of_options.append(options)
        fish_to_options[fish_spot] = options

        # print("move options for fish (" + str(fish) + "): ", end="")
        # print(options)

    # sort list of options shortest to longest to increase chances of move availability
    list_of_options.sort(key=len)

    for options in list_of_options:
        for key, value in fish_to_options.items():
            if value == options:
                cur_fish = key
        # choose a random spot from list of options
        choice = random.choice(options)
        # if spot already in the new fish spots, remove it and choose again
        while choice in moved_fish_spots and len(options) > 0:
            options.remove(choice)
            fish_to_options[cur_fish] = options
            if len(options) > 0:
                choice = random.choice(options)
        if len(options) > 0:
            moved_fish_spots.append(choice)
            for fish in pond.fish:
                print('fish.pos', fish.pos, 'cur_fish', cur_fish)
                if fish.pos == cur_fish:

                    fish.pos = choice

    pond.fish_spots = moved_fish_spots
    print(moved_fish_spots)
    print([fish.pos for fish in pond.fish])
