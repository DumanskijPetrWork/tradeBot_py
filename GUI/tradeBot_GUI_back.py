import string
import sys
from PyQt5 import QtWidgets
from tradeBot_GUI_front import Ui_MainWindow
from DATA.tradeBot_parser_static import *
from CORE import *  # Будущий импорт для графиков и matplotlib / plotly
from PyQt5 import QtCore
import random


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

        # Текст кнопок
        self._front_end.run_button.setText("RUN")  # RUN
        self._front_end.info_button.setText("INFO")  # INFO

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

        # Обработка нажатий на кнопки
        self._front_end.run_button.clicked.connect(self.build_data)  # RUN
        self._front_end.info_button.clicked.connect(self.graphic_dynamic_show)  # INFO

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
                # self.data = get_quotes_list(ticker, start_date, end_date)  # Получение котировок

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

    # Функция построения графика
    def graphic_show(self):
        print(f'{self.data}\n')
        x_list = range(len(self.data))

        try:
            self._front_end.graphic_field.axes.cla()
            self._front_end.graphic_field.axes.plot(x_list, self.data, 'r')
            self._front_end.graphic_field.draw()
        except Exception as err:
            print(f'{err}\n')
            self._front_end.status_field.setText(f'<span style=\"color:#ff0000;\">WARNING:</span> {err}')
        else:
            print("Plot's been built.\n")
            self._front_end.status_field.setText("Plot's been built.")

    # Тестовая функция
    def graphic_dynamic_show(self):
        n_data = 50
        self.xdata = list(range(n_data))
        self.ydata = [random.randint(0, 10) for _ in range(n_data)]
        self.update_plot()

        self.timer = QtCore.QTimer()
        self.timer.setInterval(80)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    # Тестовая вспомогательная функция
    def update_plot(self):
        # Drop off the first y element, append a new one.
        self.ydata = self.ydata[1:] + [random.randint(0, 10)]
        self._front_end.graphic_field.axes.cla()  # Clear the canvas.
        self._front_end.graphic_field.axes.plot(self.xdata, self.ydata, 'r')
        # Trigger the canvas to update and redraw.
        self._front_end.graphic_field.draw()

    # Показать информацию об алгоритме
    def show_info(self):
        print("Dialog window's been opened.\n")
        QtWidgets.QMessageBox.about(self, "INFO", "Info will be there soon:")
        # text, ok = QtWidgets.QInputDialog.getText(self, 'INFO', 'Info will be there soon:')


if __name__ == '__main__':
    print('---start---\n')
    app = QtWidgets.QApplication(sys.argv)
    application = BackEnd()
    application.show()
    sys.exit(app.exec_())

# Убираем все упоминания retranslateUi в файле tradeBot_GUI_front, переносим import MplCanvas новерх
# QMessageBox - information / warning
# QDialog (Box)

# Добавлять в файл tradeBot_GUI_front:
# from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
#
#         Панель инструментов (не нажимать на сохранение в виде файла, вылетает.)
#         self.tools_field = NavigationToolbar2QT(self.graphic_field, self.centralwidget)
#         self.tools_field.setMaximumSize(QtCore.QSize(16777215, 35))  # Размер панели
#         self.tools_field.setObjectName("tools_field")
#         self.verticalLayout.addWidget(self.tools_field)  # Отобразить панель в группе виджетов

# Toolbar можно переписать
