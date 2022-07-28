import random
import sys


def generate_game_objects():
    global BOARD_SIZE, NUM_BARRIERS
    obj_list = []
    while len(obj_list) < NUM_BARRIERS:
        rand = (random.randrange(0, BOARD_SIZE), random.randrange(0, BOARD_SIZE))
        if rand not in obj_list:
            obj_list.append(rand)

    return obj_list


def generate_gameboard():
    global SPRITES
    board = [[SPRITES['space'] for _ in range(0, BOARD_SIZE)] for _ in range(0, BOARD_SIZE)]

    objects = generate_game_objects()

    # create barriers list from objects list
    barriers = []
    for i in range(2, len(objects)):
        barriers.append(objects[i])
        board[objects[i][1]][objects[i][0]] = SPRITES['barrier']

    # player is first object
    player_pos = objects[0]
    player_x, player_y = player_pos
    board[player_y][player_x] = SPRITES['player']

    # goal is second object
    goal_pos = objects[1]
    goal_x, goal_y = goal_pos
    board[goal_y][goal_x] = SPRITES['goal']

    return board, barriers, player_pos, goal_pos


def check_move_availability(barriers, player_pos):
    global BOARD_SIZE
    player_col, player_row = player_pos

    available_moves = []
    # check left side
    if player_col > 0:
        if not (player_col - 1, player_row) in barriers:
            available_moves.append('a')
    # check right side
    if player_col < BOARD_SIZE - 1:
        if not (player_col + 1, player_row) in barriers:
            available_moves.append('d')
    # check top
    if player_row > 0:
        if not (player_col, player_row - 1) in barriers:
            available_moves.append('w')
    # check bottom
    if player_row < BOARD_SIZE - 1:
        if not (player_col, player_row + 1) in barriers:
            available_moves.append('s')

    return available_moves


def display_gameboard(board):
    global BOARD_SIZE

    # sys.stdout.write(' ')
    # sys.stdout.write('⎽⎽' * ((2 * BOARD_SIZE) + 1) + '\n')
    # for row in board:
    #     sys.stdout.write('╫ ')
    #     for char in row:
    #         sys.stdout.write(char + ' ')
    #     sys.stdout.write('╫' + '\n')
    # sys.stdout.write('⎺⎺' * ((2 * BOARD_SIZE) + 1) + '\n')

    print(' ', end='')
    print('⎽⎽' * ((2 * BOARD_SIZE) + 1))
    for row in board:
        print('╫ ', end='')
        for char in row:
            print(char, end=' ')
        print('╫')
    print(' ', end='')
    print('⎺⎺' * ((2 * BOARD_SIZE) + 1))


def get_input(valid_moves):
    global KEY_OPTIONS

    while True:
        key = input("Enter direction [ASDW]: ")
        key = key.lower()

        if key in KEY_OPTIONS and key in valid_moves:
            return key
        else:
            print('[!] Invalid Move')


def determine_goal_search(barriers, player_pos, goal_pos, direction):
    global BOARD_SIZE
    player_x, player_y = player_pos

    if direction == 'a':
        res = search_for_goal(goal_pos, barriers, player_x - 1, 0 - 1, -1, 'i', player_y)
    elif direction == 'd':
        res = search_for_goal(goal_pos, barriers, player_x + 1, BOARD_SIZE, 1, 'i', player_y)
    elif direction == 'w':
        res = search_for_goal(goal_pos, barriers, player_y - 1, 0 - 1, -1, player_x, 'i')
    else:
        res = search_for_goal(goal_pos, barriers, player_y + 1, BOARD_SIZE, 1, player_x, 'i')

    return res


def search_for_goal(goal_pos, barriers, start, end, step, a, b):
    ai = False
    bi = False
    if a == 'i':
        ai = True
    if b == 'i':
        bi = True

    for i in range(start, end, step):
        if ai:
            a = i
        if bi:
            b = i

        if a == goal_pos[0] and b == goal_pos[1]:
            return True
        for barrier in barriers:
            if a == barrier[0] and b == barrier[1]:
                return False

    return False


