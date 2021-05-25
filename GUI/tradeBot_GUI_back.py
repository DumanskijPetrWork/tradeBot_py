import string
import sys
from PyQt5 import QtWidgets
from tradeBot_GUI_front import Ui_MainWindow
from DATA.tradeBot_parser_static import *
# from CORE import *  # Будущий импорт для графиков и matplotlib / plotly


class BackEnd(QtWidgets.QMainWindow):
    def __init__(self):
        super(BackEnd, self).__init__()

        # Предыдущие значения полей для предотвращения излишних запросов
        self.ticker_prev = ''
        self.date_from_prev = dt.date.today() - dt.timedelta(days=30)
        self.date_to_prev = dt.date.today()
        self.time_frame = 'TIME FRAME'

        self.data = []  # Данные котировок

        self._front_end = Ui_MainWindow()
        self._front_end.setupUi(self)
        self.init_FrontEnd()

    # Инициализация функционала
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
        self._front_end.status_field.setText('Select:  Ticker, Start date, End date, Algorithm, Time frame;\n'
                                             'Press "RUN".')

        # Обработка нажатия на кнопку
        self._front_end.run_button.clicked.connect(self.build_data)

    # Функция получения данных при нажатии кнопки
    def build_data(self):
        print("Button's been pressed.\n")
        ticker = self._front_end.ticker_edit.text().upper().strip(' ' + string.punctuation)

        # Форматирование дат
        start_date_raw = dt.datetime.strftime(dt.datetime.strptime(
            self._front_end.dateEdit_from.text(), '%d.%m.%Y'),
            '%Y-%m-%d')
        end_date_raw = dt.datetime.strftime(dt.datetime.strptime(
            self._front_end.dateEdit_to.text(), '%d.%m.%Y'),
            '%Y-%m-%d')

        # Автокоррекция дат
        start_date = min(start_date_raw, end_date_raw)
        end_date = max(start_date_raw, end_date_raw)

        algorithm = self._front_end.comboBox_alg.currentText()
        time_frame = self._front_end.comboBox_time.currentText()

        print(f"ticker: {ticker}\n"
              f"start_date: {start_date}\n"
              f"end_date: {end_date}\n"
              f"algorithm: {algorithm}\n"
              f"time_frame: {time_frame}\n")

        try:
            if (self.ticker_prev != ticker or
                    self.date_from_prev != self._front_end.dateEdit_from.text() or
                    self.date_to_prev != self._front_end.dateEdit_to.text() or
                    self.time_frame != time_frame):
                self.data = get_quotes_list(ticker, start_date, end_date)  # Получение котировок

                self.ticker_prev = ticker
                self.date_from_prev = self._front_end.dateEdit_from.text()
                self.date_to_prev = self._front_end.dateEdit_to.text()
                self.time_frame = time_frame
        except Exception as err:
            print(f'{err}\n')
            self._front_end.status_field.setText(f'<span style=\"color:#ff0000;\">WARNING:</span> {err}')
        else:
            print("Data's been received.\n")
            self._front_end.status_field.setText("Data's been received.")
            self.graphic_show()

    def graphic_show(self):
        print(self.data)


if __name__ == '__main__':
    print('---start---\n')
    app = QtWidgets.QApplication(sys.argv)
    application = BackEnd()
    application.show()
    sys.exit(app.exec_())

# убираем все упоминания retranslateUi в файле tradeBot_GUI_front
