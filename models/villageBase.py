import random

from models.calc import calc
from models.unitStatic import unitStatic
import models


# Main village base that will delete clan if destroyed
class villageBase(unitStatic):

    baseList = []

    def __init__(self, cox, coy, id, initialpopulation, morale=50):
        super().__init__(cox, coy, id)
        self.status = "peace"
        self.maxhp = 100
        self.currenthp = 100
        self.__population = initialpopulation
        self.populationList = []
        self.morale = morale
        self.__attitude = calc.yesOrNo("passive", "aggressive")
        self.__colorId = self.id

    def getPopulation(self):
        return self.__population

    def getAttitude(self):
        return self.__attitude

    def getColorId(self):
        return self.__colorId

    def deletion(self, tribe, list, tab):
        # Refresh the id in baseList and transfer the rest of villagers to victorious tribe
        for villager in self.populationList:
            villager.id = len(tribe.populationList)
            tribe.populationList.append(villager)
        tab[self.coy][self.cox] = 0
        del list[self.id]
        for base in range(len(list)):
            list[base].id = base
            for villager in list[base].populationList:
                villager.tribe = list[base].id

    def moraleUpdate(self, tribe, list, tab):
        # morale can add new villager or delete one from beginning of list, can also destry base if last villager dies of hunger
        self.morale = self.morale - 1

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
            return

        if(self.morale > 0): return

        self.morale = 50
        self.populationList[0].deletion(tribe, list, tab)
        if(len(self.populationList) > 0): return

        for x in range(len(self.populationList)):
            del self.populationList[x]
        tab[self.coy][self.cox] = 0
        del list[self.id]
        for base in range(len(list)):
            list[base].id = base
            for villager in list[base].populationList:
                villager.tribe = list[base].id

    @classmethod
    def globalPeace(cls):
        # All out war because if they are in corners it's more fun to watch them go to each other
        for base in villageBase.baseList:
            base.status = "peace"

    @classmethod
    def globalWar(cls):
        # Early all out peace to reset war status witch at this time everyone has on
        for base in villageBase.baseList:
            base.status = "war"
