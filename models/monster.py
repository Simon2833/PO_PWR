#monster class----
class monster:
    def __init__(self, name, maxhp, attack, armor, range, loot, position):
        self.name = name
        self.maxhp = maxhp
        self.currenthp = maxhp
        self.attack = attack
        self.armor = armor
        self.range = range
        self.loot = loot
        self.position = position
