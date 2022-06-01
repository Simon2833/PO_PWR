from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtOpenGL import *
from PyQt6 import *
from PyQt6.QtGui import QPainter, QColor, QBrush
import time
import copy
import sys
sys.path.append('../')
import models



class Ui_Simulation(object):
    def clickedbutton(self):
        app = QApplication.instance()
        app.closeAllWindows()

    def setupUi(self, Simulation, array):
        Simulation.setObjectName("Simulation")
        Simulation.resize(1080, 820)
        self.arr = array
        self.graphicsView = QtWidgets.QGraphicsView(Simulation)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 800, 800))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.label = QtWidgets.QLabel(Simulation)
        self.label.setGeometry(QtCore.QRect(820, 20, 61, 16))
        colors=[Qt.GlobalColor.white, Qt.GlobalColor.black, Qt.GlobalColor.cyan, Qt.GlobalColor.darkCyan, Qt.GlobalColor.red, Qt.GlobalColor.darkRed, Qt.GlobalColor.magenta, Qt.GlobalColor.darkMagenta, Qt.GlobalColor.green, Qt.GlobalColor.darkGreen, Qt.GlobalColor.yellow, Qt.GlobalColor.darkYellow, Qt.GlobalColor.blue, Qt.GlobalColor.darkBlue, Qt.GlobalColor.gray, Qt.GlobalColor.darkGray, Qt.GlobalColor.lightGray] 
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
        self.EndButton.clicked.connect(self.clickedbutton)
        self.PauseButton.clicked.connect(self.Simulate)
        ############################################################################################################
        
        
                

        ############################################################################################################
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
        self.PauseButton.setText(_translate("Simulation", "Start"))
        #self.PauseButton.setText(_translate("Simulation", "Pause/Continue"))
        self.EndButton.setText(_translate("Simulation", "End"))

    def Simulate(self):
        colors=[Qt.GlobalColor.white, Qt.GlobalColor.black, Qt.GlobalColor.cyan, Qt.GlobalColor.darkCyan, Qt.GlobalColor.red, Qt.GlobalColor.darkRed, Qt.GlobalColor.magenta, Qt.GlobalColor.darkMagenta, Qt.GlobalColor.green, Qt.GlobalColor.darkGreen, Qt.GlobalColor.yellow, Qt.GlobalColor.darkYellow, Qt.GlobalColor.blue, Qt.GlobalColor.darkBlue, Qt.GlobalColor.gray, Qt.GlobalColor.darkGray, Qt.GlobalColor.lightGray] 
        startData = self.arr
        self.PauseButton.setText("Pause/Continue")
        starttime = time.time()
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 800, 800)
        self.graphicsView.setScene(self.scene)

        edgeL = QPixmap(QImage('ui/assets/edge_L.png'))
        edgeT = QPixmap(QImage('ui/assets/edge_T.png'))
        edgeB = QPixmap(QImage('ui/assets/edge_B.png'))
        edgeR = QPixmap(QImage('ui/assets/edge_R.png'))
        land = QPixmap(QImage('ui/assets/land.png'))


        bgtemps=[]
        h = startData[-1]
        w = startData[-2]
        for x in range(0,w):
            for y in range(0,h):
                if(x == 0):
                    bgtemps.append(QGraphicsPixmapItem(edgeL))
                elif(x == w-1):
                    bgtemps.append(QGraphicsPixmapItem(edgeR))
                elif(y == 0):
                    bgtemps.append(QGraphicsPixmapItem(edgeT))
                elif(y == h-1):
                    bgtemps.append(QGraphicsPixmapItem(edgeB))
                else:
                    bgtemps.append(QGraphicsPixmapItem(land))
                self.scene.addItem(bgtemps[len(bgtemps)-1])
                bgtemps[len(bgtemps)-1].setPos(x*8, y*8)

        print(time.time() - starttime)


        


            # BOARD INITIALIZING
        board = models.board(w, h)
        tab = board.boardInit()

        # BOARD GENERATING
        tab = board.boardGenerate(tab, startData[1], startData[0], startData[2], startData[4])

        for i in range(0, 10):
            # BOARD PRINTING
            # for y in range(len(tab)):
            #     print()
            #     for x in range(len(tab[y])):
            #         print(tab[y][x], end="|")
            print()


            # CHECKING BOARD IN RANGE OF EVERY OBJECT ON THE BOARD and attacking
            for monster in models.monster.monsterList:
                sighted = monster.checkRange(tab, monster)
                monster.move(tab, monster)
                monster.heal()

            for base in models.villageBase.baseList:
                base.moraleUpdate("None", models.villageBase.baseList, tab)
                for villager in base.populationList:
                    sighted = villager.checkRange(tab, villager)
                    villager.move(tab, villager)
                    villager.heal()
                base.heal()

            for base in models.villageBase.baseList:
                print(base.currenthp, base.morale, len(base.populationList), base.status)


            if(startData[3] > 0 and i % startData[3] == 0):
                models.resource.spawnRate(tab)

            if(len(models.villageBase.baseList) <= 1):
                pass  # olaf dokończy koniec gry





        for base in models.villageBase.baseList:
            brush = QBrush(colors[base.id], Qt.BrushStyle.SolidPattern)
            self.scene.addRect(QRectF((base.cox)*8,(base.coy)*8, 8,8),QPen(),brush) 
        #trzeba zrobic bgtemps liste i dodawac QGraphicsRectItem zeby byylo szybciej i latwiej z dostepem do obietkow pozniej           
        



        self.graphicsView.show()








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Simulation()
    array = []
    ui.setupUi(Form, array)
    Form.show()
    sys.exit(app.exec())

