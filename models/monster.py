# Independent animal which is stronger than normal unit but can offer quality goods
class monster:

    # List of monsters used in board class to store objects in their categories
    monsterList = []

    def __init__(self, maxhp, attack, armor, range, loot, cox, coy):
        self.id = len(self.monsterList)
        self.maxhp = maxhp
        self.currenthp = maxhp
        self.attack = attack
        self.armor = armor
        self.range = range
        self.loot = loot
        self.cox = cox
        self.coy = coy
        self.type = "monster"
