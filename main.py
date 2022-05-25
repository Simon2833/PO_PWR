import models
import time
import sys
import ui.MenuLayout
from PyQt6.QtWidgets import *



def main():
    #MENU SETUP
    app = QApplication(sys.argv)
    Form = QWidget()
    menu = ui.MenuLayout.Ui_Form()
    menu.setupUi(Form)
    Form.show()
    app.exec()
    start_time = time.time() #Moved here to substract menu time from program running time

    #exiting program if start button was not pressed
    if not(menu.condition):
        print("Start button not pressed.\nTerminating Simulation...")
        time.sleep(1)
        exit()

    #GRABBING USER INPUT VALUES
    maxMonster = int(menu.MonsterAmnt_prev.text())
    maxFood = int(menu.StartFood_prev.text())
    maxTribes = int(menu.TribeAmount_prev.text())

    # BOARD INITIALIZING
    board = models.board(int(menu.dimX_prev.text()), int(menu.dimY_prev.text()))
    tab = board.boardInit()

    # BOARD GENERATING
    tab = board.boardGenerate(tab, maxFood, maxMonster, maxTribes)

    for i in range(0, 10):
        # BOARD PRINTING
        for y in range(len(tab)):
            print()
            for x in range(len(tab[y])):
                print(tab[y][x], end="|")

        print("--- %s seconds ---" % (time.time() - start_time))
        # CHECKING BOARD IN RANGE OF EVERY OBJECT ON THE BOARD
        # for bruh in models.monster.monsterList:
        #     enemy, sighted = bruh.checkRange(tab, bruh)
        #     print(enemy, sighted)
        # for base in models.villageBase.baseList:
        #     for bruh in base.populationList:
        #         enemy, sighted = bruh.checkRange(tab, bruh)
        #         print(enemy, sighted)
        print("--- %s seconds ---" % (time.time() - start_time))
        for monster in models.monster.monsterList:
            monster.move(tab, monster)



main()

