import string
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtGui import QStandardItem, QColor
from tradeBot_GUI_front import Ui_MainWindow
from tradeBot_widget import CustomDialog
from DATA.tradeBot_parser_static import *
from DATA.tradeBot_parser_static_yf import *
from DATA.tradeBot_parser_dynamic import get_dynamic_quotes
from CORE.Plots import *


class BackEnd(QtWidgets.QMainWindow):
    def __init__(self):
        super(BackEnd, self).__init__()

        # Предыдущие значения полей для предотвращения излишних запросов
        self.ticker_prev = ''
        self.date_from_prev = dt.date.today() - dt.timedelta(days=360)
        self.date_to_prev = dt.date.today()
        self.time_frame = '1d'

        self.data = []  # Данные котировок
        self.data_len = 0  # Данные котировок
        self.extraData = []  # Данные котировок за период + 1 год
        self.timer = QtCore.QTimer()  # Таймер для динамики

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
        self._front_end.dateEdit_from.setDate(dt.date.today() - dt.timedelta(days=360))
        self._front_end.dateEdit_from.setMaximumDate(dt.date.today())

        # Инициализация конечной даты
        self._front_end.dateEdit_to.setDate(dt.date.today())
        self._front_end.dateEdit_to.setMaximumDate(dt.date.today())

        # Инициализация списка алгоритмов
        self._front_end.comboBox_alg.setCurrentText("ALGORITHM")
        self.model_comboBox_alg = self._front_end.comboBox_alg.model()
        for name in ["ALGORITHM",
                     "DYNAMIC",
                     "SMA",
                     "twoSMA",
                     "EMA",
                     "DEMA",
                     "TEMA",
                     "RSI",
                     "MACD",
                     "bullsPOWER",
                     "bearsPOWER",
                     "Elder-rays",
                     "MASS INDEX",
                     "CHV"]:
            item = QStandardItem(name)
            item.setBackground(QColor('white'))
            self.model_comboBox_alg.appendRow(item)

        # Инициализцаия списков таймфреймов
        self._front_end.comboBox_time.setCurrentText("TIME FRAME")
        self.model_comboBox_time = self._front_end.comboBox_time.model()
        for name in ["TIME FRAME",
                     "5m", "15m", "30m", "1h",
                     "1d", "1wk", "1mo"]:
            item = QStandardItem(name)
            item.setBackground(QColor('white'))
            self.model_comboBox_time.appendRow(item)

        # Инициализация строки состояний
        self._front_end.status_field.setText('Select:  Ticker, Start date, End date, Algorithm, Time frame;\n'
                                             'Press "RUN".')

        # Обработка нажатий на кнопки
        self._front_end.run_button.clicked.connect(self.button_pressed)  # RUN
        self._front_end.info_button.clicked.connect(self.show_info)  # INFO

    # Функция назначения действия
    def button_pressed(self):
        time_frame = self._front_end.comboBox_time.currentText()
        algorithm = self._front_end.comboBox_alg.currentText()
        if (time_frame != 'TIME FRAME') and (algorithm == 'ALGORITHM'):
            self.build_data_y()
        else:
            self.build_data()

    # Функция получения yahoo-данных при нажатии кнопки
    def build_data_y(self):
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

        if ticker != '':
            try:
                if (self.ticker_prev != ticker or
                        self.date_from_prev != self._front_end.dateEdit_from.text() or
                        self.date_to_prev != self._front_end.dateEdit_to.text() or
                        self.time_frame != time_frame):
                    self.ticker_prev = ticker
                    self.date_from_prev = self._front_end.dateEdit_from.text()
                    self.date_to_prev = self._front_end.dateEdit_to.text()
                    self.time_frame = time_frame
                    self.data = get_quotesY_tab(ticker, start_date, end_date, time_frame)  # Получение котировок
            except Exception as err:
                print(f'{err}\n')
                self._front_end.status_field.setText(f'<span style=\"color:#ff0000;\">WARNING:</span> {err}')
            else:
                print("Data's been received.\n")
                self._front_end.status_field.setText("Data's been received.")
                self.graphic_show(ticker, start_date, end_date)
        else:
            print('No ticker\n')
            self._front_end.status_field.setText("<span style=\"color:#ff0000;\">WARNING:</span> specify the ticker")

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
        prev_start_date_raw = dt.datetime.strftime(dt.datetime.strptime(
            self._front_end.dateEdit_from.text(), '%d.%m.%Y') - dt.timedelta(days=360),
            '%Y-%m-%d')
        prev_end_date_raw = dt.datetime.strftime(dt.datetime.strptime(
            self._front_end.dateEdit_to.text(), '%d.%m.%Y') - dt.timedelta(days=360),
            '%Y-%m-%d')

        # Автокоррекция дат
        start_date = min(start_date_raw, end_date_raw)
        end_date = max(start_date_raw, end_date_raw)
        prev_date = min(start_date, prev_start_date_raw, prev_end_date_raw)

        algorithm = self._front_end.comboBox_alg.currentText()
        time_frame = self._front_end.comboBox_time.currentText()

        print(f"ticker: {ticker}\n"
              f"start_date: {start_date}\n"
              f"end_date: {end_date}\n"
              f"algorithm: {algorithm}\n"
              f"time_frame: {time_frame}\n")

        if ticker != '':
            try:
                if (self.ticker_prev != ticker or
                        self.date_from_prev != self._front_end.dateEdit_from.text() or
                        self.date_to_prev != self._front_end.dateEdit_to.text() or
                        self.time_frame != time_frame):
                    self.ticker_prev = ticker
                    self.date_from_prev = self._front_end.dateEdit_from.text()
                    self.date_to_prev = self._front_end.dateEdit_to.text()
                    self.time_frame = time_frame
                    self.data = get_quotes_tab(ticker, start_date, end_date)  # Получение котировок
                    if not self.data.empty:
                        self.data_len = len(self.data)
                        print(f'data_len: {self.data_len}\n')
                    self.extraData = get_quotes_tab(ticker, prev_date, end_date)  # Получение котировок
            except Exception as err:
                print(f'{err}\n')
                self._front_end.status_field.setText(f'<span style=\"color:#ff0000;\">WARNING:</span> {err}')
            else:
                print("Data's been received.\n")
                self._front_end.status_field.setText("Data's been received.")
                self.graphic_show(ticker, start_date, end_date)
        else:
            print('No ticker\n')
            self._front_end.status_field.setText("<span style=\"color:#ff0000;\">WARNING:</span> specify the ticker")

    # Функция построения графика
    def graphic_show(self, _ticker, _start_date, _end_date):
        print(f'{self.data}\n')
        self.timer.stop()

        try:
            y_data = []
            open_data = self.data['Open'].values
            close_data = self.data['Close'].values
            for price in range(len(open_data)):
                y_data.append(open_data[price])
                y_data.append(close_data[price])
            x_data = range(len(y_data))
        except Exception as err:
            print(f'{err}\n')
            self._front_end.status_field.setText('<span style=\"color:#ff0000;\">WARNING:</span> no such ticker')
        else:
            try:
                self._front_end.graphic_field.axes.cla()  # Очистка поля

                # Основная часть выбора алгоритма и построения графика
                graphic_name = self._front_end.comboBox_alg.currentText()

                if graphic_name == 'ALGORITHM':
                    print("No algorithm's been selected\n")
                    self._front_end.graphic_field.axes.plot(x_data, y_data, c='black', zorder=1)
                    # self._front_end.graphic_field.axes.scatter(x_data, y_data,
                    #                                            marker='^', c='g',
                    #                                            s=4000 / (len(x_data) + 100),
                    #                                            zorder=5)

                elif graphic_name == 'DYNAMIC':
                    print("Dynamic show has been selected\n")
                    self.graphic_dynamic_show(_ticker)

                elif graphic_name == 'SMA':
                    print("Algorithm 'SMA' has been selected\n")

                    result, plot1, plot2 = plot_SMA(self.data_len, self.extraData)
                    plot1(self._front_end.graphic_field.axes)
                    plot2(self._front_end.graphic_field.axes)
                    print(f'result: {result}')
                    if result == 0:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#ff0000;\">SELL</span>')
                    elif result == 1:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#fff700;\">WAIT</span>')
                    elif result == 2:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#70ff00;\">BUY</span>')

                elif graphic_name == 'twoSMA':
                    print("Algorithm 'twoSMA' has been selected\n")

                    result, plot1, plot2, plot3 = plot_twoSMA(self.data_len, self.extraData)
                    plot1(self._front_end.graphic_field.axes)
                    plot2(self._front_end.graphic_field.axes)
                    plot3(self._front_end.graphic_field.axes)
                    print(f'result: {result}')
                    if result == 0:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#ff0000;\">SELL</span>')
                    elif result == 1:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#fff700;\">WAIT</span>')
                    elif result == 2:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#70ff00;\">BUY</span>')

                elif graphic_name == 'EMA':
                    print("Algorithm 'EMA' has been selected\n")

                    result, plot1, plot2 = plot_EMA(self.data_len, self.extraData)
                    plot1(self._front_end.graphic_field.axes)
                    plot2(self._front_end.graphic_field.axes)
                    print(f'result: {result}')
                    if result == 0:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#ff0000;\">SELL</span>')
                    elif result == 1:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#fff700;\">WAIT</span>')
                    elif result == 2:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#70ff00;\">BUY</span>')

                elif graphic_name == 'DEMA':
                    print("Algorithm 'DEMA' has been selected\n")

                    result, plot1, plot2 = plot_DEMA(self.data_len, self.extraData)
                    plot1(self._front_end.graphic_field.axes)
                    plot2(self._front_end.graphic_field.axes)
                    print(f'result: {result}')
                    if result == 0:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#ff0000;\">SELL</span>')
                    elif result == 1:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#fff700;\">WAIT</span>')
                    elif result == 2:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#70ff00;\">BUY</span>')

                elif graphic_name == 'TEMA':
                    print("Algorithm 'TEMA' has been selected\n")

                    result, plot1, plot2 = plot_TEMA(self.data_len, self.extraData)
                    plot1(self._front_end.graphic_field.axes)
                    plot2(self._front_end.graphic_field.axes)
                    print(f'result: {result}')
                    if result == 0:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#ff0000;\">SELL</span>')
                    elif result == 1:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#fff700;\">WAIT</span>')
                    elif result == 2:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#70ff00;\">BUY</span>')

                elif graphic_name == 'RSI':
                    print("Algorithm 'RSI' has been selected\n")

                    result, plot1, plot2, plot3 = plot_RSI(self.data_len, self.extraData)
                    self._front_end.graphic_field.axes.set_ylim([0, 100])
                    plot1(self._front_end.graphic_field.axes)
                    plot2(self._front_end.graphic_field.axes)
                    plot3(self._front_end.graphic_field.axes)
                    print(f'result: {result}')
                    if result == 0:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#ff0000;\">SELL</span>')
                    elif result == 1:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#fff700;\">WAIT</span>')
                    elif result == 2:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#70ff00;\">BUY</span>')

                elif graphic_name == 'MACD':
                    print("Algorithm 'MACD' has been selected\n")

                    result, plot1, plot2, plot3 = plot_MACD(self.data_len, self.extraData)
                    plot1(self._front_end.graphic_field.axes)
                    plot2(self._front_end.graphic_field.axes)
                    plot3(self._front_end.graphic_field.axes)
                    print(f'result: {result}')
                    if result == 0:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#ff0000;\">SELL</span>')
                    elif result == 1:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#fff700;\">WAIT</span>')
                    elif result == 2:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#70ff00;\">BUY</span>')

                elif graphic_name == 'bullsPOWER':
                    print("Algorithm 'bullsPOWER' has been selected\n")

                    result, plot1, plot2 = plot_bulls(self.data_len, self.extraData)
                    plot1(self._front_end.graphic_field.axes)
                    plot2(self._front_end.graphic_field.axes)
                    print(f'result: {result}')
                    if result == 0:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#ff0000;\">SELL</span>')
                    elif result == 1:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#fff700;\">WAIT</span>')
                    elif result == 2:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#70ff00;\">BUY</span>')

                elif graphic_name == 'bearsPOWER':
                    print("Algorithm 'bearsPOWER' has been selected\n")

                    result, plot1, plot2 = plot_bears(self.data_len, self.extraData)
                    plot1(self._front_end.graphic_field.axes)
                    plot2(self._front_end.graphic_field.axes)
                    print(f'result: {result}')
                    if result == 0:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#ff0000;\">SELL</span>')
                    elif result == 1:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#fff700;\">WAIT</span>')
                    elif result == 2:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#70ff00;\">BUY</span>')

                elif graphic_name == 'Elder-rays':
                    print("Algorithm 'Elder-rays' has been selected\n")

                    result, plot1, plot2, plot3, plot4 = plot_ER(self.data_len, self.extraData)
                    plot1(self._front_end.graphic_field.axes)
                    plot2(self._front_end.graphic_field.axes)
                    plot3(self._front_end.graphic_field.axes)
                    plot4(self._front_end.graphic_field.axes)
                    print(f'result: {result}')
                    if result == 0:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#ff0000;\">SELL</span>')
                    elif result == 1:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#fff700;\">WAIT</span>')
                    elif result == 2:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#70ff00;\">BUY</span>')

                elif graphic_name == 'MASS INDEX':
                    print("Algorithm 'MASS INDEX' has been selected\n")

                    result, plot1, plot2, plot3 = plot_MI(self.data_len, self.extraData)
                    plot1(self._front_end.graphic_field.axes)
                    plot2(self._front_end.graphic_field.axes)
                    plot3(self._front_end.graphic_field.axes)

                    print(f'result: {result}')
                    if result == 0:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#ff0000;\">SELL</span>')
                    elif result == 1:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#fff700;\">WAIT</span>')
                    elif result == 2:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#70ff00;\">BUY</span>')

                elif graphic_name == 'CHV':
                    print("Algorithm 'CHV' has been selected\n")

                    result, plot1, plot2 = plot_CHV(self.data_len, self.extraData)
                    plot1(self._front_end.graphic_field.axes)
                    plot2(self._front_end.graphic_field.axes)
                    print(f'result: {result}')
                    if result == 0:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#ff0000;\">SELL</span>')
                    elif result == 1:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#fff700;\">WAIT</span>')
                    elif result == 2:
                        self._front_end.status_field.setText(
                            'RECOMMENDATION: <span style=\"color:#70ff00;\">BUY</span>')

                else:
                    print('No such algorithm or data\n')

            except Exception as err:
                print(f'{err}\n')
                self._front_end.status_field.setText(f'<span style=\"color:#ff0000;\">WARNING:</span> {err}')
            else:
                self._front_end.graphic_field.draw()  # Отображение графика
                print("Plot's been built.\n")
                if len(x_data) == 0:
                    self._front_end.status_field.setText(
                        f'<span style=\"color:#ff0000;\">WARNING:</span> decrease the time interval')

    # Построить динамический график
    def graphic_dynamic_show(self, _ticker):
        self.n = 300

        # Форматирование дат
        start_date_raw = dt.datetime.strptime(
            self._front_end.dateEdit_from.text(), '%d.%m.%Y')
        end_date_raw = dt.datetime.strptime(
            self._front_end.dateEdit_to.text(), '%d.%m.%Y')

        # Автокоррекция дат
        start_date = min(start_date_raw, end_date_raw)
        end_date = max(start_date_raw, end_date_raw)

        if (end_date - start_date).days < self.n:
            start_date -= dt.timedelta(days=self.n)

        try:
            data = get_quotes_list(_ticker,
                                   start_date,
                                   end_date)
        except Exception as err:
            print(f'{err}\n')
            self._front_end.status_field.setText(f'<span style=\"color:#ff0000;\">WARNING:</span> {err}')
        else:
            self.duration = len(data)
            self.iter = self.n
            self.xdata = range(self.n)
            self.ydata = data[:self.n]
            self.quotes_generator = get_dynamic_quotes(data[self.n:])
            self.update_plot()

            self.timer.setInterval(1000)
            self.timer.timeout.connect(self.update_plot)
            self.timer.start()

    # Функция динамического обновления графика
    def update_plot(self):
        if self.iter < self.duration:
            self.iter += 1
            self.ydata = self.ydata[1:] + [next(self.quotes_generator)]

            self._front_end.graphic_field.axes.cla()
            self._front_end.graphic_field.axes.plot(self.xdata, self.ydata, 'black')

            self._front_end.graphic_field.draw()
        else:
            self.timer.stop()

    # Показать информацию об алгоритме
    def show_info(self):

        # В инициализации добавить поля self для дополнительных переменных алгоритмов

        print("Dialog window's been opened.\n")
        self.popup = CustomDialog()

        graphic_name = self._front_end.comboBox_alg.currentText()
        if graphic_name == 'ALGORITHM':
            self.popup._front_end.algorithm_info.setText(
f'''График котировок тикера {self._front_end.ticker_edit.text().upper().strip(' ' + string.punctuation)} за указанный период''')

        elif graphic_name == 'DYNAMIC':
            self.popup._front_end.algorithm_info.setText(
'''Эмуляция динамического изменения цены 
за определенный промежуток времени''')

        elif graphic_name == 'SMA':
            self.popup._front_end.algorithm_info.setText(
'''SMA (Simple Moving Average) - это простая скользящая средняя. 
Она максимально прозрачно обозначает основные тенденции, 
а также побочные ценовые изменения.

Период: обычно период берется 5, 13 и 21 для более чувствительных 
индикаторов и 52, 100 и 200 для долгосрочной перспективы. 
Чем больше период, тем меньше риск.

Стратегия: если цена пересекает медленную скользящую 
сверху вниз, то стоит продавать. В обратном случае покупать''')

        elif graphic_name == 'twoSMA':
            self.popup._front_end.algorithm_info.setText(
'''two_SMA (Simple Moving Average) - это простая скользящая средняя, 
однако вместо цены берется быстро скользящая средняя. 
Она максимально прозрачно обозначает основные тенденции, 
а также побочные ценовые изменения.

Период: обычно для медленной скользящей берется период 
5, 13 и 21 для более чувствительных индикаторов и 
52, 100 и 200 для долгосрочной перспективы. 
Чем больше период, тем меньше риск. 
А для быстрой скользящей берется значение до половины медленной. 
Чем больше разница, тем более чувствительный получится индикатор.

Стратегия: если цена пересекает медленную скользящую 
сверху вниз, то стоит продавать. В обратном случае покупать''')

        elif graphic_name == 'EMA':
            self.popup._front_end.algorithm_info.setText(
'''EMA (Exponential Moving Average) – разновидность скользящей средней, 
рассчитываемая экспоненциально. В сравнении с простой, экспонента 
придает гораздо больше важности текущим значениям, чем старым, 
имевшим место некоторое время назад.

Период: обычно период берется до 25 – быстрые, от 25 до 50 – средние 
и от 50 и более – медленные. Чем больше период, тем меньше риск.

Стратегия: если цена пересекает медленную скользящую сверху вниз, 
то стоит продавать. В обратном случае покупать''')

        elif graphic_name == 'DEMA':
            self.popup._front_end.algorithm_info.setText(
'''DEMA (Double exponential moving average) – дважды взятая EMA, 
является более продвинутой, чем традиционные скользящие средние, 
и реагирует быстрее, что делает её более востребованной у трейдеров.

Период: обычно период берется до 25 – быстрые, 
от 25 до 50 – средние и от 50 и более – медленные. 
Чем больше период, тем меньше риск.

Стратегия: если цена пересекает медленную скользящую 
сверху вниз, то стоит продавать. В обратном случае покупать''')

        elif graphic_name == 'TEMA':
            self.popup._front_end.algorithm_info.setText(
'''TEMA (Triple exponential moving average) – трижды взятая EMA, 
является более продвинутой, чем традиционные скользящие средние, 
и реагирует быстрее, что делает её более востребованной у трейдеров.

Период: обычно период берется до 25 – быстрые, 
от 25 до 50 – средние и от 50 и более – медленные. 
Чем больше период, тем меньше риск.

Стратегия: если цена пересекает медленную скользящую 
сверху вниз, то стоит продавать. В обратном случае покупать''')

        elif graphic_name == 'RSI':
            self.popup._front_end.algorithm_info.setText(
'''RSI позиционируется как индекс перекупленности/перепроданности.

Еще его используют для поиска дивергенций – простыми словами, 
если индикатор идет вверх, а общий график вниз, или наоборот, 
то, возможно, намечается разворот.

Период: обычно период берется до 25 – быстрые, от 25 до 50 – средние 
и от 50 и более – медленные. Чем больше период, тем меньше риск.

Стратегия: индикатор возвращает значения от 0 до 100, считается, 
что значения ниже 30 говорят о недооценности рынка (нужно покупать), 
а выше 70 – о перекупленности (нужно продавать)''')

        elif graphic_name == 'MACD':
            self.popup._front_end.algorithm_info.setText(
'''MACD (Moving average convergence/divergence) - это 
схождение/расхождение скользящих средних.

Период: довольно сложный для настройки обычному пользователю, 
поэтому рекомендуется взять классический [12,26,9] 
или [5,35,5] для более рискованного варианта.

Стратегия: если гистограмма пересекает сигнальную линию 
сверху вниз, то стоит продавать. В обратном случае покупать''')

        elif graphic_name == 'bullsPOWER':
            self.popup._front_end.algorithm_info.setText(
'''Индикатор Bulls Power – простой и эффективный инструмент анализа, 
применение которого позволяет определять настроения покупателей 
(«быков») в обозначенный период времени. 
Чаще всего применяется в связке с осциллятором Bears Power, 
работающему по такому же принципу, только в отношении продавцов.

Период: обычно период берется до 25 – быстрые, от 25 до 50 – средние 
и от 50 и более – медленные. Чем больше период, тем меньше риск.

Стратегия: если столбцы гистограммы падают, 
но значения пока больше 0, то стоит продавать''')

        elif graphic_name == 'bearsPOWER':
            self.popup._front_end.algorithm_info.setText(
'''Индикатор Bears Power – классический осциллятор, определяющий 
силу продавцов («медведей») рынка в конкретный временной период. 

Период: обычно период берется до 25 – быстрые, от 25 до 50 – средние 
и от 50 и более – медленные. Чем больше период, тем меньше риск.

Стратегия: если столбцы гистограммы растут, 
но значения пока меньше 0, то стоит покупать''')

        elif graphic_name == 'Elder-rays':
            self.popup._front_end.algorithm_info.setText(
'''Индикатор Лучи Элдера – комплексный индикатор, разработанный 
американским трейдером советского происхождения А.Элдером. 
Цена определяется в результате компромисса между покупателями, 
нейтральными игроками, готовыми вступить в рынок в любой момент, и продавцами. 
Moving Average являет собой среднюю величину этого консенсуса.

Период: обычно период берется до 25 – быстрые, от 25 до 50 – средние 
и от 50 и более – медленные. Чем больше период, тем меньше риск.

Стратегия: если столбцы гистограммы растут, но значения пока меньше 0, то стоит покупать; 
если столбцы гистограммы падают, но значения пока больше 0, то стоит продавать''')

        elif graphic_name == 'MASS INDEX':
            self.popup._front_end.algorithm_info.setText(
'''Индикатор Mass Index (MI) – технический индикатор, использование 
которого дает возможность спрогнозировать разворот тренда за счет 
анализа динамики изменений диапазона цен. 
Был создан для определения уровня волатильности на рынке.

Период: алгоритм достаточно сложный, поэтому 
рекомендуется взять значение по умолчанию 9.

Стратегия: если кривая пересекает линию 27 снизу вверх, 
а потом линию 26,5 сверху вниз, то следует покупать''')

        elif graphic_name == 'CHV':
            self.popup._front_end.algorithm_info.setText(
'''Индикатор волатильности Чайкина (Chaikin Volatility, CHV) –  индикатор, 
с помощью которого определяют волатильность рынка.

Период: обычно период берется до 25 – быстрые, от 25 до 50 – средние 
и от 50 и более – медленные. Чем больше период, тем меньше риск.

Стратегия: начало роста индикатора может свидетельствовать 
о формировании очередного максимума цены. В таком случае волатильность 
будет увеличиваться до тех пор, пока этот экстремум не будет установлен. 
Быстрое снижение кривой CHV говорит о замедлении текущей тенденции. 
Вероятно, в ближайшее время произойдет сильная коррекция или откат цены.''')

        self.popup.show()


if __name__ == '__main__':
    print('---start---\n')
    app = QtWidgets.QApplication(sys.argv)
    application = BackEnd()
    application.show()
    sys.exit(app.exec_())

# Убираем все упоминания retranslateUi в файле tradeBot_GUI_front, переносим import MplCanvas новерх

# Добавлять в файл tradeBot_GUI_front:
# from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
#
#         Панель инструментов (не нажимать на сохранение в виде файла, вылетает.)
#         self.tools_field = NavigationToolbar2QT(self.graphic_field, self.centralwidget)
#         self.tools_field.setMaximumSize(QtCore.QSize(16777215, 35))  # Размер панели
#         self.tools_field.setObjectName("tools_field")
#         self.verticalLayout.addWidget(self.tools_field)  # Отобразить панель в группе виджетов
