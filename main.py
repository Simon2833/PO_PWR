import models
import time
import sys
import ui.MenuLayout
import ui.Simulation
from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication

def main():
    # MENU SETUP
    app = QApplication(sys.argv)
    Form = QWidget()
    menu = ui.MenuLayout.Ui_Form()
    menu.setupUi(Form)
    Form.show()
    app.exec()

    # Exiting program if start button was not pressed
    if not(menu.condition):
        print("Start button not pressed.\nTerminating Simulation...")
        time.sleep(1) 
        exit()

    # GRABBING USER INPUT VALUES
    maxMonster = int(menu.MonsterAmnt_prev.text())
    maxFood = int(menu.StartFood_prev.text())
    maxTribes = int(menu.TribeAmount_prev.text())
    spawnRate = int(menu.FSpawnRate_prev.text())
    initialpopulation = int(menu.InitPopulation_prev.text())    
    array = [maxMonster, maxFood, maxTribes, spawnRate, initialpopulation, int(menu.dimX_prev.text()), int(menu.dimY_prev.text())]
    del app

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    sim = ui.Simulation.Ui_Simulation()
    sim.setupUi(Form, array)
    Form.show()
    sys.exit(app.exec())

















    # BOARD INITIALIZING
    board = models.board(int(menu.dimX_prev.text()), int(menu.dimY_prev.text()))
    tab = board.boardInit()

    # BOARD GENERATING
    tab = board.boardGenerate(tab, maxFood, maxMonster, maxTribes, initialpopulation)

    for i in range(0, 2):
        # BOARD PRINTING
        for y in range(len(tab)):
            print()
            for x in range(len(tab[y])):
                print(tab[y][x], end="|")
        print()


        # CHECKING BOARD IN RANGE OF EVERY OBJECT ON THE BOARD and attacking
        for monster in models.monster.monsterList:
            sighted = monster.checkRange(tab, monster)
            monster.move(tab, monster)
            monster.heal()

        for base in models.villageBase.baseList:
            base.moraleUpdate("None", models.villageBase.baseList, tab)
            for villager in base.populationList:
                sighted = villager.checkRange(tab, villager)
                villager.move(tab, villager)
                villager.heal()
            base.heal()

        for base in models.villageBase.baseList:
            print(base.currenthp, base.morale, len(base.populationList), base.status)


        if(spawnRate > 0 and i % spawnRate == 0):
            models.resource.spawnRate(tab)

        if(len(models.villageBase.baseList) <= 1):
            pass  # olaf dokończy koniec gry


main()
