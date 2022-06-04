import time
import sys
import ui.MenuLayout
import ui.Simulation
from PyQt6.QtWidgets import *
from PyQt6 import QtWidgets
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

    # GAME
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    sim = ui.Simulation.Ui_Simulation()
    sim.setupUi(Form, array)
    Form.show()
    sys.exit(app.exec())
    del app


main()
