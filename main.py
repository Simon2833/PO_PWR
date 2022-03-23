import models



max_food = 20

def main():

    board = models.board(10, 10)

    tab = board.board_init()

    tab = board.board_generate(tab, max_food)



main()
