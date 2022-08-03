# Rod class
from Item import Item


class Rod(Item):

    def __init__(self, name, max_durability, resistance, deep_sea):
        super().__init__()
        self.name = name
        self.max_durability = max_durability
        self.cur_durability = max_durability
        self.resistance = resistance
        self.deep_sea = deep_sea
        self.bait = None
        self.exists = True

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
        print("[" + (self.cur_durability * "#") + ((self.max_durability - self.cur_durability) * "_")
                  + "] (" + str(self.cur_durability) + "/" + str(self.max_durability) + ")")

    def decrease_duraility(self):
        self.cur_durability -= 1
        if self.cur_durability <= 0:
            self.break_rod()

    def display_stats(self):
        bait_display = "{None}"
        if self.bait:
            bait_display = self.bait.to_string()
        print(self.to_string() + " | Bait: " + bait_display + " | Durability: ", end="")
        self.display_durability()

    # method that overrides abstract "use" method in item class
    def use(self):
        # this method equips a fishing rod
        pass

    def display_info(self):
        print(self.name)
        print("\t" + str(self.resistance) + " resistance")
        print("\tDurability: " + str(self.cur_durability) + "/" + str(self.max_durability))
        if self.deep_sea:
            print("\tDeep sea: Yes")
        else:
            print("\tDeep sea: No")
