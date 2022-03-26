import models


# Board class where the simulation happens
class board:

    def __init__(self, cox, coy):
        self.cox = cox
        self.coy = coy

    # Where getting empty 2D list
    def boardInit(self):
        tab = [[None] * self.cox for _ in range(self.coy)]
        return tab

    # Function generates random coordinates and if the spot is empty makes new food object in food list with those coordinates
    def foodGenerate(self, tab, maxFood):
        foodCount = 0
        while (foodCount != maxFood):
            pos = models.math.randomPos(self.cox, self.coy)
            if (tab[pos[1]][pos[0]] != 1):
                tab[pos[1]][pos[0]] = 1
                models.resource.foodList.append(models.resource(pos[1], pos[0]))
                foodCount += 1

    # Function generates random coordinates and if the spot is empty makes new monster object in monster list with those coordinates
    def monsterGenerate(self, tab, maxMonster):
        monsterCount = 0
        while (monsterCount != maxMonster):
            pos = models.math.randomPos(self.cox, self.coy)
            if (tab[pos[1]][pos[0]] not in [1, 2]):
                tab[pos[1]][pos[0]] = 2
                models.monster.monsterList.append(models.monster("wiesio", 100, 10, 10, 1, "food", pos[1], pos[0]))
                monsterCount += 1

    # All the starting objects are generated on the previously empty board
    def boardGenerate(self, tab, maxFood, maxMonster):
        self.foodGenerate(tab, maxFood)
        self.monsterGenerate(tab, maxMonster)
        for y in range(len(tab)):
            print()
            for x in range(len(tab[y])):
                if (tab[y][x] not in [1, 2]):
                    tab[y][x] = 0

                print(tab[y][x], end="|")

        return tab

    # For first villagers we need function similar to food and monster
    # where we create village_base and after that
    # we add later agreed amount of villager one or two block from base
