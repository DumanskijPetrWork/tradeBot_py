# -*- coding: utf-8 -*-
print('----WIN----')
from GUI.tradeBot_widget import MplCanvas
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 640)
        MainWindow.setMinimumSize(QtCore.QSize(810, 640))
        MainWindow.setStyleSheet("background-color: #2e2f33;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout.setSpacing(40)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.panel_and_spacer = QtWidgets.QVBoxLayout()
        self.panel_and_spacer.setSpacing(0)
        self.panel_and_spacer.setObjectName("panel_and_spacer")
        self.panel = QtWidgets.QSplitter(self.centralwidget)
        self.panel.setOrientation(QtCore.Qt.Vertical)
        self.panel.setHandleWidth(40)
        self.panel.setObjectName("panel")
        self.panel_input = QtWidgets.QSplitter(self.panel)
        self.panel_input.setOrientation(QtCore.Qt.Vertical)
        self.panel_input.setHandleWidth(20)
        self.panel_input.setObjectName("panel_input")
        self.ticker_edit = QtWidgets.QLineEdit(self.panel_input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ticker_edit.sizePolicy().hasHeightForWidth())
        self.ticker_edit.setSizePolicy(sizePolicy)
        self.ticker_edit.setMinimumSize(QtCore.QSize(250, 80))
        self.ticker_edit.setMaximumSize(QtCore.QSize(250, 80))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.ticker_edit.setFont(font)
        self.ticker_edit.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0  #5B86E5, stop:1 #36D1DC);\n"
            "border-radius: 10px;\n"
            "padding: 10px;")
        self.ticker_edit.setInputMethodHints(QtCore.Qt.ImhLatinOnly | QtCore.Qt.ImhPreferUppercase)
        self.ticker_edit.setFrame(False)
        self.ticker_edit.setObjectName("ticker_edit")
        self.dateEdit_from = QtWidgets.QDateEdit(self.panel_input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_from.sizePolicy().hasHeightForWidth())
        self.dateEdit_from.setSizePolicy(sizePolicy)
        self.dateEdit_from.setMinimumSize(QtCore.QSize(250, 80))
        self.dateEdit_from.setMaximumSize(QtCore.QSize(250, 80))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(20)
        self.dateEdit_from.setFont(font)
        self.dateEdit_from.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.dateEdit_from.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.dateEdit_from.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dateEdit_from.setStyleSheet("background-color: rgba( 255, 255, 255, 90%);\n"
                                         "border-radius: 10px;\n"
                                         "padding: 10px;")
        self.dateEdit_from.setFrame(False)
        self.dateEdit_from.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEdit_from.setMaximumDate(QtCore.QDate(3000, 12, 31))
        self.dateEdit_from.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dateEdit_from.setObjectName("dateEdit_from")
        self.dateEdit_to = QtWidgets.QDateEdit(self.panel_input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_to.sizePolicy().hasHeightForWidth())
        self.dateEdit_to.setSizePolicy(sizePolicy)
        self.dateEdit_to.setMinimumSize(QtCore.QSize(250, 80))
        self.dateEdit_to.setMaximumSize(QtCore.QSize(250, 80))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(20)
        self.dateEdit_to.setFont(font)
        self.dateEdit_to.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.dateEdit_to.setStyleSheet("background-color: rgba( 255, 255, 255, 90%);\n"
                                       "border-radius: 10px;\n"
                                       "padding: 10px;")
        self.dateEdit_to.setFrame(False)
        self.dateEdit_to.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEdit_to.setMaximumDate(QtCore.QDate(3000, 12, 31))
        self.dateEdit_to.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dateEdit_to.setObjectName("dateEdit_to")
        self.comboBox_alg = QtWidgets.QComboBox(self.panel_input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_alg.sizePolicy().hasHeightForWidth())
        self.comboBox_alg.setSizePolicy(sizePolicy)
        self.comboBox_alg.setMinimumSize(QtCore.QSize(250, 80))
        self.comboBox_alg.setMaximumSize(QtCore.QSize(250, 80))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_alg.setFont(font)
        self.comboBox_alg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_alg.setStyleSheet("QComboBox {\n"
                                        "    border-radius: 10px;\n"
                                        "    background-color: rgba( 255, 255, 255, 90%);\n"
                                        "    selection-color: #5B86E5;\n"
                                        "}\n"
                                        "\n"
                                        "QComboBox::drop-down \n"
                                        "{\n"
                                        "    border: none;\n"
                                        "    background-color: none;\n"
                                        "}")
        self.comboBox_alg.setObjectName("comboBox_alg")
        self.comboBox_time = QtWidgets.QComboBox(self.panel_input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_time.sizePolicy().hasHeightForWidth())
        self.comboBox_time.setSizePolicy(sizePolicy)
        self.comboBox_time.setMinimumSize(QtCore.QSize(250, 80))
        self.comboBox_time.setMaximumSize(QtCore.QSize(250, 80))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_time.setFont(font)
        self.comboBox_time.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_time.setStyleSheet("QComboBox {\n"
                                         "    border-radius: 10px;\n"
                                         "    background-color: rgba( 255, 255, 255, 90%);\n"
                                         "    selection-color: #d65c66;\n"
                                         "}\n"
                                         "\n"
                                         "QComboBox::drop-down \n"
                                         "{\n"
                                         "    border: none;\n"
                                         "    background-color: none;\n"
                                         "}")
        self.comboBox_time.setObjectName("comboBox_time")
        self.buttons = QtWidgets.QSplitter(self.panel)
        self.buttons.setOrientation(QtCore.Qt.Horizontal)
        self.buttons.setHandleWidth(20)
        self.buttons.setObjectName("buttons")
        self.info_button = QtWidgets.QPushButton(self.buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_button.sizePolicy().hasHeightForWidth())
        self.info_button.setSizePolicy(sizePolicy)
        self.info_button.setMinimumSize(QtCore.QSize(90, 80))
        self.info_button.setMaximumSize(QtCore.QSize(90, 80))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.info_button.setFont(font)
        self.info_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.info_button.setStyleSheet("QPushButton {\n"
                                       "    border-radius: 10px;\n"
                                       "    background-color: qlineargradient(\n"
                                       "spread:pad, x1: 0, y1: 0, x2: 1, y2: 0, \n"
                                       "stop: 0  #e37966, stop:1 #d64d59);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: qlineargradient(\n"
                                       "spread:pad, x1: 0, y1: 0, x2: 1, y2: 0, \n"
                                       "stop: 0  #e38676, stop:1 #d65c66);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: qlineargradient(\n"
                                       "spread:pad, x1: 0, y1: 0, x2: 1, y2: 0, \n"
                                       "stop: 0  #36D1DC, stop:1 #5B86E5);\n"
                                       "}")
        self.info_button.setAutoDefault(False)
        self.info_button.setFlat(False)
        self.info_button.setObjectName("info_button")
        self.run_button = QtWidgets.QPushButton(self.buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.run_button.sizePolicy().hasHeightForWidth())
        self.run_button.setSizePolicy(sizePolicy)
        self.run_button.setMinimumSize(QtCore.QSize(140, 80))
        self.run_button.setMaximumSize(QtCore.QSize(140, 80))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.run_button.setFont(font)
        self.run_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.run_button.setStyleSheet("QPushButton {\n"
                                      "    border-radius: 10px;\n"
                                      "    background-color: qlineargradient(\n"
                                      "spread:pad, x1: 0, y1: 0, x2: 1, y2: 0, \n"
                                      "stop: 0  #e37966, stop:1 #d64d59);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: qlineargradient(\n"
                                      "spread:pad, x1: 0, y1: 0, x2: 1, y2: 0, \n"
                                      "stop: 0  #e38676, stop:1 #d65c66);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: qlineargradient(\n"
                                      "spread:pad, x1: 0, y1: 0, x2: 1, y2: 0, \n"
                                      "stop: 0  #36D1DC, stop:1 #5B86E5);\n"
                                      "}")
        self.run_button.setAutoDefault(False)
        self.run_button.setFlat(False)
        self.run_button.setObjectName("run_button")
        self.panel_and_spacer.addWidget(self.panel)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.panel_and_spacer.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.panel_and_spacer)
        self.right_part = QtWidgets.QVBoxLayout()
        self.right_part.setSpacing(40)
        self.right_part.setObjectName("right_part")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("graphic_layout")
        self.graphic_field = MplCanvas(self.centralwidget)
        self.graphic_field.setMinimumSize(QtCore.QSize(400, 400))
        self.graphic_field.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.graphic_field.setObjectName("graphic_field")

        self.verticalLayout.addWidget(self.graphic_field)

        # # Панель инструментов (не нажимать на сохранение в виде файла, вылетает.)
        # self.tools_field = NavigationToolbar2QT(self.graphic_field, self.centralwidget)
        # self.tools_field.setMaximumSize(QtCore.QSize(16777215, 35))  # Размер панели
        # self.tools_field.setObjectName("tools_field")
        # self.verticalLayout.addWidget(self.tools_field)  # Отобразить панель в группе виджетов

        self.right_part.addLayout(self.verticalLayout)
        self.status_field = QtWidgets.QTextBrowser(self.centralwidget)
        self.status_field.setMinimumSize(QtCore.QSize(400, 80))
        self.status_field.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.status_field.setFont(font)
        self.status_field.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "border: 1px solid white;\n"
                                        "border-radius: 5px;\n"
                                        "padding: 10px;")
        self.status_field.setObjectName("status_field")
        self.right_part.addWidget(self.status_field)
        self.horizontalLayout.addLayout(self.right_part)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
