# Form implementation generated from reading ui file 'Simulation.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Simulation(object):
    def setupUi(self, Simulation):
        Simulation.setObjectName("Simulation")
        Simulation.resize(1080, 820)
        self.graphicsView = QtWidgets.QGraphicsView(Simulation)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 800, 800))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(Simulation)
        self.label.setGeometry(QtCore.QRect(820, 20, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 14pt \"Segoe UI\";")
        self.label.setObjectName("label")
        self.roundCount = QtWidgets.QLabel(Simulation)
        self.roundCount.setGeometry(QtCore.QRect(880, 20, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.roundCount.setFont(font)
        self.roundCount.setObjectName("roundCount")
        self.label_3 = QtWidgets.QLabel(Simulation)
        self.label_3.setGeometry(QtCore.QRect(820, 60, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.monsterCount = QtWidgets.QLabel(Simulation)
        self.monsterCount.setGeometry(QtCore.QRect(940, 60, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.monsterCount.setFont(font)
        self.monsterCount.setObjectName("monsterCount")
        self.label_5 = QtWidgets.QLabel(Simulation)
        self.label_5.setGeometry(QtCore.QRect(820, 80, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.foodCount = QtWidgets.QLabel(Simulation)
        self.foodCount.setGeometry(QtCore.QRect(920, 80, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.foodCount.setFont(font)
        self.foodCount.setObjectName("foodCount")
        self.label_7 = QtWidgets.QLabel(Simulation)
        self.label_7.setGeometry(QtCore.QRect(820, 100, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.tribeCount = QtWidgets.QLabel(Simulation)
        self.tribeCount.setGeometry(QtCore.QRect(920, 100, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tribeCount.setFont(font)
        self.tribeCount.setObjectName("tribeCount")
        self.label_9 = QtWidgets.QLabel(Simulation)
        self.label_9.setGeometry(QtCore.QRect(820, 120, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.populationCount = QtWidgets.QLabel(Simulation)
        self.populationCount.setGeometry(QtCore.QRect(1010, 120, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.populationCount.setFont(font)
        self.populationCount.setObjectName("populationCount")
        self.simSpeedSlider = QtWidgets.QSlider(Simulation)
        self.simSpeedSlider.setGeometry(QtCore.QRect(920, 670, 151, 22))
        self.simSpeedSlider.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.SizeHorCursor))
        self.simSpeedSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.simSpeedSlider.setObjectName("simSpeedSlider")
        self.label_11 = QtWidgets.QLabel(Simulation)
        self.label_11.setGeometry(QtCore.QRect(820, 670, 101, 16))
        self.label_11.setObjectName("label_11")
        self.line = QtWidgets.QFrame(Simulation)
        self.line.setGeometry(QtCore.QRect(820, 40, 241, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.PauseButton = QtWidgets.QPushButton(Simulation)
        self.PauseButton.setGeometry(QtCore.QRect(820, 700, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.PauseButton.setFont(font)
        self.PauseButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.PauseButton.setObjectName("PauseButton")
        self.EndButton = QtWidgets.QPushButton(Simulation)
        self.EndButton.setGeometry(QtCore.QRect(820, 760, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.EndButton.setFont(font)
        self.EndButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.EndButton.setObjectName("EndButton")

        self.retranslateUi(Simulation)
        QtCore.QMetaObject.connectSlotsByName(Simulation)

    def retranslateUi(self, Simulation):
        _translate = QtCore.QCoreApplication.translate
        Simulation.setWindowTitle(_translate("Simulation", "Form"))
        self.label.setText(_translate("Simulation", "Round:"))
        self.roundCount.setText(_translate("Simulation", "0"))
        self.label_3.setText(_translate("Simulation", "Current Monsters:"))
        self.monsterCount.setText(_translate("Simulation", "0"))
        self.label_5.setText(_translate("Simulation", "Current Food:"))
        self.foodCount.setText(_translate("Simulation", "0"))
        self.label_7.setText(_translate("Simulation", "Current Tribes:"))
        self.tribeCount.setText(_translate("Simulation", "0"))
        self.label_9.setText(_translate("Simulation", "Current Population (Global):"))
        self.populationCount.setText(_translate("Simulation", "0"))
        self.label_11.setText(_translate("Simulation", "Simulation Speed"))
        self.PauseButton.setText(_translate("Simulation", "Pause/Continue"))
        self.EndButton.setText(_translate("Simulation", "End"))
