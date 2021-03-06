from models.unitDynamic import unitDynamic


# Independent animal which is stronger than normal unit but can offer quality goods
class monster(unitDynamic):

    # List of monsters used in board class to store objects in their categories
    monsterList = []

    def __init__(self, cox, coy, id, maxhp=100, attack=10, armor=10, range=2):
        super().__init__(cox, coy, id, maxhp, attack, armor, range)
        self.tribe = "None"

    def deletion(self, tribe, list, tab):
        tab[self.coy][self.cox] = 0
        del list[self.id]
        for monster in range(len(list)):
            list[monster].id = monster
        tribe.morale = tribe.morale + 10
