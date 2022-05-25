import models
import time
import sys
import ui.MenuLayout
from PyQt6.QtWidgets import *


def main():
    # MENU SETUP
    app = QApplication(sys.argv)
    Form = QWidget()
    menu = ui.MenuLayout.Ui_Form()
    menu.setupUi(Form)
    Form.show()
    app.exec()
    start_time = time.time()  # Moved here to substract menu time from program running time

    # Exiting program if start button was not pressed
    if not(menu.condition):
        print("Start button not pressed.\nTerminating Simulation...")
        time.sleep(1)
        exit()

    # GRABBING USER INPUT VALUES
    maxMonster = int(menu.MonsterAmnt_prev.text())
    maxFood = int(menu.StartFood_prev.text())
    maxTribes = int(menu.TribeAmount_prev.text())

    # BOARD INITIALIZING
    board = models.board(int(menu.dimX_prev.text())*5, int(menu.dimY_prev.text())*5)
    tab = board.boardInit()

    # BOARD GENERATING
    tab = board.boardGenerate(tab, maxFood, maxMonster, maxTribes)

    for i in range(0, 3):
        # BOARD PRINTING
        for y in range(len(tab)):
            print()
            for x in range(len(tab[y])):
                print(tab[y][x], end="|")

        print("--- %s seconds ---" % (time.time() - start_time))
        # CHECKING BOARD IN RANGE OF EVERY OBJECT ON THE BOARD and attacking
        for bruh in models.monster.monsterList:
            enemy, sighted = bruh.checkRange(tab, bruh)
            # print(enemy, sighted)
        for base in models.villageBase.baseList:
            for bruh in base.populationList:
                enemy, sighted = bruh.checkRange(tab, bruh)
                # print(enemy, sighted)

        for monster in models.monster.monsterList:
            monster.move(tab, monster)
        for list in models.villageBase.baseList:
            for villager in list.populationList:
                villager.move(tab, villager)

        print("--- %s seconds ---" % (time.time() - start_time))


main()
