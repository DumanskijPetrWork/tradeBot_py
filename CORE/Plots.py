import matplotlib.pyplot as plt
import Indicators
from DATA.tradeBot_parser_static import get_quotes_tab
import datetime as dt

#я обозначил дата за 0, тк не обозначать нельзя
# мне ее оставить пустой, чтобы она как глобальная переменная была,или добавить как аргумент?
data = 0

def plot_SMA(ticker, start, end, window):
    sma = Indicators.SMA(data['Close'], window)

    return 0, \
           (lambda blank: blank.plot(sma)), \
           (lambda blank: blank.plot(data['Close']))


#70 and 140
def plot_twoSMA(ticker, start, end, window1, window2):
    smaShort = Indicators.SMA(data['Close'], window1)
    smaLong = Indicators.SMA(data['Close'], window2)

    return 0, \
           (lambda blank: blank.plot(smaShort)), \
           (lambda blank: blank.plot(smaLong)), \
           (lambda blank: blank.plot(data['Close']))


def plot_EMA(ticker, start, end, window):
    ema = Indicators.EMA(data['Close'], window)

    return 0, \
           (lambda blank: blank.plot(ema)), \
           (lambda blank: blank.plot(data['Close']))


def plot_MACD(ticker, start, end, shortwindow, longwindow, signalwindow):
    macd = Indicators.MACD(data['Close'], shortwindow, longwindow, signalwindow)

    return 0, \
           (lambda blank: blank.bar(macd[0])), \
           (lambda blank: blank.bar(macd[1])), \
           (lambda blank: blank.bar(macd[2]))

def plot_RSI(ticker, start, end, window):
    rsi = Indicators.RSI(data['Close'], window)

    return 0, \
           (lambda blank: blank.plot(rsi)), \
           (lambda blank: blank.plot([30] * len(data['Close']))), \
           (lambda blank: blank.plot([70] * len(data['Close'])))


def plot_DEMA(ticker, start, end, window):
    dema = Indicators.DEMA(data['Close'], window)

    return 0, \
           (lambda blank: blank.plot(dema)), \
           (lambda blank: blank.plot(data['Close']))


def plot_TEMA(ticker, start, end, window):
    tema = Indicators.TEMA(data['Close'], window)

    return 0, \
           (lambda blank: blank.plot(tema)), \
           (lambda blank: blank.plot(data['Close']))


def plot_bulls(ticker, start, end, window):
    bulls = Indicators.Bulls_power(data, window)

    return 0, \
           (lambda blank: blank.plot(bulls)), \
           (lambda blank: blank.plot(data['Close']))


def plot_bears(ticker, start, end, window):
    bears = Indicators.Bears_power(data, window);

    return 0, \
           (lambda blank: blank.plot(bears)), \
           (lambda blank: blank.plot(data['Close']))


def plot_ER(ticker, start, end, window):
    ema = Indicators.Elder_Rays(data, window)[0]
    bulls = Indicators.Elder_Rays(data, window)[1]
    bears = Indicators.Elder_Rays(data, window)[2]

    return 0, \
           (lambda blank: blank.plot(ema)), \
           (lambda blank: blank.plot(bulls)), \
           (lambda blank: blank.plot(bears)), \
           (lambda blank: blank.plot(data['Close']))


def plot_MI(ticker, start, end, window):
    mi = Indicators.MI(data, window)

    return 0, \
           (lambda blank: blank.plot(mi)), \
           (lambda blank: blank.plot(data['Close']))


def plot_CHV(ticker, start, end, window):
    chv = Indicators.CHV(data, window)

    return 0, \
           (lambda blank: blank.plot(chv)), \
           (lambda blank: blank.plot(data['Close']))
