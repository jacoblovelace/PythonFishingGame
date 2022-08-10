# Save_File class
from Bag import *
from Bucket_Class import *
from Level_System import Level_System


class Save_File:
    def __init__(self, file_name, atts):
        self.file_name = file_name
        self.exists = atts[0]
        self.name = atts[1].strip()
        atts[2] = eval(atts[2])
        self.bag = Bag(atts[2][0], [eval(atts[2][1][i]) for i in range(len(atts[2][1]))])
        atts[3] = eval(atts[3])
        self.bucket = Fishing_Bucket(atts[3][0], [eval(atts[3][1][i]) for i in range(len(atts[3][1]))])
        self.coins = int(atts[4])
        atts[5] = eval(atts[5])
        self.level_system = Level_System(int(atts[5][0]), int(atts[5][1]))
        self.equipped_rod = None

    def delete(self):
        with open(self.file_name, "w") as file:
            file.write("False")

    def display_stats(self):
        print(f"{self.level_system.ui} || COINS: {self.coins}"
)
