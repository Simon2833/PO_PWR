#villag_base class
class village_base:
    def __init__(self, maxhp, position, tribe):
        self.maxhp = maxhp
        self.currenthp = maxhp
        self.position = position
        self.tribe = tribe
