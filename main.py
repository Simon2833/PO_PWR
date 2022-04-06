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
    models.calc.checkAllRange(tab, models.villageBase.baseList, models.monster.monsterList)


main()

print("--- %s seconds ---" % (time.time() - start_time))
