# Main village base that will delete clan if destroyed
class village_base:
    def __init__(self, maxhp, position, tribe):
        self.maxhp = maxhp
        self.currenthp = maxhp
        self.position = position
        self.tribe = tribe
