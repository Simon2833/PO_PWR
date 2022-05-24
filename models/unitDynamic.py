from abc import abstractmethod
from models.unit import unit
import models


# Basic villager class from whom every other citizen class is inherited
class unitDynamic(unit):

    def __init__(self, cox, coy, id, maxhp, attack, armor, range):
        super().__init__(cox, coy, id)
        self.maxhp = maxhp
        self.attack = attack
        self.armor = armor
        self.range = range
        self.cox = cox
        self.coy = coy

    @classmethod
    def checkRange(cls, tab, entityRange, cox, coy, type, id, tribe, job):
        # In chosen list it checks for every position around(in a circle) given object, according to this object's range
        x = 0
        y = 0
        enemy = []
        for j in range(1, entityRange+1):
            y = unitDynamic.direction("south", x, y)
            x = unitDynamic.direction("west", x, y)
            for k in range(2*j):
                y = unitDynamic.direction("north", x, y)
                unitDynamic.ifInBoard(tab, x, y, cox, coy, type, id, tribe, job, enemy)
            for k in range(2*j):
                x = unitDynamic.direction("east", x, y)
                unitDynamic.ifInBoard(tab, x, y, cox, coy, type, id, tribe, job, enemy)
            for k in range(2*j):
                y = unitDynamic.direction("south", x, y)
                unitDynamic.ifInBoard(tab, x, y, cox, coy, type, id, tribe, job, enemy)
            for k in range(2*j):
                x = unitDynamic.direction("west", x, y)
                unitDynamic.ifInBoard(tab, x, y, cox, coy, type, id, tribe, job, enemy)
        return enemy

    @classmethod
    def ifInBoard(cls, tab, x, y, cox, coy, type, id, tribe, job, enemy):
        # Function for possible error if checked position would be outside of board's range
        if(0 > (cox + x) or (len(tab[1])-1) < (cox + x) or 0 > (coy + y) or (len(tab)-1) < (coy + y)):
            pass
        else:
            # Checks if there is villager in monsters range
            checked = tab[coy + y][cox + x]
            if(type == "monster"):
                if(checked in [4, 5, 6]):
                    for villagerlist in models.villageBase.baseList:
                        for villager in villagerlist.populationList:
                            if(cox + x == villager.cox and coy + y == villager.coy):
                                enemy.append([cox+x, coy+y])
                                print("{} {} attacked {} {} from base {}".format(job, id, villager.job, villager.id, villagerlist.id))
            elif(type == "villager"):
                if(checked in [4, 5, 6]):
                    for villagerlist in models.villageBase.baseList:
                        if(tribe != villagerlist.id):
                            for villager in villagerlist.populationList:
                                if(cox + x == villager.cox and coy + y == villager.coy):
                                    enemy.append([cox+x, coy+y])
                                    print("{} {} from base {} attacked {} {} from base {}".format(job, id, tribe, villager.job, villager.id, villagerlist.id))
                elif(checked == 2):
                    for monsterEnemy in models.monster.monsterList:
                        if(cox + x == monsterEnemy.cox and coy + y == monsterEnemy.coy):
                            enemy.append([cox+x, coy+y])
                            print("{} {} from base {} attacked {} {}".format(job, id, tribe, monsterEnemy.job, monsterEnemy.id))

    @classmethod
    def direction(cls, direction, x, y):
        # Function to switch between checked positions
        # Board is inverted, when we go up Y is decreasing
        if(direction == "north"):
            y = y - 1
            return y
        if(direction == "south"):
            y = y + 1
            return y
        if(direction == "west"):
            x = x - 1
            return x
        if(direction == "east"):
            x = x + 1
            return x


