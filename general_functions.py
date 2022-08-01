# general game functions

def title_display(title):
    print("\n||| " + ("-" * 25) + title.upper() + ("-" * 25) + " |||")


def display_options_from_list(lst):
    print("")
    for i in range(0, len(lst)):
        print("[" + str(i + 1) + "] - " + lst[i])
    print("")
