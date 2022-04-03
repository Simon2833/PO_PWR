from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMenu
from PyQt6.QtGui import QFont
import sys

class Window(QWidget):
	def __init__(self):
		super().__init__()


		self.setGeometry(0, 0, 1024, 1024)	#xpos, ypos, height, width
		self.setWindowTitle("test window title")
		#possible addition of icon in future with QtGui.QIcon
		self.setFixedHeight(1024)	#overwrites setGeometry values and makes them constant
		self.setFixedWidth(1024)		#	-//-

		self.create_button()

	def create_button(self):
		button = QPushButton("Test Button", self)
		button.setGeometry(50, 50, 100, 50)
		button.setFont(QFont("Sanserif", 11, QFont.Weight.Bold))
		#btn.setIcon(QIcon("--path"))	Possible future usage of images instead of text on buttons (QIcon)


		#pop-up menu button mode
		menu = QMenu()
		menu.addAction("opt. 1")
		menu.addAction("opt. 2")
		menu.addAction("opt. 3")
		button.setMenu(menu)


app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())