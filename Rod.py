# Rod class
from abc import ABC
from Item import Item


class Rod(Item, ABC):

    def __init__(self, name, value, max_durability, resistance, deep_sea, bait=None):
        super().__init__()
        if name == 1:
            name = "Cheap Rod"
        self.name = name
        self.value = value
        self.max_durability = max_durability
        self.cur_durability = max_durability
        self.resistance = resistance
        self.deep_sea = deep_sea
        self.bait = bait

    def detach_bait(self):
        # Bag.add(self.bait)
        self.bait = None

    def attach_bait(self, bait):
        # if bait on the rod already, store it in the bag
        if self.bait:
            self.detach_bait()
        # add bait to rod
        self.bait = bait

    def break_rod(self):
        self.cur_durability = 0
        print("[!] Your fishing rod broke!")
        self.exists = False
        del self

    def display_durability(self):
        print("(" + str(self.cur_durability) + "/" + str(self.max_durability) + ")")

    def decrease_duraility(self):
        self.cur_durability -= 1

    def display_stats(self):
        bait_display = "{None}"
        if self.bait:
            bait_display = self.bait.to_string()
        print(self.to_string() + " | Bait: " + bait_display + " | Durability: ", end="")
        self.display_durability()

    def use(self, save_obj, pond):
        if save_obj.equipped_rod is not None:
            save_obj.bag.add_item(save_obj.equipped_rod)
        save_obj.equipped_rod = self
        return True

    def display_info(self):
        print(self.name)
        print("\tDurability: " + str(self.cur_durability) + "/" + str(self.max_durability))
        print("\tResistance: " + str(self.resistance))
        if self.deep_sea:
            print("\tDeep sea: Yes")
        else:
            print("\tDeep sea: No")

    def display_info_shop(self):
        print("")
        print(self.name)
        print("\tCost: " + str(self.value) + " coins")
        print("\tDurability: " + str(self.max_durability))
        print("\tResistance: " + str(self.resistance))
        if self.deep_sea:
            print("\tDeep sea: Yes")
        else:
            print("\tDeep sea: No")
    
    def get_constructor_string(self):
        return f"Rod('{self.name}', {self.value}, {self.max_durability}, {self.cur_durability}, {self.deep_sea}, {self.bait})"
