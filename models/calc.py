import random
import math
import models


# Class where all the repeated calc functions are grouped up in one place
class calc:

    @classmethod
    def randomPos(cls, x, y):
        # Will be used to get coordinates of objects before creating for simplicity if current place would be occupied
        x = random.randint(0, x-1)
        y = random.randint(0, y-1)
        tab = [x, y]
        return tab

    @classmethod
    def yesOrNo(cls):
        # Help to randomize choosing between two things, for example if tribe is aggressive or not
        x = random.randint(0, 1)
        if x == 1:
            return True
        else:
            return False

    @classmethod
    def rangeBetween(cls, firstx, firsty, secondx, secondy):
        # Finds a distance between two locations
        x = abs(firstx - secondx)
        y = abs(firsty - secondy)

        answer = pow(x, 2) + pow(y, 2)
        answer = int(math.sqrt(answer))

        return answer

    @classmethod
    def checkAllRange(cls, tab, baseList, monsterList):
        # Parent function for checkRange to check all objects at once
        for i in range(len(baseList)):
            calc.checkRange(tab, baseList[i].populationList)

        calc.checkRange(tab, monsterList)

    @classmethod
    def checkRange(cls, tab, compareList):
        # In chosen list it checks for every position around(in a circle) given object, according to this object's range
        for i in range(len(compareList)):
            x = 0
            y = 0
            for j in range(1, compareList[i].range+1):
                y = calc.direction("south", x, y)
                x = calc.direction("west", x, y)
                for k in range(2*j):
                    y = calc.direction("north", x, y)
                    calc.ifInBoard(compareList, tab, x, y, i)
                for k in range(2*j):
                    x = calc.direction("east", x, y)
                    calc.ifInBoard(compareList, tab, x, y, i)
                for k in range(2*j):
                    y = calc.direction("south", x, y)
                    calc.ifInBoard(compareList, tab, x, y, i)
                for k in range(2*j):
                    x = calc.direction("west", x, y)
                    calc.ifInBoard(compareList, tab, x, y, i)

    @classmethod
    def ifInBoard(cls, compareList, tab, x, y, i):
        # Function for possible error if checked position would be outside of board's range
        if(0 > (compareList[i].cox + x) or (len(tab[1])-1) < (compareList[i].cox + x) or 0 > (compareList[i].coy + y) or (len(tab)-1) < (compareList[i].coy + y)):
            pass
        else:
            # Checks if there is villager in monsters range
            checked = tab[compareList[i].coy + y][compareList[i].cox + x]
            if(compareList[i].type == "monster"):
                if(checked in [4, 5, 6]):
                    for villagerlist in models.villageBase.baseList:
                        for villager in villagerlist.populationList:
                            if(compareList[i].cox + x == villager.cox and compareList[i].coy + y == villager.coy):
                                print("monster {} attacked villager {} from base {}".format(compareList[i].id, villager.id, villagerlist.id))
                elif(compareList[i].type == "villager"):
                    if(checked in [4, 5, 6]):
                        for villagerlist in models.villageBase.baseList:
                            for villager in villagerlist.populationList:
                                if(compareList[i].cox + x == villager.cox and compareList[i].coy + y == villager.coy):
                                    print("villager {} from base {} attacked villager {} from base {}".format(compareList[i].id, models.villageBase.baseList[compareList[i].tribe], villager.id, villagerlist.id))
                    elif(checked == 2):
                        pass

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
