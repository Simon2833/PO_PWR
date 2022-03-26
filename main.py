import models

# Starting variables which user will be inputting
maxMonster = 1
maxFood = 1


def main():
    # BOARD INITIALIZING
    board = models.board(10, 10)
    tab = board.boardInit()

    # BOARD GENERATING
    tab = board.boardGenerate(tab, maxFood, maxMonster)

    # BOARD REFRESHING
    # STILL IN WORK :(


main()
