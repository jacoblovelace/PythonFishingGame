# Level system class

from ponds import PONDS
import math


class Level_System:
    def __init__(self, xp=0, level=1):
        self.xp = xp
        self.level = level
        self.xp_cap = int((self.level*20)**1.3)
        self.unlocked_ponds = [pond for pond in PONDS if self.level >= pond.level]
        self.ui = "LEVEL: " + str(self.level) + " | XP: " + str(self.xp) + " / " + str(self.xp_cap)

    def check_level_to_update(self):
        while self.xp >= self.xp_cap:
            # set xp to remainer xp after reaching cap
            self.xp = self.xp - self.xp_cap
            # increment level and update to next level xp cap
            self.level += 1
            self.xp_cap = int(math.sqrt(self.level * 100) * 10)
            print(" > LEVEL UP! " + str(self.level-1) + " -> " + str(self.level))

            self.unlock_next_pond()

    def add_xp(self, fish, catch):
        if catch:
            xp_to_add = fish.LEVEL * 5
        else:
            xp_to_add = fish.LEVEL * fish.size_num + (500//fish.NORMALITY)

        print("\t\x1B[3m+ " + str(xp_to_add) + " XP!\x1B[0m")

        self.xp += xp_to_add
        self.check_level_to_update()
        self.ui = "LEVEL: " + str(self.level) + " | XP: " + str(self.xp) + " / " + str(self.xp_cap)

    def unlock_next_pond(self):
        # append to list of unlocked ponds the next index in PONDS
        if len(self.unlocked_ponds) < len(PONDS):
            if self.level >= PONDS[len(self.unlocked_ponds)].level:
                self.unlocked_ponds.append(PONDS[len(self.unlocked_ponds)])
                print(" > Unlocked a new fishing location: " + self.unlocked_ponds[-1].name)
