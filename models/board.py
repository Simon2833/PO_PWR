import models
import random


# Board class where the simulation happens
class board:

    def __init__(self, cox, coy):
        self.cox = cox
        self.coy = coy

    # Here getting an empty 2D list
    def boardInit(self):
        tab = [[None] * self.cox for _ in range(self.coy)]
        return tab

    # Function generates random coordinates and if the spot is empty makes new food object in food list with those coordinates
    def foodGenerate(self, tab, maxFood):
        foodCount = 0
        while (foodCount != maxFood):
            pos = models.calc.randomPos(self.cox, self.coy)
            if (tab[pos[1]][pos[0]] not in [1, 2, 3, 4, 5, 6]):
                tab[pos[1]][pos[0]] = 1
                models.resource.foodList.append(models.resource(pos[1], pos[0]))
                foodCount += 1

    # Function generates random coordinates and if the spot is empty makes new monster object in monster list with those coordinates
    def monsterGenerate(self, tab, maxMonster):
        monsterCount = 0
        while (monsterCount != maxMonster):
            pos = models.calc.randomPos(self.cox, self.coy)
            if (tab[pos[1]][pos[0]] not in [1, 2, 3, 4, 5, 6]):
                tab[pos[1]][pos[0]] = 2
                models.monster.monsterList.append(models.monster("wiesio", 100, 10, 10, 1, "food", pos[1], pos[0]))
                monsterCount += 1

    def villagersGenerate(self, tab, maxPopulation, tribeCount, basex, basey):
        populationCount = 0
        listShortcut = models.village_base.baseList[tribeCount].populationList
        while (populationCount != maxPopulation):
            pos = models.calc.randomPos(self.cox, self.coy)
            while(models.calc.range(basex, basey, pos[0], pos[1]) >= 2):
                pos = models.calc.randomPos(self.cox, self.coy)
            vil = random.randint(1, 3)
            for i in range(1, 3):
                if (tab[pos[1]][pos[0]] not in [1, 2, 3, 4, 5, 6] and vil == i):
                    if vil == 1:
                        populationCount += 1
                        tab[pos[1]][pos[0]] = 4
                        listShortcut.append(models.warrior(models.village_base.baseList[tribeCount].id, pos[0], pos[1]))
                    elif vil == 2:
                        populationCount += 1
                        tab[pos[1]][pos[0]] = 5
                        listShortcut.append(models.spearman(models.village_base.baseList[tribeCount].id, pos[0], pos[1]))
                    elif vil == 3:
                        populationCount += 1
                        tab[pos[1]][pos[0]] = 6
                        listShortcut.append(models.archer(models.village_base.baseList[tribeCount].id, pos[0], pos[1]))

    def isNext(self, pos, tribeCount):
        x = 0
        if(tribeCount == 1):
            if(models.calc.range(models.village_base.baseList[tribeCount-1].cox, models.village_base.baseList[tribeCount-1].coy, pos[0], pos[1]) >= 3):
                return pos
        while (x != tribeCount):
            for i in range(1, tribeCount+1):
                if(models.calc.range(models.village_base.baseList[tribeCount-i].cox, models.village_base.baseList[tribeCount-i].coy, pos[0], pos[1]) >= 3):
                    x = x + 1
            if(x != tribeCount):
                x = 0
                pos = models.calc.randomPos(self.cox, self.coy)
        return pos

    def tribeGenerate(self, tab, maxTribes):
        tribeCount = 0
        while (tribeCount != maxTribes):
            pos = models.calc.randomPos(self.cox, self.coy)
            if (tribeCount != 0):
                pos = self.isNext(pos, tribeCount)
            if (tab[pos[1]][pos[0]] not in [1, 2, 3, 4, 5, 6]):
                tab[pos[1]][pos[0]] = 3
                models.village_base.baseList.append(models.village_base(pos[0], pos[1]))
                self.villagersGenerate(tab, models.village_base.baseList[tribeCount].population, tribeCount, pos[0], pos[1])
                tribeCount += 1

    # All the starting objects are generated on the previously empty board
    def boardGenerate(self, tab, maxFood, maxMonster, maxTribes):
        self.tribeGenerate(tab, maxTribes)
        self.foodGenerate(tab, maxFood)
        self.monsterGenerate(tab, maxMonster)
        for y in range(len(tab)):
            print()
            for x in range(len(tab[y])):
                if (tab[y][x] not in [1, 2, 3, 4, 5, 6]):
                    tab[y][x] = 0

                print(tab[y][x], end="|")

        return tab

    # For first villagers we need function similar to food and monster
    # where we create village_base and after that
    # we add later agreed amount of villager one or two block from base
