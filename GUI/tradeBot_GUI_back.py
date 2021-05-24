import sys
from PyQt5 import QtWidgets
from tradeBot_GUI_front import Ui_MainWindow
from DATA.tradeBot_parser_static import *


class BackEnd(QtWidgets.QMainWindow):
    def __init__(self):
        super(BackEnd, self).__init__()
        self._front_end = Ui_MainWindow()
        self._front_end.setupUi(self)
        self.init_FrontEnd()

    def init_FrontEnd(self):
        # Заголовок окна
        self.setWindowTitle("Trade Bot")

        # Текст кнопки
        self._front_end.run_button.setText("RUN")

        # Текст поля ввода тикера
        self._front_end.ticker_edit.setPlaceholderText("TICKER")

        # Инициализация начальной даты
        self._front_end.dateEdit_from.setDate(dt.date.today() - dt.timedelta(days=30))
        self._front_end.dateEdit_from.setMaximumDate(dt.date.today())

        # Инициализация конечной даты
        self._front_end.dateEdit_to.setDate(dt.date.today())
        self._front_end.dateEdit_to.setMaximumDate(dt.date.today())

        # Инициализация списка алгоритмов
        self._front_end.comboBox_alg.setCurrentText("ALGORITHM")
        for _ in ["ALGORITHM", ""]:
            self._front_end.comboBox_alg.addItem(_)

        # Инициализцаия списков таймфреймов
        self._front_end.comboBox_time.setCurrentText("TIME FRAME")
        for _ in ["TIME FRAME",
                  "1m", "2m", "5m",
                  "15m", "30m", "1h",
                  "1d", "1wk", "1mo"]:
            self._front_end.comboBox_time.addItem(_)

        # Инициализация строки состояний
        self._front_end.status_field.setText('Select:  Ticker, Start date, End date, Algorithm, Time frame\n'
                                             'Press "RUN"')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = BackEnd()
    application.show()
    sys.exit(app.exec_())

# убираем все упоминания retranslateUi в файле tradeBot_GUI_front
