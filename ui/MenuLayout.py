# Form implementation generated from reading ui file '.\MenuLayout.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication


class Ui_Form(object):



    def clickedbutton(self): # checks if user closed the window with start or 'X' button
        self.condition = True
        app = QApplication.instance()
        app.closeAllWindows()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 633)
        Form.setToolTipDuration(-1)
        Form.setStyleSheet("\n"
"background-color: rgb(211, 211, 211);")
        self.layoutWidget = QtWidgets.QWidget(Form)

        self.condition = False

        self.layoutWidget.setGeometry(QtCore.QRect(9, 3, 481, 611))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.line_3 = QtWidgets.QFrame(self.layoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalSlider_dimX = QtWidgets.QSlider(self.layoutWidget)
        self.horizontalSlider_dimX.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.SizeHorCursor))
        self.horizontalSlider_dimX.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.horizontalSlider_dimX.setAcceptDrops(False)
        self.horizontalSlider_dimX.setToolTipDuration(2)
        self.horizontalSlider_dimX.setMinimum(10)
        self.horizontalSlider_dimX.setMaximum(100)
        self.horizontalSlider_dimX.setSingleStep(1)
        self.horizontalSlider_dimX.setPageStep(1)
        self.horizontalSlider_dimX.setProperty("value", 2)
        self.horizontalSlider_dimX.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider_dimX.setInvertedAppearance(False)
        self.horizontalSlider_dimX.setInvertedControls(False)
        self.horizontalSlider_dimX.setTickPosition(QtWidgets.QSlider.TickPosition.TicksAbove)
        self.horizontalSlider_dimX.setTickInterval(10)
        self.horizontalSlider_dimX.setObjectName("horizontalSlider_dimX")
        self.horizontalLayout_2.addWidget(self.horizontalSlider_dimX)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.dimX_prev = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        self.dimX_prev.setFont(font)
        self.dimX_prev.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.dimX_prev.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.dimX_prev.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.dimX_prev.setObjectName("dimX_prev")
        self.horizontalLayout_3.addWidget(self.dimX_prev)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.horizontalSlider_dimY = QtWidgets.QSlider(self.layoutWidget)
        self.horizontalSlider_dimY.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.SizeHorCursor))
        self.horizontalSlider_dimY.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.horizontalSlider_dimY.setAcceptDrops(False)
        self.horizontalSlider_dimY.setToolTipDuration(2)
        self.horizontalSlider_dimY.setMinimum(10)
        self.horizontalSlider_dimY.setMaximum(100)
        self.horizontalSlider_dimY.setSingleStep(1)
        self.horizontalSlider_dimY.setPageStep(1)
        self.horizontalSlider_dimY.setProperty("value", 2)
        self.horizontalSlider_dimY.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider_dimY.setInvertedAppearance(False)
        self.horizontalSlider_dimY.setInvertedControls(False)
        self.horizontalSlider_dimY.setTickPosition(QtWidgets.QSlider.TickPosition.TicksAbove)
        self.horizontalSlider_dimY.setTickInterval(10)
        self.horizontalSlider_dimY.setObjectName("horizontalSlider_dimY")
        self.horizontalLayout_4.addWidget(self.horizontalSlider_dimY)
        self.dimY_prev = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        self.dimY_prev.setFont(font)
        self.dimY_prev.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.dimY_prev.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.dimY_prev.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.dimY_prev.setObjectName("dimY_prev")
        self.horizontalLayout_4.addWidget(self.dimY_prev)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.line_5 = QtWidgets.QFrame(self.layoutWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_5.addWidget(self.line_5)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.line_4 = QtWidgets.QFrame(self.layoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_5.addWidget(self.line_4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.horizontalSlider_MonsterAmnt = QtWidgets.QSlider(self.layoutWidget)
        self.horizontalSlider_MonsterAmnt.setMaximum(15)
        self.horizontalSlider_MonsterAmnt.setPageStep(1)
        self.horizontalSlider_MonsterAmnt.setProperty("value", 1)
        self.horizontalSlider_MonsterAmnt.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider_MonsterAmnt.setObjectName("horizontalSlider_MonsterAmnt")
        self.horizontalLayout_6.addWidget(self.horizontalSlider_MonsterAmnt)
        self.MonsterAmnt_prev = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        self.MonsterAmnt_prev.setFont(font)
        self.MonsterAmnt_prev.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.MonsterAmnt_prev.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.MonsterAmnt_prev.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.MonsterAmnt_prev.setObjectName("MonsterAmnt_prev")
        self.horizontalLayout_6.addWidget(self.MonsterAmnt_prev)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.horizontalSlider_StartFood = QtWidgets.QSlider(self.layoutWidget)
        self.horizontalSlider_StartFood.setMaximum(15)
        self.horizontalSlider_StartFood.setPageStep(1)
        self.horizontalSlider_StartFood.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider_StartFood.setObjectName("horizontalSlider_StartFood")
        self.horizontalLayout_7.addWidget(self.horizontalSlider_StartFood)
        self.StartFood_prev = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        self.StartFood_prev.setFont(font)
        self.StartFood_prev.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.StartFood_prev.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.StartFood_prev.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.StartFood_prev.setObjectName("StartFood_prev")
        self.horizontalLayout_7.addWidget(self.StartFood_prev)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.horizontalSlider_FSpawnRate = QtWidgets.QSlider(self.layoutWidget)
        self.horizontalSlider_FSpawnRate.setMaximum(10)
        self.horizontalSlider_FSpawnRate.setPageStep(1)
        self.horizontalSlider_FSpawnRate.setProperty("value", 1)
        self.horizontalSlider_FSpawnRate.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider_FSpawnRate.setTickPosition(QtWidgets.QSlider.TickPosition.TicksAbove)
        self.horizontalSlider_FSpawnRate.setTickInterval(5)
        self.horizontalSlider_FSpawnRate.setObjectName("horizontalSlider_FSpawnRate")
        self.horizontalLayout_8.addWidget(self.horizontalSlider_FSpawnRate)
        self.FSpawnRate_prev = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        self.FSpawnRate_prev.setFont(font)
        self.FSpawnRate_prev.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.FSpawnRate_prev.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.FSpawnRate_prev.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.FSpawnRate_prev.setObjectName("FSpawnRate_prev")
        self.horizontalLayout_8.addWidget(self.FSpawnRate_prev)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.line_7 = QtWidgets.QFrame(self.layoutWidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_9.addWidget(self.line_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.line_6 = QtWidgets.QFrame(self.layoutWidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_9.addWidget(self.line_6)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_10.addWidget(self.label_5)
        self.horizontalSlider_TribeAmnt = QtWidgets.QSlider(self.layoutWidget)
        self.horizontalSlider_TribeAmnt.setMinimum(2)
        self.horizontalSlider_TribeAmnt.setMaximum(3)
        self.horizontalSlider_TribeAmnt.setPageStep(1)
        self.horizontalSlider_TribeAmnt.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider_TribeAmnt.setTickPosition(QtWidgets.QSlider.TickPosition.NoTicks)
        self.horizontalSlider_TribeAmnt.setObjectName("horizontalSlider_TribeAmnt")
        self.horizontalLayout_10.addWidget(self.horizontalSlider_TribeAmnt)
        self.TribeAmount_prev = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        self.TribeAmount_prev.setFont(font)
        self.TribeAmount_prev.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.TribeAmount_prev.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.TribeAmount_prev.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TribeAmount_prev.setObjectName("TribeAmount_prev")
        self.horizontalLayout_10.addWidget(self.TribeAmount_prev)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        self.horizontalSlider_initPopulation = QtWidgets.QSlider(self.layoutWidget)
        self.horizontalSlider_initPopulation.setMinimum(1)
        self.horizontalSlider_initPopulation.setMaximum(5)
        self.horizontalSlider_initPopulation.setPageStep(1)
        self.horizontalSlider_initPopulation.setProperty("value", 2)
        self.horizontalSlider_initPopulation.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider_initPopulation.setTickPosition(QtWidgets.QSlider.TickPosition.TicksAbove)
        self.horizontalSlider_initPopulation.setTickInterval(1)
        self.horizontalSlider_initPopulation.setObjectName("horizontalSlider_initPopulation")
        self.horizontalLayout_11.addWidget(self.horizontalSlider_initPopulation)
        self.InitPopulation_prev = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        self.InitPopulation_prev.setFont(font)
        self.InitPopulation_prev.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.InitPopulation_prev.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.InitPopulation_prev.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.InitPopulation_prev.setObjectName("InitPopulation_prev")
        self.horizontalLayout_11.addWidget(self.InitPopulation_prev)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clickedbutton)
        self.verticalLayout.addWidget(self.pushButton)

        def limiter(): #limits tribe amount accordingly to map area
            if self.horizontalSlider_dimX.value()*self.horizontalSlider_dimY.value() < 400:
                self.horizontalSlider_TribeAmnt.setMaximum(3)
            elif self.horizontalSlider_dimX.value()*self.horizontalSlider_dimY.value() < 900:
                self.horizontalSlider_TribeAmnt.setMaximum(6)
            else:
                self.horizontalSlider_TribeAmnt.setMaximum(15)




        


        self.retranslateUi(Form)
        self.horizontalSlider_dimX.valueChanged.connect(limiter)
        self.horizontalSlider_dimY.valueChanged.connect(limiter)
        self.horizontalSlider_dimX.valueChanged['int'].connect(self.dimX_prev.setNum) # type: ignore
        self.horizontalSlider_dimY.valueChanged['int'].connect(self.dimY_prev.setNum) # type: ignore
        self.horizontalSlider_TribeAmnt.valueChanged['int'].connect(self.TribeAmount_prev.setNum) # type: ignore
        self.horizontalSlider_MonsterAmnt.valueChanged['int'].connect(self.MonsterAmnt_prev.setNum) # type: ignore
        self.horizontalSlider_StartFood.valueChanged['int'].connect(self.StartFood_prev.setNum) # type: ignore
        self.horizontalSlider_initPopulation.valueChanged['int'].connect(self.InitPopulation_prev.setNum) # type: ignore
        self.horizontalSlider_FSpawnRate.valueChanged['int'].connect(self.FSpawnRate_prev.setNum) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Menu"))
        self.label_3.setText(_translate("Form", "Board settings"))
        self.label.setText(_translate("Form", "Board Dimension X"))
        self.dimX_prev.setText(_translate("Form", "10"))
        self.label_2.setText(_translate("Form", "Board Dimension Y"))
        self.dimY_prev.setText(_translate("Form", "10"))
        self.label_4.setText(_translate("Form", "Map settings"))
        self.label_6.setText(_translate("Form", "Monster Amount"))
        self.MonsterAmnt_prev.setText(_translate("Form", "1"))
        self.label_7.setText(_translate("Form", "Starting Food"))
        self.StartFood_prev.setText(_translate("Form", "0"))
        self.label_10.setText(_translate("Form", "Food Spawn Rate"))
        self.FSpawnRate_prev.setText(_translate("Form", "1"))
        self.label_8.setText(_translate("Form", "Tribe setting"))
        self.label_5.setText(_translate("Form", "Tribe Amount"))
        self.TribeAmount_prev.setText(_translate("Form", "2"))
        self.label_9.setText(_translate("Form", "Initial Population"))
        self.InitPopulation_prev.setText(_translate("Form", "2"))
        self.pushButton.setText(_translate("Form", "Start"))




if __name__ == "__main__": #debugging tool
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
