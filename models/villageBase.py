from models.calc import calc
from models.unitStatic import unitStatic


# Main village base that will delete clan if destroyed
class villageBase(unitStatic):

    x = calc.yesOrNo("pasive", "aggressive")
    baseList = []

    def __init__(self, cox, coy, id, morale=50):
        super().__init__(cox, coy, id)
        self.food = 50
        self.status = "peace"
        self.maxhp = 100
        self.currenthp = 100
        self.population = 3
        self.populationList = []
        self.morale = morale
        self.attitude = self.x
        self.job = "base"

    def deletion(self, tribe, list, tab):
        for villager in self.populationList:
            villager.id = len(tribe.populationList)
            tribe.populationList.append(villager)
        tab[self.coy][self.cox] = 0
        del list[self.id]
        for base in range(len(list)):
            list[base].id = base
