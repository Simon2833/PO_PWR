import random

from models.calc import calc
from models.unitStatic import unitStatic
import models


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
            for villager in list[base].populationList:
                villager.tribe = list[base].id

    def moraleReset(self, tab):
        if(self.morale >= 100):
            self.morale = 50
            vil = random.randint(1, 3)
            pos = models.calc.randomPos(len(tab[0]), len(tab))
            while(models.calc.rangeBetween(self.cox, self.coy, pos[0], pos[1]) >= 2 and tab[pos[1]][pos[0]] not in [1, 2, 3, 4, 5, 6]):
                pos = models.calc.randomPos(len(tab[0]), len(tab))
            match vil:
                case 1:
                    tab[pos[1]][pos[0]] = 4
                    self.populationList.append(models.warrior(pos[0], pos[1], len(self.populationList), self.id))
                case 2:
                    tab[pos[1]][pos[0]] = 5
                    self.populationList.append(models.spearman(pos[0], pos[1], len(self.populationList), self.id))
                case 3:
                    tab[pos[1]][pos[0]] = 6
                    self.populationList.append(models.archer(pos[0], pos[1], len(self.populationList), self.id))
