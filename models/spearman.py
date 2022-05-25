from models.unitDynamic import unitDynamic


# One of three tribe classes which will be concluded in simulation
class spearman(unitDynamic):

    def __init__(self, cox, coy, id, tribe, maxhp=150, armor=3, range=2, attack=2):
        super().__init__(cox, coy, id, maxhp, attack, armor, range)
        self.currenthp = maxhp
        self.tribe = tribe
        self.type = "villager"
        self.job = "spearman"

    def deletion(self, tribe, list, tab):
        tab[self.coy][self.cox] = 0
        del list[self.tribe].populationList[self.id]
        for villager in range(len(list[self.tribe].populationList[self.id])):
            list[self.tribe].populationList[villager].id = villager
            print(list[self.tribe].populationList[villager].id)
