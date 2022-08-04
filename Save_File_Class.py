# Save_File class

class Save_File:
    def __init__(self, name=None):
        self.exists = False
        self.index = 0
        self.name = name
        self.equipped_rod = None

    def delete(self):
        self.exists = False
        self.index = 0
        self.name = None
        self.equipped_rod = None
