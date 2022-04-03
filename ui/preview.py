import render
from PyQt6.QtWidgets import QApplication, QWidget, QGraphicsView, QGraphicsScene
from PyQt6.QtGui import QPen, QBrush
from PyQt6.QtCore import Qt
import sys

print("dupa")











app = QApplication([])
window = render.Window()
window.show()
sys.exit(app.exec())


window.PaintRectangle(10, 10)
window.scene.update()
app.update()
window.view.update()