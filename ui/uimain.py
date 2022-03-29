from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication([])
window = QMainWindow()
window.statusBar().showMessage("status bar text")
window.menuBar().addMenu("File") #menu category text




window.show()
sys.exit(app.exec())