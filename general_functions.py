# general game functions

def title_display(title):
    num_dashes = 50 - len(title)
    print("\n||| " + ("-" * (num_dashes//2)) + " " + title.upper() + " " + ("-" * (num_dashes//2)) + " |||")


def display_options_from_list(lst):
    print("")
    for i in range(0, len(lst)):
        print("[" + str(i + 1) + "] - " + lst[i])
    print("")
