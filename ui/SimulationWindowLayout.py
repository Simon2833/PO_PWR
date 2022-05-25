from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Simulation(object):
    def setupUi(self, Simulation):
        if not Simulation.objectName():
            Simulation.setObjectName(u"Simulation")
        Simulation.resize(1080, 820)
        self.graphicsView = QGraphicsView(Simulation)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(10, 10, 800, 800))
        self.label = QLabel(Simulation)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(820, 20, 61, 16))
        font = QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.roundCount = QLabel(Simulation)
        self.roundCount.setObjectName(u"roundCount")
        self.roundCount.setGeometry(QRect(880, 20, 71, 16))
        font1 = QFont()
        font1.setPointSize(14)
        self.roundCount.setFont(font1)
        self.label_3 = QLabel(Simulation)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(820, 60, 121, 16))
        font2 = QFont()
        font2.setPointSize(11)
        self.label_3.setFont(font2)
        self.monsterCount = QLabel(Simulation)
        self.monsterCount.setObjectName(u"monsterCount")
        self.monsterCount.setGeometry(QRect(940, 60, 41, 16))
        self.monsterCount.setFont(font2)
        self.label_5 = QLabel(Simulation)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(820, 80, 91, 16))
        self.label_5.setFont(font2)
        self.foodCount = QLabel(Simulation)
        self.foodCount.setObjectName(u"foodCount")
        self.foodCount.setGeometry(QRect(920, 80, 41, 16))
        self.foodCount.setFont(font2)
        self.label_7 = QLabel(Simulation)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(820, 100, 101, 16))
        self.label_7.setFont(font2)
        self.tribeCount = QLabel(Simulation)
        self.tribeCount.setObjectName(u"tribeCount")
        self.tribeCount.setGeometry(QRect(920, 100, 41, 16))
        self.tribeCount.setFont(font2)
        self.label_9 = QLabel(Simulation)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(820, 120, 191, 16))
        self.label_9.setFont(font2)
        self.populationCount = QLabel(Simulation)
        self.populationCount.setObjectName(u"populationCount")
        self.populationCount.setGeometry(QRect(1010, 120, 21, 16))
        self.populationCount.setFont(font2)
        self.simSpeedSlider = QSlider(Simulation)
        self.simSpeedSlider.setObjectName(u"simSpeedSlider")
        self.simSpeedSlider.setGeometry(QRect(920, 670, 151, 22))
        self.simSpeedSlider.setCursor(QCursor(Qt.SizeHorCursor))
        self.simSpeedSlider.setOrientation(Qt.Horizontal)
        self.label_11 = QLabel(Simulation)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(820, 670, 101, 16))
        self.line = QFrame(Simulation)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(820, 40, 241, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.PauseButton = QPushButton(Simulation)
        self.PauseButton.setObjectName(u"PauseButton")
        self.PauseButton.setGeometry(QRect(820, 700, 251, 51))
        font3 = QFont()
        font3.setFamilies([u"Comic Sans MS"])
        font3.setPointSize(14)
        font3.setBold(False)
        self.PauseButton.setFont(font3)
        self.PauseButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.EndButton = QPushButton(Simulation)
        self.EndButton.setObjectName(u"EndButton")
        self.EndButton.setGeometry(QRect(820, 760, 251, 51))
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(False)
        self.EndButton.setFont(font4)
        self.EndButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.retranslateUi(Simulation)

        QMetaObject.connectSlotsByName(Simulation)
    # setupUi

    def retranslateUi(self, Simulation):
        Simulation.setWindowTitle(QCoreApplication.translate("Simulation", u"Form", None))
        self.label.setText(QCoreApplication.translate("Simulation", u"Round:", None))
        self.roundCount.setText(QCoreApplication.translate("Simulation", u"0", None))
        self.label_3.setText(QCoreApplication.translate("Simulation", u"Current Monsters:", None))
        self.monsterCount.setText(QCoreApplication.translate("Simulation", u"0", None))
        self.label_5.setText(QCoreApplication.translate("Simulation", u"Current Food:", None))
        self.foodCount.setText(QCoreApplication.translate("Simulation", u"0", None))
        self.label_7.setText(QCoreApplication.translate("Simulation", u"Current Tribes:", None))
        self.tribeCount.setText(QCoreApplication.translate("Simulation", u"0", None))
        self.label_9.setText(QCoreApplication.translate("Simulation", u"Current Population (Global):", None))
        self.populationCount.setText(QCoreApplication.translate("Simulation", u"0", None))
        self.label_11.setText(QCoreApplication.translate("Simulation", u"Simulation Speed", None))
        self.PauseButton.setText(QCoreApplication.translate("Simulation", u"Pause/Continue", None))
        self.EndButton.setText(QCoreApplication.translate("Simulation", u"End", None))
    # retranslateUi
