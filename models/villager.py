#basic villager class
class villager:
    def __init__(self, name, maxhp, armor, tribe, attack, morale):
        self.name = name
        self.maxhp = maxhp
        self.currenthp = maxhp
        self.armor = armor
        self.tribe = tribe
        self.attack = attack
        self.morale = morale
