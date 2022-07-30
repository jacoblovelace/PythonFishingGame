import random


def do_fish(pond, max_durability, cur_durability, bucket):
    pond.display_pond()

    while True:
        spot_input = input(">>> enter spot (press 'q' to leave pond): ")
        if spot_input == 'q':
            confirm_quit = 'y'
            while confirm_quit != 'n':
                confirm_quit = input("Are you sure you want to leave this fishing location? [y/n]: ")
                if confirm_quit == 'y':
                    cur_durability = 0
                    return cur_durability
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
                    cur_durability = 0
                    return cur_durability
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


def move_fish(pond):
    list_of_options = []
    updated_fish_spots = []

    # calculate and make list of move options for each fish
    for fish_spot in pond.fish_spots:
        # initialize list with fish object as first element
        options = [pond.board[fish_spot]]
        # check left side
        if (fish_spot % pond.x) != 0:
            options.append(fish_spot-1)
        # check right side
        if ((fish_spot+1) % pond.x) != 0:
            options.append(fish_spot+1)
        # check top
        if fish_spot+1 > pond.x:
            options.append(fish_spot - pond.x)
        # check bottom
        if fish_spot < (pond.x * (pond.y-1)):
            options.append(fish_spot + pond.x)
        # always add same spot to options
        options.append(fish_spot)
        list_of_options.append(options)

    # sort list of options shortest to longest to increase chances of move availability
    list_of_options.sort(key=len)

    for options in list_of_options:
        # choose a random spot from list of options
        cur_fish = options[0]
        options = options[1:]
        choice = random.choice(options)
        # if spot already in the new fish spots, remove it and choose again
        while choice in updated_fish_spots and len(options) > 0:
            options.remove(choice)
            if len(options) > 0:
                choice = random.choice(options)
        if len(options) > 0:
            updated_fish_spots.append(choice)
            cur_fish.pos = choice

    pond.board = [i for i in range(pond.x * pond.y)]
    for fish in pond.fish:
        pond.board[fish.pos] = fish
    pond.fish_spots = updated_fish_spots
