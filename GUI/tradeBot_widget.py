# Виджет отображения графических данных для matplotlib
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from popup_window_front import Ui_Form


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=90):  # dpi - размер осевых отметок
        self.parent = parent
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.subplots_adjust(left=0.07, bottom=0.07, right=0.95, top=0.94)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class CustomDialog(QtWidgets.QDialog):
    def __init__(self):
        super(CustomDialog, self).__init__()
        self._front_end = Ui_Form()
        self._front_end.setupUi(self)
        self.init_FrontEnd()

    def init_FrontEnd(self):
        self.setWindowTitle('INFO')
        self.setModal(True)
        self.is_visible = False

        self._front_end.link_label.setText(
            '<a href="https://stockanalysis.com/stocks/">ALL TICKERS ARE HERE</a>')
        self._front_end.link_label.setOpenExternalLinks(True)

        self._front_end.algorithm_info.setText('SOME INFO ABOUT ALGORITHM')
        self._front_end.algorithm_info.setVisible(False)

        self._front_end.info_show_hide_button.clicked.connect(self.popup_show_info)
        self._front_end.close_button.clicked.connect(self.popup_close)

    def popup_show_info(self):
        if self.is_visible:
            # Сокрытие текста
            self._front_end.algorithm_info.setVisible(False)
            self._front_end.info_show_hide_button.setText('SHOW INFO')
            self.is_visible = False
        else:
            # Показ текста
            self._front_end.algorithm_info.setVisible(True)
            self._front_end.info_show_hide_button.setText('HIDE INFO')
            self.is_visible = True

    def popup_close(self):
        self.close()
