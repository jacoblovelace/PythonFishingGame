import pickle
import sys

from general_functions import *
from Save_File_Class import *


def choose_file():
    while True:
        title_display("file select")
        print(">>> (press 'q' to quit) Enter 1, 2, or 3 to select or create a new save file below: \n")
        file_list = ["savefile1.txt", "savefile2.txt", "savefile3.txt"]
    # load save files and display them
        save_names = []
        exists_list = []
        for i in range(len(file_list)):
            with open(file_list[i], "r") as file:
                lines = file.readlines()
            if lines[0].strip() == "True":
                exists_list.append(1)
                print("[" + str(i+1) + "] - " + str(lines[1]).strip())
            else:
                exists_list.append(0)
                print("[" + str(i + 1) + "] - {empty}")
        print("")

        # get user input to select a file
        while True:
            file_select_num = input(">>> Enter a file number: ")

            if file_select_num == 'q':
                prompt_quit()
            else:
                if (file_select_num.isdigit()) and (1 <= int(file_select_num) <= 3):
                    break
                else:
                    print("[!] invalid option\n")
        file_select_num = int(file_select_num)
        if not exists_list[file_select_num - 1]:
            if create_new_file(file_list[file_select_num - 1]):
                break
        else:
            break

    # grab file from list of saves
    print("Loading save file [" + str(file_select_num) + "]...\n")
    with open(file_list[file_select_num - 1], "r") as file:
        lines = file.readlines()

    file = Save_File(file_list[file_select_num - 1], lines)

    return file


def create_new_file(file_name):

    # create new file with inputted name
    while True:
        create_file = input(">>> No save data for this file. Would you like to create a new file? [y/n]: ")
        if create_file == 'y':

            # set exists flag, index, and name
            save_name = input(">>> Enter a name for the save file: ")
            with open(file_name, "w") as file:
                values = [True, save_name, [10, ["Rod(\"Cheap Rod\", 10, 5, 0.0, False)"]], [5, []], 100, [0, 0]]
                for value in values:
                    file.write(str(value) + '\n')

            # file created, so return True
            return True

        elif create_file != 'n':
            print("[!] invalid option\n")

        return False


def file_options(file):

    print("> Select an action below:")
    file_actions = ["Play", "Delete", "Go Back"]
    display_options_from_list(file_actions)

    while True:
        num = input(">>> Enter an option number: ")
        if (num.isdigit()) and (1 <= int(num) <= 3):
            if num == '1':
                print("> Now playing as save file '" + file.name + "'")
                return True
            elif num == '2':
                if prompt_delete_file():
                    print("> Deleting save file '" + file.name + "'")
                    file.delete()
                return False
            else:
                return False
        else:
            print("[!] invalid option\n")


def prompt_quit():
    confirm_quit = 'y'
    while confirm_quit != 'n':
        confirm_quit = input(">>> Are you sure you want to quit? [y/n]: ")
        if confirm_quit == 'y':
            print("\x1B[1m\x1B[3mSee you soon...\x1B[0m")
            sys.exit()
        elif confirm_quit != 'n':
            print("[!] invalid option\n")


def prompt_delete_file():
    confirm_delete = 'y'
    while confirm_delete != 'n':
        confirm_delete = input(">>> Are you sure you want to delete this file? [y/n]: ")
        if confirm_delete == 'y':
            return True
        elif confirm_delete != 'n':
            print("[!] invalid option\n")
    return False


def save(save):
    with open(save.file_name, "w") as file:
        # file.writeline("True")
        # file.writeline(save.name)
        bag = [save.bag.capacity, [item.get_constructor_string() for item in save.bag.contents]]
        # file.writeline(str(bag))
        bucket = [save.bucket.capacity, [item.get_constructor_string() for item in save.bucket.contents]]
        # file.writeline(str(bucket))
        # file.writeline(str(save.coins))
        lines = ["True", save.name, str(bag), str(bucket), str(save.coins), str(save.level)]
        for line in lines:
            file.write(line + "\n")
