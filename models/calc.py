import random
import math


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
        x = random.randint(0, 1)
        if x == 1:
            return True
        else:
            return False

    @classmethod
    def rangeBetween(cls, firstx, firsty, secondx, secondy):
        x = abs(firstx - secondx)
        y = abs(firsty - secondy)

        answer = pow(x, 2) + pow(y, 2)
        answer = int(math.sqrt(answer))

        return answer

    @classmethod
    def checkAllRange(cls, tab, baseList, monsterList):
        for i in range(len(baseList)):
            calc.checkRange(tab, baseList[i].populationList)

        calc.checkRange(tab, monsterList)

    @classmethod
    def checkRange(cls, tab, compareList):
        for i in range(len(compareList)):
            position = (compareList[i].cox, compareList[i].coy)
            print(position)
            x = 0
            y = 0
            for j in range(1, compareList[i].range+1):
                y = calc.direction("south", x, y)
                x = calc.direction("west", x, y)
                for k in range(2*j):
                    y = calc.direction("north", x, y)
                    calc.ifInBoard(compareList, tab, position, x, y, i)
                for k in range(2*j):
                    x = calc.direction("east", x, y)
                    calc.ifInBoard(compareList, tab, position, x, y, i)
                for k in range(2*j):
                    y = calc.direction("south", x, y)
                    calc.ifInBoard(compareList, tab, position, x, y, i)
                for k in range(2*j):
                    x = calc.direction("west", x, y)
                    calc.ifInBoard(compareList, tab, position, x, y, i)
            print()

    @classmethod
    def ifInBoard(cls, compareList, tab, position, x, y, i):
        if(0 > (compareList[i].cox + x) or (len(tab[1])-1) < (compareList[i].cox + x) or 0 > (compareList[i].coy + y) or (len(tab)-1) < (compareList[i].coy + y)):
            print(i, "out of board")
        else:
            checked = tab[compareList[i].coy + y][compareList[i].cox + x]
            print(i, position, checked)

    @classmethod
    # Board is inverted, when we go up Y is decreasing
    def direction(cls, direction, x, y):
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
