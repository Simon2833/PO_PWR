import MenuLayout
from PyQt6.QtWidgets import QApplication, QWidget, QGraphicsView, QGraphicsScene
from PyQt6.QtGui import QPen, QBrush
from PyQt6.QtCore import Qt
import sys
from PyQt6 import uic
import time



class UI(QWidget):
	def __init__(self):
		super().__init__()
		uic.loadUi("MenuLayout.ui", self)

		self.pushButton.setText("Start")
		self.pushButton.clicked.connect(self.clicked_btn)


	def clicked_btn(self):
		print("start")
		time.sleep(0.2)
		window.close()







app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()

