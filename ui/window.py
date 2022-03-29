from PyQt6.QtWidgets import QApplication, QWidget
import sys

class Window(QWidget):
	def __init__(self):
		super().__init__()


		self.setGeometry(100, 100, 300, 300)	#xpos, ypos, height, width
		self.setWindowTitle("test window title")
		#possible addition of icon in future with QtGui.QIcon
		self.setFixedHeight(300)	#overwrites setGeometry values and makes them constant
		self.setFixedWidth(300)		#	-//-




app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())