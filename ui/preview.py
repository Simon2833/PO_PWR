import render
import MenuLayout
from PyQt6.QtWidgets import QApplication, QWidget, QGraphicsView, QGraphicsScene
from PyQt6.QtGui import QPen, QBrush
from PyQt6.QtCore import Qt
import sys

print("dupa")











app = QApplication([])
RenderWindow = render.Window()
RenderWindow.show()

ui = MenuLayout.Ui_Form()
ui.setupUi(Form)
Form.show()


sys.exit(app.exec())


RenderWindow.PaintRectangle(10, 10)
RenderWindow.scene.update()
app.update()
RenderWindow.view.update()