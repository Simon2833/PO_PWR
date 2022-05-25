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

    #GRABBING USER INPUT VALUES
    maxMonster = int(menu.MonsterAmnt_prev.text())
    maxFood = int(menu.StartFood_prev.text())
    maxTribes = int(menu.TribeAmount_prev.text())

    # BOARD INITIALIZING
    board = models.board(int(menu.dimX_prev.text())*5, int(menu.dimY_prev.text())*5)
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
