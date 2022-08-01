# Rod class


class Rod:
    def __init__(self, name, max_durability, resistance, deep_sea):
        self.name = name
        self.max_durability, self.cur_durability = max_durability
        self.resistance = resistance
        self.deep_sea = deep_sea
        self.bait = None

    def attach_bait(self, bait):
        # if bait on the rod already, store it in the bag
        if self.bait:
            # Bag.add(bait)
            pass
        # add bait to rod
        self.bait = bait

    def break_rod(self):
        self.cur_durability = 0
        print("[!] Your fishing rod broke!")
        del self

    def display_durability(self):
        print("[" + (self.cur_durability * "#") + ((self.max_durability - self.cur_durability) * "_")
                  + "] (" + str(self.cur_durability) + "/" + str(self.max_durability) + ")")

    def use_rod(self):
        self.cur_durability -= 1
        self.display_durability()
        if self.cur_durability <= 0:
            self.break_rod()

    def display_info(self):
        print(self.name)
        print("\t" + str(self.resistance) + " resistance")
        print("\tDurability: " + str(self.cur_durability) + "/" + str(self.max_durability))
        if self.deep_sea:
            print("\tDeep sea: Yes")
        else:
            print("\tDeep sea: No")