def determine_barrier_search(barriers, player_pos, direction):
    global BOARD_SIZE
    player_x, player_y = player_pos

    if direction == 'a':
        res = search_for_closest_barrier(barriers, player_x - 1, 0 - 1, -1, 'i', player_y)
    elif direction == 'd':
        res = search_for_closest_barrier(barriers, player_x + 1, BOARD_SIZE, 1, 'i', player_y)
    elif direction == 'w':
        res = search_for_closest_barrier(barriers, player_y - 1, 0 - 1, -1, player_x, 'i')
    else:
        res = search_for_closest_barrier(barriers, player_y + 1, BOARD_SIZE, 1, player_x, 'i')

    return res


def search_for_closest_barrier(barriers, start, end, step, a, b):
    ai, bi = False
    if a == 'i':
        ai = True
    if b == 'i':
        bi = True

    for i in range(start, end, step):
        if ai:
            a = i
        if bi:
            b = i

        for barrier in barriers:
            if a == barrier[0] and b == barrier[1]:
                return barrier
    return False


def get_new_player_pos(direction, player_pos):
    if direction == 'a':
        player_pos = (0, player_pos[1])
    elif direction == 'd':
        player_pos = (BOARD_SIZE-1, player_pos[1])
    elif direction == 'w':
        player_pos = (player_pos[0], 0)
    else:
        player_pos = (player_pos[0], BOARD_SIZE-1)
    return player_pos


def get_new_player_pos_with_barriers(direction, player_pos, barrier_pos):

    if direction == 'a':
        player_pos = (barrier_pos[0] + 1, player_pos[1])
    elif direction == 'd':
        player_pos = (barrier_pos[0] - 1, player_pos[1])
    elif direction == 'w':
        player_pos = (player_pos[0], barrier_pos[1] + 1)
    else:
        player_pos = (player_pos[0], barrier_pos[1] - 1)

    return player_pos


def update_board(board, barriers, direction, player_pos):

    # loop through directional line given player_pos and direction
    # find closest barrier
    # set player_pos as neighbor depending on direction

    # set previous player position to empty spot
    board[player_pos[1]][player_pos[0]] = SPRITES['space']

    # if no barriers in the way, put player on a wall
    if not determine_barrier_search(barriers, player_pos, direction):
        player_pos = get_new_player_pos(direction, player_pos)
    # else, put player next to closest barrier depending on direction
    else:
        closest_barrier = determine_barrier_search(barriers, player_pos, direction)
        player_pos = get_new_player_pos_with_barriers(direction, player_pos, closest_barrier)

    board[player_pos[1]][player_pos[0]] = SPRITES['player']

    return board, player_pos


def update_board_for_win(board, player_pos, goal_pos):
    board[player_pos[1]][player_pos[0]] = SPRITES['space']
    board[goal_pos[1]][goal_pos[0]] = SPRITES['player']

    return board


def win_message():
    print("\n" + "*" * 10 + " YOU WIN " + "*" * 10 + "\n")


game_running = True
KEY_OPTIONS = ['a', 's', 'd', 'w']
SPRITES = {'space': ' ',
           'player': '◯',
           'barrier': '▣',
           'goal': 'G'
           }
BOARD_SIZE = 4
NUM_BARRIERS = 25

# generate gameboard
gameboard, barriers, player_pos, goal_pos = generate_gameboard()

# display gameboard
display_gameboard(gameboard)

while game_running:
    # get move availability
    # -> barriers, player_pos
    available_moves = check_move_availability(barriers, player_pos)

    # get keyboard input
    # -> available_moves
    direction = get_input(available_moves)

    # check win condition
    # -> barriers, player_pos, goal_pos, direction
    if not determine_goal_search(barriers, player_pos, goal_pos, direction):
        # update board list
        # -> board, direction
        gameboard, player_pos = update_board(gameboard, barriers, direction, player_pos)
    else:
        win_message()
        gameboard = update_board_for_win(gameboard, player_pos, goal_pos)
        game_running = False

    # display board
    display_gameboard(gameboard)
