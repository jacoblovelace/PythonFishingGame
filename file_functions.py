import pickle
import sys

from Save_File_Class import *


def prompt_quit():
    confirm_quit = 'y'
    while confirm_quit != 'n':
        confirm_quit = input("Are you sure you want to quit? [y/n]: ")
        if confirm_quit == 'y':
            print("See you soon...")
            sys.exit()
        elif confirm_quit != 'n':
            print("[!] invalid option\n")


def prompt_delete_file():
    confirm_delete = 'y'
    while confirm_delete != 'n':
        confirm_delete = input("Are you sure you want to delete this file? [y/n]: ")
        if confirm_delete == 'y':
            return True
        elif confirm_delete != 'n':
            print("[!] invalid option\n")
    return False


def save_the_save_files(save_files):
    with open('savefiledata.dat', 'wb') as f:
        pickle.dump(save_files, f)


def load_the_save_files():
    with open('savefiledata.dat', 'rb') as f:
        save_file_data = pickle.load(f)
    return save_file_data


def delete_file(save_files, file):
    file.delete()
    save_the_save_files(save_files)


def display_options_from_list(lst):
    for i in range(0, len(lst)):
        print("[" + str(i + 1) + "] - " + lst[i])
    print("")


def choose_file():
    print("\n||| " + ("-" * 25) + " FILE SELECT " + ("-" * 25) + " |||")
    print("Enter 1, 2, or 3 to select or create a new save file below: (press 'q' to quit)\n")

    # load save files and display them
    save_list = load_the_save_files()
    for i in range(0, len(save_list)):
        if save_list[i].exists:
            print("[" + str(i+1) + "] - " + str(save_list[i].name))
        else:
            print("[" + str(i + 1) + "] - {empty}")
    print("")

    # get user input to select a file
    while True:
        file_select_num = input("Enter a file number: ")

        if file_select_num == 'q':
            prompt_quit()
        else:
            if (file_select_num.isdigit()) and (1 <= int(file_select_num) <= 3):
                break
            else:
                print("[!] invalid option\n")

    # grab file from list of saves
    print("Loading save file [" + str(file_select_num) + "]...")
    file = save_list[int(file_select_num) - 1]

    # set index attribute of file
    file.set_index(file_select_num)

    return file, save_list


def check_if_file_exists(file):
    if file.exists:
        return True
    return False


def create_new_file(file, save_list):

    # create new file with inputted name
    create_file_invalid = True
    while create_file_invalid:
        create_file = input("No save data for this file. Would you like to create a new file? [y/n]: ")
        if create_file == 'y':

            # set exists flag, index, and name
            file_name = input("Enter a name for the save file: ")
            file.set_exists(True)
            file.set_name(file_name)

            # save updated file back to save file data
            save_the_save_files(save_list)

            # file created, so return True
            return True

        elif create_file != 'n':
            print("[!] invalid option\n")

        return False


def file_options(file, save_list):

    print("Select an action below:\n")
    file_actions = ["Play", "Delete", "Go Back"]
    display_options_from_list(file_actions)

    while True:
        action_select_num = input("Enter an option number: ")
        if (action_select_num.isdigit()) and (1 <= int(action_select_num) <= 3):
            if action_select_num == '1':
                print("Now playing as save file '" + file.name + "'")
                return True
            elif action_select_num == '2':
                if prompt_delete_file():
                    print("Deleting save file '" + str(file.name) + "'")
                    delete_file(save_list, file)
                return False
            else:
                return False
        else:
            print("[!] invalid option\n")
