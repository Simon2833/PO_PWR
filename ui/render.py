from PyQt6.QtWidgets import QApplication, QWidget, QGraphicsView, QGraphicsScene
from PyQt6.QtGui import QPen, QBrush
from PyQt6.QtCore import Qt
import sys

class Window(QWidget):					#6 kolorow	scene.clear() scene.update()
	def __init__(self):
		super().__init__()

		self.setGeometry(0, 0, 850, 850)
		self.setWindowTitle("Simulation Display")\

		self.scene = QGraphicsScene()
		self.view = QGraphicsView(self.scene, self)
		self.view.setGeometry(0,0,810,810)

		blackPen = QPen(Qt.GlobalColor.black)
		blackPen.setWidth(1)
		bkgBrush = QBrush()
		bkgBrush.setColor(Qt.GlobalColor.green)
		bkgBrush.setStyle(Qt.BrushStyle.DiagCrossPattern)
		self.scene.addRect(0, 0, 800, 800,blackPen, bkgBrush)

	def PaintRectangle(xObjPos, yObjPos):

		self.scene.addRect(xObjPos*10, yObjPos*10,8, 8, QPen(Qt.GlobalColor.black))
		self.scene.update()
		self.view.update()










