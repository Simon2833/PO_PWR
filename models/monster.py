from models.unitDynamic import unitDynamic


# Independent animal which is stronger than normal unit but can offer quality goods
class monster(unitDynamic):

    # List of monsters used in board class to store objects in their categories
    monsterList = []

    def __init__(self, cox, coy, id, loot="bussinLoot", maxhp=100, attack=10, armor=10, range=1):
        super().__init__(cox, coy, id, maxhp, attack, armor, range)
        self.currenthp = maxhp
        self.loot = loot
        self.type = "monster"
        self.tribe = "None"
        self.job = "monster"

    def deletion(self, tribe, list, tab):
        tab[self.coy][self.cox] = 0
        del list[self.id]
        for monster in range(len(list)):
            list[monster].id = monster
        tribe.morale = tribe.morale + 10
