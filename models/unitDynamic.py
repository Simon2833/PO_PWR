from models.unit import unit
import models


# Basic villager class from whom every other citizen class is inherited
class unitDynamic(unit):

    def __init__(self, cox, coy, id, maxhp, attack, armor, range):
        super().__init__(cox, coy, id)
        self.maxhp = maxhp
        self.currenthp = self.maxhp
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
        for j in range(1, ent.range+1):
            y = unitDynamic.direction("south", x, y)
            x = unitDynamic.direction("west", x, y)
            for k in range(2*j):
                y = unitDynamic.direction("north", x, y)
                unitDynamic.ifInBoard(tab, x, y, ent)
            for k in range(2*j):
                x = unitDynamic.direction("east", x, y)
                unitDynamic.ifInBoard(tab, x, y, ent)
            for k in range(2*j):
                y = unitDynamic.direction("south", x, y)
                unitDynamic.ifInBoard(tab, x, y, ent)
            for k in range(2*j):
                x = unitDynamic.direction("west", x, y)
                unitDynamic.ifInBoard(tab, x, y, ent)

    @classmethod
    def ifInBoard(cls, tab, x, y, ent):
        # Function for possible error if checked position would be outside of board's range
        if(0 > (ent.cox + x) or (len(tab[1])-1) < (ent.cox + x) or 0 > (ent.coy + y) or (len(tab)-1) < (ent.coy + y)):
            return

        # Checks if there is villager in monsters range
        checked = tab[ent.coy + y][ent.cox + x]
        if(ent.type == "monster"):
            if(checked in [4, 5, 6]):
                unitDynamic.monsterVillager(ent, x, y, tab)

        elif(ent.type == "villager"):
            if(checked == 1):
                unitDynamic.villagerFood(ent, x, y, tab)

            if(checked in [4, 5, 6]):
                unitDynamic.villagerVillager(ent, x, y, tab)

            elif(checked == 3):
                unitDynamic.villagerBase(ent, x, y, tab)

            elif(checked == 2):
                unitDynamic.villagerMonster(ent, x, y, tab)

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
    def move(cls, tab, entity, baseList):
        name = type(entity).__name__
        tab[entity.coy][entity.cox] = 0
        mPos = models.calc.movePos(tab, entity, baseList)
        entity.cox = mPos[0]
        entity.coy = mPos[1]
        if(name == "monster"):
            tab[mPos[1]][mPos[0]] = 2
            return
        elif(name == "warrior"):
            tab[mPos[1]][mPos[0]] = 4
            return
        elif(name == "spearman"):
            tab[mPos[1]][mPos[0]] = 5
            return
        elif(name == "archer"):
            tab[mPos[1]][mPos[0]] = 6
            return

    def deletion(self, tribe, list, tab):
        pass

    def heal(self):
        if(self.currenthp < self.maxhp):
            self.currenthp = self.currenthp + 2
            if(self.currenthp > self.maxhp):
                self.currenthp = self.maxhp

    @classmethod
    def villagerVillager(cls, ent, x, y, tab):
        for villagerlist in models.villageBase.baseList:
            if(ent.tribe == villagerlist.id): continue
            for villager in villagerlist.populationList:
                if(ent.cox + x != villager.cox or ent.coy + y != villager.coy): continue

                if(models.calc.randomChance() < 2 and villagerlist.attitude == models.villageBase.baseList[ent.tribe].attitude == "passive"):
                    if(villagerlist.status == "war"):
                        models.villageBase.baseList[ent.tribe].status = "war"
                    villagerlist.deletion(models.villageBase.baseList[ent.tribe], models.villageBase.baseList, tab)
                else:
                    villager.currenthp = villager.currenthp - ent.attack
                    if (villager.currenthp <= 0):
                        villager.deletion("None", models.villageBase.baseList, tab)
                        villagerlist.morale = villagerlist.morale - 10
                        villagerlist.status = "war"
                        models.villageBase.baseList[ent.tribe].status = "war"
                        if(len(villagerlist.populationList) == 0):
                            villagerlist.deletion(models.villageBase.baseList[ent.tribe], models.villageBase.baseList, tab)

    @classmethod
    def villagerFood(cls, ent, x, y, tab):
        for food in models.resource.resourceList:
            if(ent.cox + x != food.cox or ent.coy + y != food.coy): continue
            food.deletion(models.villageBase.baseList[ent.tribe], models.resource.resourceList, tab)

    @classmethod
    def villagerBase(cls, ent, x, y, tab):
        for base in models.villageBase.baseList:
            if(ent.tribe != base.id and models.villageBase.baseList[ent.tribe].status == "war" and base.status == "war"):
                if(ent.cox + x != base.cox or ent.coy + y != base.coy): continue
                base.currenthp = base.currenthp - 2
                if (base.currenthp > 0): continue
                base.deletion(models.villageBase.baseList[ent.tribe], models.villageBase.baseList, tab)
                models.villageBase.baseList[ent.tribe].status = "peace"

    @classmethod
    def villagerMonster(cls, ent, x, y, tab):
        for monsterEnemy in models.monster.monsterList:
            if(ent.cox + x != monsterEnemy.cox or ent.coy + y != monsterEnemy.coy): continue
            monsterEnemy.currenthp = monsterEnemy.currenthp - ent.attack
            if (monsterEnemy.currenthp > 0): continue
            monsterEnemy.deletion(models.villageBase.baseList[ent.tribe], models.monster.monsterList, tab)

    @classmethod
    def monsterVillager(cls, ent, x, y, tab):
        for villagerlist in models.villageBase.baseList:
            for villager in villagerlist.populationList:
                if(ent.cox + x != villager.cox or ent.coy + y != villager.coy): continue
                villager.currenthp = villager.currenthp - ent.attack
                if (villager.currenthp > 0): continue
                villager.deletion("None", models.villageBase.baseList, tab)
