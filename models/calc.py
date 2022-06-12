import random
import math


# Class where all the repeated calc functions are grouped up in one place
class calc:

    @classmethod
    def randomChance(cls):
        chance = random.randint(1, 100)
        return chance

    @classmethod
    def randomPos(cls, x, y):
        # Will be used to get coordinates of objects before creating for simplicity if current place would be occupied
        x = random.randint(0, x-1)
        y = random.randint(0, y-1)
        tab = [x, y]
        return tab

    @classmethod
    def movePos(cls, tab, ent, baseList):
        # Moving dynamic objects and checking if they're in board range and empty spot
        escape = 0
        if(ent.getType() == "monster"): pos = calc.__monsterFindMovePos(ent)
        else: pos = calc.__villagerFindMovePos(ent, baseList)
        while(0 > pos[0] or (len(tab[1])-1) < pos[0] or 0 > pos[1] or (len(tab)-1) < pos[1]):
            if(ent.getType() == "monster"): pos = calc.__monsterFindMovePos(ent)
            else: pos = calc.__villagerFindMovePos(ent, baseList)
        while(tab[pos[1]][pos[0]] != 0):
            escape += 1
            if(escape > 10):
                return [ent.cox, ent.coy]
            if(ent.getType() == "monster"): pos = calc.__monsterFindMovePos(ent)
            else: pos = calc.__villagerFindMovePos(ent, baseList)
            while(0 > pos[0] or (len(tab[1])-1) < pos[0] or 0 > pos[1] or (len(tab)-1) < pos[1]):
                if(ent.getType() == "monster"): pos = calc.__monsterFindMovePos(ent)
                else: pos = calc.__villagerFindMovePos(ent, baseList)
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

    @classmethod
    def __monsterFindMovePos(cls, ent):
        # Finds random position for monster within his range
        x = random.randint(ent.cox - ent.range, ent.cox + ent.range)
        y = random.randint(ent.coy - ent.range, ent.coy + ent.range)
        pos = [x, y]
        return pos

    @classmethod
    def __villagerFindMovePos(cls, ent, baseList):
        # Finds random position for villager within his range and have aggro when is on the war with other tribe
        x = random.randint(ent.cox - ent.range, ent.cox + ent.range)
        y = random.randint(ent.coy - ent.range, ent.coy + ent.range)
        pos = [x, y]
        if(baseList[ent.tribe].status == "peace"): return pos

        bestId = 100
        if(ent.id % 2 == 0):

            best = 100
            for base in baseList:
                if(base.status == "peace"): continue
                if(base.id == baseList[ent.tribe].id): continue
                new = calc.rangeBetween(ent.cox, ent.coy, base.cox, base.coy)
                if(new < best):
                    best = new
                    bestId = base.id

        if(bestId == 100): return pos

        if(baseList[bestId].cox > ent.cox): x = random.randint(ent.cox, ent.cox + ent.range)
        else: x = random.randint(ent.cox - ent.range, ent.cox)

        if(baseList[bestId].coy > ent.coy): y = random.randint(ent.coy, ent.coy + ent.range)
        else: y = random.randint(ent.coy - ent.range, ent.coy)

        pos = [x, y]
        return pos
