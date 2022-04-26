
import sys
import MenuLayout
from PyQt6.QtWidgets import *



app = QApplication(sys.argv)
Form = QWidget()
ui = MenuLayout.Ui_Form()
ui.setupUi(Form)
Form.show()

#sys.exit(app.exec())
app.exec()

print("condition is equal to {}".format(ui.condition))
print("xdim is equal to {}".format(ui.dimX_prev.text()))
print("ydim is equal to {}".format(ui.dimY_prev.text()))
print("mosnteramnt is equal to {}".format(ui.MonsterAmnt_prev.text()))
print("startfood is equal to {}".format(ui.StartFood_prev.text()))
print("foodspawnrate is equal to {}".format(ui.FSpawnRate_prev.text()))
print("tribeamnt is equal to {}".format(ui.TribeAmount_prev.text()))
print("initialpopulation is equal to {}".format(ui.InitPopulation_prev.text()))



