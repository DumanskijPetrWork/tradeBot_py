# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 540)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("background-color: #2e2f33;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 560, 1421, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        self.runButton.setGeometry(QtCore.QRect(20, 440, 250, 80))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.runButton.setFont(font)
        self.runButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.runButton.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(\n"
"spread:pad, x1: 0, y1: 0, x2: 1, y2: 0, \n"
"stop: 0  #e38676, stop:1 #d65c66);\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"spread:pad, x1: 0, y1: 0, x2: 1, y2: 0, \n"
"stop: 0  #e38a7b, stop:1 #d6636c);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(\n"
"spread:pad, x1: 0, y1: 0, x2: 1, y2: 0, \n"
"stop: 0  #e39486, stop:1 #d66b74);\n"
"    }")
        self.runButton.setAutoDefault(False)
        self.runButton.setFlat(False)
        self.runButton.setObjectName("runButton")
        self.tickerEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.tickerEdit.setGeometry(QtCore.QRect(20, 20, 250, 80))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.tickerEdit.setFont(font)
        self.tickerEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tickerEdit.setStyleSheet("background-color: qlineargradient(spread:pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0  #5B86E5, stop:1 #36D1DC);\n"
"border-radius: 10px;\n"
"padding: 10px;")
        self.tickerEdit.setMaxLength(32767)
        self.tickerEdit.setFrame(False)
        self.tickerEdit.setCursorPosition(6)
        self.tickerEdit.setObjectName("tickerEdit")
        self.dateEdit_from = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_from.setGeometry(QtCore.QRect(20, 120, 250, 80))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.dateEdit_from.setFont(font)
        self.dateEdit_from.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dateEdit_from.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.dateEdit_from.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dateEdit_from.setStyleSheet("background-color: rgba( 255, 255, 255,90%);\n"
"border-radius: 10px;\n"
"padding: 10px;\n"
"font: 75 24pt \"Montserrat\";")
        self.dateEdit_from.setFrame(False)
        self.dateEdit_from.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEdit_from.setObjectName("dateEdit_from")
        self.dateEdit_to = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_to.setGeometry(QtCore.QRect(20, 220, 250, 80))
        self.dateEdit_to.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dateEdit_to.setStyleSheet("background-color: rgba( 255, 255, 255,90%);\n"
"border-radius: 10px;\n"
"padding: 10px;\n"
"font: 75 24pt \"Montserrat\";")
        self.dateEdit_to.setFrame(False)
        self.dateEdit_to.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEdit_to.setObjectName("dateEdit_to")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 320, 250, 80))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox.setStyleSheet("QComboBox {\n"
"    border-radius: 10px;\n"
"    background-color: rgba( 255, 255, 255,90%);\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QComboBox::drop-down \n"
"{\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    width: 40px;\n"
"    height: 80px;\n"
"    background-color: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"  color: rgb(85, 170, 255);    \n"
"  background-color: #373e4e;\n"
"  padding: 10px;\n"
"  selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.comboBox.setCurrentText("ALGORITHM")
        self.comboBox.setFrame(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.GraphicField = QtWidgets.QWidget(self.centralwidget)
        self.GraphicField.setGeometry(QtCore.QRect(310, 20, 650, 380))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        self.GraphicField.setFont(font)
        self.GraphicField.setObjectName("GraphicField")
        self.statesField = QtWidgets.QLabel(self.centralwidget)
        self.statesField.setGeometry(QtCore.QRect(310, 440, 650, 80))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.statesField.setFont(font)
        self.statesField.setStyleSheet("color: rgb(255, 255, 255);")
        self.statesField.setText("")
        self.statesField.setObjectName("statesField")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Trade Bot"))
        self.runButton.setText(_translate("MainWindow", "RUN"))
        self.tickerEdit.setText(_translate("MainWindow", "TICKER"))
        self.comboBox.setItemText(0, _translate("MainWindow", "ALGORITHM"))
        self.comboBox.setItemText(1, _translate("MainWindow", "SMA"))
        self.comboBox.setItemText(2, _translate("MainWindow", "buyAndHold"))
        self.comboBox.setItemText(3, _translate("MainWindow", "twoSMA"))
        self.comboBox.setItemText(4, _translate("MainWindow", "EMA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
