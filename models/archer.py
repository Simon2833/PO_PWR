from models.unitDynamic import unitDynamic


# One of three tribe classes which will be concluded in simulation
class archer(unitDynamic):

    def __init__(self, cox, coy, id, tribe, maxhp=100, attack=15, armor=0, range=5):
        super().__init__(cox, coy, id, maxhp, attack, armor, range)
        self.tribe = tribe
        self.type = "villager"

    def deletion(self, tribe, list, tab):
        tab[self.coy][self.cox] = 0
        list[self.tribe].morale = list[self.tribe].morale - 10
        del list[self.tribe].populationList[self.id]
        for villager in range(len(list[self.tribe].populationList)):
            list[self.tribe].populationList[villager].id = villager
