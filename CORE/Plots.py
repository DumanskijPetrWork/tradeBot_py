import matplotlib.pyplot as plt
import Indicators
from DATA.tradeBot_parser_static import get_quotes_tab
import datetime as dt

# я обозначил дата за 0, тк не обозначать нельзя
# мне ее оставить пустой, чтобы она как глобальная переменная была,или добавить как аргумент?
data = 0


# параметр n отвечает за покупку - продажу акций
# если n = 2 - покупать
#      n = 1 - ничего
#      n = 0 - продавать


def plot_SMA(ticker, start, end, window):
    sma = Indicators.SMA(data['Close'], window)

    if (data['Close'][-1] <= sma[-1] and data['Close'][-2] > sma[-2]):
        n = 0
    elif (data['Close'][-1] >= sma[-1] and data['Close'][-2] < sma[-2]):
        n = 2
    else:
        n = 1

    return n, \
           (lambda blank: blank.plot(sma)), \
           (lambda blank: blank.plot(data['Close']))


# 70 and 140
def plot_twoSMA(ticker, start, end, window1, window2):
    smaShort = Indicators.SMA(data['Close'], window1)
    smaLong = Indicators.SMA(data['Close'], window2)

    if (smaShort[-1] <= smaLong[-1] and smaShort[-2] > smaLong[-2]):
        n = 0
    elif (smaShort[-1] >= smaLong[-1] and smaShort[-2] < smaLong[-2]):
        n = 2
    else:
        n = 1

    return n, \
           (lambda blank: blank.plot(smaShort)), \
           (lambda blank: blank.plot(smaLong)), \
           (lambda blank: blank.plot(data['Close']))


def plot_EMA(ticker, start, end, window):
    ema = Indicators.EMA(data['Close'], window)

    if (data['Close'][-1] <= ema[-1] and data['Close'][-2] > ema[-2]):
        n = 0
    elif (data['Close'][-1] >= ema[-1] and data['Close'][-2] < ema[-2]):
        n = 2
    else:
        n = 1

    return n, \
           (lambda blank: blank.plot(ema)), \
           (lambda blank: blank.plot(data['Close']))


def plot_MACD(ticker, start, end, shortwindow, longwindow, signalwindow):
    macd = Indicators.MACD(data['Close'], shortwindow, longwindow, signalwindow)
    macdsignal = macd[1]
    macdhist = macd[2]

    if (macdhist[-1] <= macdsignal[-1] and macdhist[-2] > macdsignal[-2]):
        n = 0
    elif (macdhist[-1] >= macdsignal[-1] and macdhist[-2] < macdsignal[-2]):
        n = 2
    else:
        n = 1

    return n, \
           (lambda blank: blank.bar(macd[0])), \
           (lambda blank: blank.bar(macd[1])), \
           (lambda blank: blank.bar(macd[2]))


def plot_RSI(ticker, start, end, window):
    rsi = Indicators.RSI(data['Close'], window)

    if rsi[-1] > 70:
        n = 0
    elif rsi[-1] < 30:
        n = 2
    else:
        n = 1

    return n, \
           (lambda blank: blank.plot(rsi)), \
           (lambda blank: blank.plot([30] * len(data['Close']))), \
           (lambda blank: blank.plot([70] * len(data['Close'])))


def plot_DEMA(ticker, start, end, window):
    dema = Indicators.DEMA(data['Close'], window)

    if (data['Close'][-1] <= dema[-1] and data['Close'][-2] > dema[-2]):
        n = 0
    elif (data['Close'][-1] >= dema[-1] and data['Close'][-2] < dema[-2]):
        n = 2
    else:
        n = 1

    return n, \
           (lambda blank: blank.plot(dema)), \
           (lambda blank: blank.plot(data['Close']))


def plot_TEMA(ticker, start, end, window):
    tema = Indicators.TEMA(data['Close'], window)

    if (data['Close'][-1] <= tema[-1] and data['Close'][-2] > tema[-2]):
        n = 0
    elif (data['Close'][-1] >= tema[-1] and data['Close'][-2] < tema[-2]):
        n = 2
    else:
        n = 1

    return n, \
           (lambda blank: blank.plot(tema)), \
           (lambda blank: blank.plot(data['Close']))


def plot_bulls(ticker, start, end, window):
    bulls = Indicators.Bulls_power(data, window)

    if (bulls[-1] < bulls[-2] and bulls[-1] > 0 and bulls[-2] > 0):
        n = 0
    else:
        n = 1

    return n, \
           (lambda blank: blank.plot(bulls)), \
           (lambda blank: blank.plot(data['Close']))


def plot_bears(ticker, start, end, window):
    bears = Indicators.Bears_power(data, window);

    if (bears[-1] > bears[-2] and bears[-1] < 0 and bears[-2] < 0):
        n = 2
    else:
        n = 1

    return n, \
           (lambda blank: blank.plot(bears)), \
           (lambda blank: blank.plot(data['Close']))


def plot_ER(ticker, start, end, window):
    ema = Indicators.Elder_Rays(data, window)[0]
    bulls = Indicators.Elder_Rays(data, window)[1]
    bears = Indicators.Elder_Rays(data, window)[2]

    if (bears[-1] > bears[-2] and bears[-1] < 0 and bears[-2] < 0):
        n = 2
    elif (bulls[-1] < bulls[-2] and bulls[-1] > 0 and bulls[-2] > 0):
        n = 0
    else:
        n = 1

    return n, \
           (lambda blank: blank.plot(ema)), \
           (lambda blank: blank.plot(bulls)), \
           (lambda blank: blank.plot(bears)), \
           (lambda blank: blank.plot(data['Close']))


def plot_MI(ticker, start, end, window):
    mi = Indicators.MI(data, window)
    mislice = mi[-20:-1]
    flag = 0

    for i in mislice:
        if (mi[i] > 26.5 and mi[i] < 27):
            flag = 1

    if (flag == 1 and mi[-1] < 26.5):
        n = 2
    else:
        n = 1

    return n, \
           (lambda blank: blank.plot(mi)), \
           (lambda blank: blank.plot([27] * len(data['Close']))), \
           (lambda blank: blank.plot([26.5] * len(data['Close']))) \
               (lambda blank: blank.plot(data['Close']))


def plot_CHV(ticker, start, end, window):
    chv = Indicators.CHV(data, window)

    if all(chv[i - 1] <= chv[i] for i in range(10)):
        n = 2
    elif all(chv[i - 1] >= chv[i] for i in range(10)):
        n = 0
    else:
        n = 1

    return n, \
           (lambda blank: blank.plot(chv)), \
           (lambda blank: blank.plot(data['Close']))
