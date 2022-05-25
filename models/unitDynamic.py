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
    def checkRange(cls, tab, ent):
        # In chosen list it checks for every position around(in a circle) given object, according to this object's range
        x = 0
        y = 0
        enemy = []
        sighted = []
        name = type(ent).__name__
        for j in range(1, (ent.range*2)+1):
            y = unitDynamic.direction("south", x, y)
            x = unitDynamic.direction("west", x, y)
            for k in range(2*j):
                y = unitDynamic.direction("north", x, y)
                unitDynamic.ifInBoard(tab, x, y, enemy, ent, name, sighted, j)
            for k in range(2*j):
                x = unitDynamic.direction("east", x, y)
                unitDynamic.ifInBoard(tab, x, y, enemy, ent, name, sighted, j)
            for k in range(2*j):
                y = unitDynamic.direction("south", x, y)
                unitDynamic.ifInBoard(tab, x, y, enemy, ent, name, sighted, j)
            for k in range(2*j):
                x = unitDynamic.direction("west", x, y)
                unitDynamic.ifInBoard(tab, x, y, enemy, ent, name, sighted, j)
        return (enemy, sighted)

    @classmethod
    def ifInBoard(cls, tab, x, y, enemy, ent, name, sighted, j):
        # Function for possible error if checked position would be outside of board's range
        if(0 > (ent.cox + x) or (len(tab[1])-1) < (ent.cox + x) or 0 > (ent.coy + y) or (len(tab)-1) < (ent.coy + y)):
            pass
        else:
            # Checks if there is villager in monsters range
            checked = tab[ent.coy + y][ent.cox + x]
            if(ent.type == "monster"):
                if(checked in [4, 5, 6]):
                    for villagerlist in models.villageBase.baseList:
                        for villager in villagerlist.populationList:
                            if(ent.cox + x == villager.cox and ent.coy + y == villager.coy):
                                if(j <= ent.range):
                                    enemy.append([villager.cox, villager.coy])
                                    print("{} {} attacked {} {} from base {}".format(name, ent.id, villager.job, villager.id, villagerlist.id))
                                    villager.currenthp = villager.currenthp - ent.attack
                                    if (villager.currenthp <= 0):
                                        villager.deletion("None", models.villageBase.baseList, tab)
                                sighted.append([villager.cox, villager.coy])

            elif(ent.type == "villager"):
                if(checked in [4, 5, 6]):
                    for villagerlist in models.villageBase.baseList:
                        if(ent.tribe != villagerlist.id):
                            for villager in villagerlist.populationList:
                                if(ent.cox + x == villager.cox and ent.coy + y == villager.coy):
                                    if(j <= ent.range):
                                        enemy.append([villager.cox, villager.coy])
                                        # print("{} {} from base {} attacked {} {} from base {}".format(name, ent.id, ent.tribe, villager.job, villager.id, villagerlist.id))
                                        villager.currenthp = villager.currenthp - ent.attack
                                        if (villager.currenthp <= 0):
                                            villager.deletion("None", models.villageBase.baseList, tab)
                                    sighted.append([villager.cox, villager.coy])

                elif(checked == 2):
                    for monsterEnemy in models.monster.monsterList:
                        if(ent.cox + x == monsterEnemy.cox and ent.coy + y == monsterEnemy.coy):
                            if(j <= ent.range):
                                enemy.append([monsterEnemy.cox, monsterEnemy.coy])
                                # print("{} {} from base {} attacked {} {}".format(name, ent.id, ent.tribe, monsterEnemy.job, monsterEnemy.id))
                                monsterEnemy.currenthp = monsterEnemy.currenthp - ent.attack
                                if (monsterEnemy.currenthp <= 0):
                                    monsterEnemy.deletion(models.villageBase.baseList[ent.tribe], models.monster.monsterList, tab)
                            sighted.append([monsterEnemy.cox, monsterEnemy.coy])
                elif(checked == 3):
                    for base in models.villageBase.baseList:
                        if(ent.tribe != base.id):
                            if(ent.cox + x == base.cox and ent.coy + y == base.coy):
                                if(j <= ent.range):
                                    enemy.append([base.cox, base.coy])
                                    # print("{} {} from base {} attacked {} {}".format(name, ent.id, ent.tribe, base.job, base.id))
                                    base.currenthp = base.currenthp - ent.attack
                                    if (base.currenthp <= 0):
                                        base.deletion(models.villageBase.baseList[ent.tribe], models.villageBase.baseList, tab)
                elif(checked == 1):
                    if(j <= ent.range):
                        for food in models.resource.resourceList:
                            if(ent.cox + x == food.cox and ent.coy + y == food.coy):
                                food.deletion(models.villageBase.baseList[ent.tribe], models.resource.resourceList, tab)

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

    @classmethod
    def move(cls, tab, entity):
        name = type(entity).__name__
        tab[entity.coy][entity.cox] = 0
        mPos = models.calc.movePos(tab, entity)
        entity.cox = mPos[0]
        entity.coy = mPos[1]
        if(name == "monster"):
            tab[mPos[1]][mPos[0]] = 2
        elif(name == "warrior"):
            tab[mPos[1]][mPos[0]] = 4
        elif(name == "spearman"):
            tab[mPos[1]][mPos[0]] = 5
        elif(name == "archer"):
            tab[mPos[1]][mPos[0]] = 6

    def deletion(self, tribe, list, tab):
        pass
