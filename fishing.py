import random


def place_fish(pond_size):
    # generate random number of fish, no more than 1/3 pond size
    num_fish = random.randrange(1, (pond_size // 3) + 1)

    # assign each fish a unique number representing its starting location in the pond
    fish_spots = random.sample(range(0, pond_size), num_fish)

    # print("num_fish:", num_fish)
    # print(fish_spots)

    return fish_spots


def do_fish(fish_spots, rows, cols, max_durability, cur_durability):
    display_pond(rows, cols)

    get_spot = input(">>> enter spot: ")

    r = ord(get_spot[0]) - 65
    c = int(get_spot[1]) - 1
    spot = (cols * r) + c

    fish_found = False
    for fish in fish_spots:
        if spot == fish:
            print("\t\x1B[3mYou caught a fish!\x1B[0m")
            fish_spots.remove(fish)
            fish_found = True
            break
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


def move_fish(fish_spots, rows, cols):
    list_of_options = []
    moved_fish_spots = []

    # calculate and make list of move options for each fish
    for fish in fish_spots:
        options = []
        # check left side
        if (fish % cols) != 0:
            options.append(fish-1)
        # check right side
        if (fish+1 % cols) != 0:
            options.append(fish+1)
        # check top
        if fish+1 > cols:
            options.append(fish - cols)
        # check bottom
        if fish < (cols * (rows-1)):
            options.append(fish + cols)
        # always add same spot to options
        options.append(fish)
        list_of_options.append(options)

        # print("move options for fish (" + str(fish) + "): ", end="")
        # print(options)

    # sort list of options shortest to longest to increase chances of move availability
    list_of_options.sort(key=len)

    for options in list_of_options:
        choice = random.choice(options)
        while choice in moved_fish_spots:
            options.remove(choice)
            if len(options) > 0:
                choice = random.choice(options)
            else:
                break
        if len(options) > 0:
            moved_fish_spots.append(choice)

    print(moved_fish_spots)

    # return moved_fish_spots
    return moved_fish_spots


def generate_pond():
    pond_spots = []
    rows = int(input("Rows: "))
    cols = int(input("Columns: "))

    # generate pond
    pond_size = rows * cols
    for r in range(rows):
        pond_row = []
        for c in range(cols):
            pond_row.append(c)
        pond_spots.append(pond_row)

    # generate random num of fish (no more than half of pond)
    fish_spots = place_fish(pond_size)

    return pond_spots, fish_spots, rows, cols


def display_pond(rows, cols):
    print("\n||| " + ("-" * 25) + " THE POND " + ("-" * 25) + " |||")
    for r in range(rows):
        for c in range(cols):
            row_letter = chr(ord('@')+(r+1))
            spot = str(row_letter) + str(c+1)
            print("| " + str(spot), end=" ")
        print("|")
