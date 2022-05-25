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
    def findMovePos(cls, ent):
        x = random.randint(ent.cox - ent.range, ent.cox + ent.range)
        y = random.randint(ent.coy - ent.range, ent.coy + ent.range)
        pos = [x, y]
        return pos

    @classmethod
    def movePos(cls, tab, ent):
        escape = 0
        pos = calc.findMovePos(ent)
        while(0 > pos[0] or (len(tab[1])-1) < pos[0] or 0 > pos[1] or (len(tab)-1) < pos[1]):
            pos = calc.findMovePos(ent)
        while(tab[pos[1]][pos[0]] != 0):
            escape += 1
            if(escape > 10):
                return [ent.cox, ent.coy]
            pos = calc.findMovePos(ent)
            while(0 > pos[0] or (len(tab[1])-1) < pos[0] or 0 > pos[1] or (len(tab)-1) < pos[1]):
                pos = calc.findMovePos(ent)
        return pos

    @classmethod
    def yesOrNo(cls, first, second):
        # Help to randomize choosing between two things, for example if tribe is aggressive or not
        x = [first, second]
        return random.choice(x)

    @classmethod
    def rangeBetween(cls, firstx, firsty, secondx, secondy):
        # Finds a distance between two locations
        x = abs(firstx - secondx)
        y = abs(firsty - secondy)

        answer = pow(x, 2) + pow(y, 2)
        answer = int(math.sqrt(answer))

        return answer
