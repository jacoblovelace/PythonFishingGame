# Save_File class

class Save_File:
    def __init__(self, name=None, score=0):
        self.exists = False
        self.index = 0
        self.name = name
        self.score = score

    def delete(self):
        self.exists = False
        self.index = 0
        self.name = None
        self.score = 0

    def set_exists(self, exists):
        self.exists = exists

    def set_index(self, index):
        self.index = index

    def set_name(self, name):
        self.name = name

    def set_score(self, score):
        self.score = score
