# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(293, 180)
        self.mainLayout = QtWidgets.QVBoxLayout(Form)
        self.mainLayout.setObjectName("mainLayout")

        self.group_3_radio = QtWidgets.QHBoxLayout()
        self.group_3_radio.setObjectName("group_3_radio")
        self.group_4_buttons = QtWidgets.QHBoxLayout()
        self.group_4_buttons.setObjectName("group_4_buttons")
        self.group_5_bottom = QtWidgets.QVBoxLayout()
        self.group_5_bottom.setObjectName("group_5_bottom")

        self.radioButton_1 = QtWidgets.QRadioButton(Form)
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_1.setText('LOW RISK')
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setText('MEDIUM RISK')
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.setText('HIGH RISK')

        self.info_show_hide_button = QtWidgets.QPushButton(Form)
        self.info_show_hide_button.setObjectName("info_show_hide_button")
        self.info_show_hide_button.setText('SHOW INFO')
        self.close_button = QtWidgets.QPushButton(Form)
        self.close_button.setObjectName("close_button")
        self.close_button.setText('CLOSE')

        self.link_label = QtWidgets.QLabel(Form)
        self.link_label.setObjectName("link_label")
        self.algorithm_info = QtWidgets.QLabel(Form)
        self.algorithm_info.setObjectName("algorithm_info")

        self.group_3_radio.addWidget(self.radioButton_1)
        self.group_3_radio.addWidget(self.radioButton_2)
        self.group_3_radio.addWidget(self.radioButton_3)
        self.mainLayout.addLayout(self.group_3_radio)
        self.group_4_buttons.addWidget(self.info_show_hide_button)
        self.group_4_buttons.addWidget(self.close_button)
        self.group_5_bottom.addLayout(self.group_4_buttons)
        self.group_5_bottom.addWidget(self.link_label)
        self.group_5_bottom.addWidget(self.algorithm_info)
        self.mainLayout.addLayout(self.group_5_bottom)

        QtCore.QMetaObject.connectSlotsByName(Form)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
