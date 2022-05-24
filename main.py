import models
import time


start_time = time.time()
# Starting variables which user will be inputting
maxMonster = 5
maxFood = 5
maxTribes = 5


def main():
    # BOARD INITIALIZING
    board = models.board(10, 10)
    tab = board.boardInit()

    # BOARD GENERATING
    tab = board.boardGenerate(tab, maxFood, maxMonster, maxTribes)

    # BOARD PRINTING
    for y in range(len(tab)):
        print()
        for x in range(len(tab[y])):
            print(tab[y][x], end="|")

    print("--- %s seconds ---" % (time.time() - start_time))
    # CHECKING BOARD IN RANGE OF EVERY OBJECT ON THE BOARD
    for i in range(len(models.monster.monsterList)):
        bruh = models.monster.monsterList[i]
        xd = bruh.checkRange(tab, bruh.range, bruh.cox, bruh.coy, bruh.type, bruh.id, bruh.tribe, bruh.job)
        print(xd)
    for base in models.villageBase.baseList:
        for unit in base.populationList:
            xd = unit.checkRange(tab, unit.range, unit.cox, unit.coy, unit.type, unit.id, unit.tribe, unit.job)
            print(xd)



main()

print("--- %s seconds ---" % (time.time() - start_time))
