import models


max_food = 10


def main():

    board = models.board(24, 10)

    tab = board.board_init()

    tab = board.board_generate(tab, max_food)


main()
