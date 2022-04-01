import models

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

    for y in range(len(tab)):
        print()
        for x in range(len(tab[y])):
            print(tab[y][x], end="|")
    # BOARD REFRESHING
    # STILL IN WORK :(


main()
