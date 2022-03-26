# Basic villager class from whom every other citizen class is inherited
class villager:
    def __init__(self, name, maxhp, armor, tribe, attack, morale, range, position):
        self.name = name
        self.maxhp = maxhp
        self.currenthp = maxhp
        self.armor = armor
        self.tribe = tribe
        self.attack = attack
        self.morale = morale
        self.range = range
        self.position = position
