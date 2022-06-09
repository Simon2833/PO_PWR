import models
import random


# Board class where the simulation happens
class board:

    def __init__(self, cox, coy):
        self.__cox = cox
        self.__coy = coy

    # Here getting an empty 2D list
    def boardInit(self):
        tab = [[None] * self.__cox for _ in range(self.__coy)]
        return tab

    # All the starting objects are generated on the previously empty board
    def boardGenerate(self, tab, maxFood, maxMonster, maxTribes, initialpopulation):
        self.__tribeGenerate(tab, maxTribes, initialpopulation)
        self.__foodGenerate(tab, maxFood)
        self.__monsterGenerate(tab, maxMonster)
        for y in range(len(tab)):
            for x in range(len(tab[y])):
                if (tab[y][x] not in [1, 2, 3, 4, 5, 6]):
                    tab[y][x] = 0

        return tab

    # Function generates random coordinates and if the spot is empty makes new food object in food list with those coordinates
    def __foodGenerate(self, tab, maxFood):
        foodCount = 0
        while (foodCount != maxFood):
            pos = models.calc.randomPos(self.__cox, self.__coy)
            if (tab[pos[1]][pos[0]] not in [1, 2, 3, 4, 5, 6]):
                tab[pos[1]][pos[0]] = 1
                models.resource.resourceList.append(models.resource(pos[0], pos[1], len(models.resource.resourceList)))
                foodCount += 1

    # Function generates random coordinates and if the spot is empty makes new monster object in monster list with those coordinates
    def __monsterGenerate(self, tab, maxMonster):
        monsterCount = 0
        while (monsterCount != maxMonster):
            pos = models.calc.randomPos(self.__cox, self.__coy)
            if (tab[pos[1]][pos[0]] not in [1, 2, 3, 4, 5, 6]):
                tab[pos[1]][pos[0]] = 2
                models.monster.monsterList.append(models.monster(pos[0], pos[1], len(models.monster.monsterList)))
                monsterCount += 1

    # Function generates random coordinates and if the spot is empty makes new villageBase object in tribe list with those coordinates
    def __tribeGenerate(self, tab, maxTribes, initialpopulation):
        tribeCount = 0
        while (tribeCount != maxTribes):
            pos = models.calc.randomPos(self.__cox, self.__coy)
            if (tribeCount != 0):
                pos = self.__isNext(pos, tribeCount)
            if (tab[pos[1]][pos[0]] not in [1, 2, 3, 4, 5, 6]):
                tab[pos[1]][pos[0]] = 3
                models.villageBase.baseList.append(models.villageBase(pos[0], pos[1], len(models.villageBase.baseList), initialpopulation))
                self.__villagersGenerate(tab, models.villageBase.baseList[tribeCount].getPopulation(), tribeCount, pos[0], pos[1])
                tribeCount += 1

    # Function generates random coordinates and if the spot is empty makes new villager object in population list with those coordinates
    def __villagersGenerate(self, tab, maxPopulation, tribeCount, basex, basey):
        populationCount = 0
        baseShortcut = models.villageBase.baseList[tribeCount]
        while (populationCount != maxPopulation):
            pos = models.calc.randomPos(self.__cox, self.__coy)
            while(models.calc.rangeBetween(basex, basey, pos[0], pos[1]) >= 2):
                pos = models.calc.randomPos(self.__cox, self.__coy)
            vil = random.randint(1, 3)
            for i in range(1, 3):
                lenOfPopulationList = len(baseShortcut.populationList)
                if (tab[pos[1]][pos[0]] not in [1, 2, 3, 4, 5, 6] and vil == i):
                    match vil:
                        case 1:
                            populationCount += 1
                            tab[pos[1]][pos[0]] = 4
                            baseShortcut.populationList.append(models.warrior(pos[0], pos[1], lenOfPopulationList, baseShortcut.id))
                        case 2:
                            populationCount += 1
                            tab[pos[1]][pos[0]] = 5
                            baseShortcut.populationList.append(models.spearman(pos[0], pos[1], lenOfPopulationList, baseShortcut.id))
                        case 3:
                            populationCount += 1
                            tab[pos[1]][pos[0]] = 6
                            baseShortcut.populationList.append(models.archer(pos[0], pos[1], lenOfPopulationList, baseShortcut.id))
    
    # Checks if villageBase is enough far from other bases to not stack them next to each other
    def __isNext(self, pos, tribeCount):
        x = 0
        baseListShortcut = models.villageBase.baseList
        if(tribeCount == 1):
            if(models.calc.rangeBetween(baseListShortcut[tribeCount-1].cox, baseListShortcut[tribeCount-1].coy, pos[0], pos[1]) >= 3):
                return pos
        while (x != tribeCount):
            for i in range(1, tribeCount+1):
                if(models.calc.rangeBetween(baseListShortcut[tribeCount-i].cox, baseListShortcut[tribeCount-i].coy, pos[0], pos[1]) >= 3):
                    x = x + 1
            if(x != tribeCount):
                x = 0
                pos = models.calc.randomPos(self.__cox, self.__coy)
        return pos


