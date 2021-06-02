import matplotlib.pyplot as plt
import numpy as np
from CORE.Indicators import *
from DATA.tradeBot_parser_static import get_quotes_tab
import datetime as dt


# я обозначил дата за 0, тк не обозначать нельзя
# мне ее оставить пустой, чтобы она как глобальная переменная была,или добавить как аргумент?

# параметр n отвечает за покупку - продажу акций
# если n = 2 - покупать
#      n = 1 - ничего
#      n = 0 - продавать


def plot_SMA(lenData, data, window=50):
    sma = SMA(data['Close'], window)

    sma = sma[(-lenData):]
    data = data[(-lenData):]

    if (data['Close'].values[-1] <= sma[-1] and data['Close'].values[-2] > sma[-2]):
        n = 0
    elif (data['Close'].values[-1] >= sma[-1] and data['Close'].values[-2] < sma[-2]):
        n = 2
    else:
        n = 1

    return n, \
           lambda blank: blank.plot(data['Date'], sma), \
           lambda blank: blank.plot(data['Date'], data['Close'])


# 70 and 140
def plot_twoSMA(lenData, data, window1=70, window2=140):
    smaShort = SMA(data['Close'], window1)
    smaLong = SMA(data['Close'], window2)

    smaShort = smaShort[(-lenData):]
    smaLong = smaLong[(-lenData):]
    data = data[(-lenData):]

    if (smaShort[-1] <= smaLong[-1] and smaShort[-2] > smaLong[-2]):
        n = 0
    elif (smaShort[-1] >= smaLong[-1] and smaShort[-2] < smaLong[-2]):
        n = 2
    else:
        n = 1

    return n, \
           lambda blank: blank.plot(data['Date'], smaShort), \
           lambda blank: blank.plot(data['Date'], smaLong), \
           lambda blank: blank.plot(data['Date'], data['Close'])


def plot_EMA(lenData, data, window=50):
    ema = EMA(data['Close'], window)

    ema = ema[(-lenData):]
    data = data[(-lenData):]

    if (data['Close'].values[-1] <= ema[-1] and data['Close'].values[-2] > ema[-2]):
        n = 0
    elif (data['Close'].values[-1] >= ema[-1] and data['Close'].values[-2] < ema[-2]):
        n = 2
    else:
        n = 1

    return n, \
           lambda blank: blank.plot(data['Date'], ema), \
           lambda blank: blank.plot(data['Date'], data['Close'])


def plot_DEMA(lenData, data, window=50):
    dema = DEMA(data['Close'], window)

    dema = dema[(-lenData):]
    data = data[(-lenData):]

    if (data['Close'].values[-1] <= dema[-1] and data['Close'].values[-2] > dema[-2]):
        n = 0
    elif (data['Close'].values[-1] >= dema[-1] and data['Close'].values[-2] < dema[-2]):
        n = 2
    else:
        n = 1

    return n, \
           lambda blank: blank.plot(data['Date'], dema), \
           lambda blank: blank.plot(data['Date'], data['Close'])


def plot_TEMA(lenData, data, window=50):
    tema = TEMA(data['Close'], window)

    tema = tema[(-lenData):]
    data = data[(-lenData):]

    if (data['Close'].values[-1] <= tema[-1] and data['Close'].values[-2] > tema[-2]):
        n = 0
    elif (data['Close'].values[-1] >= tema[-1] and data['Close'].values[-2] < tema[-2]):
        n = 2
    else:
        n = 1

    return n, \
           lambda blank: blank.plot(data['Date'], tema), \
           lambda blank: blank.plot(data['Date'], data['Close'])


def plot_RSI(lenData, data, window=50):
    rsi = RSI(data['Close'], window)

    rsi = rsi[(-lenData):]
    data = data[(-lenData):]

    if rsi[-1] > 70:
        n = 0
    elif rsi[-1] < 30:
        n = 2
    else:
        n = 1

    return n, \
           lambda blank: blank.plot(data['Date'], rsi), \
           lambda blank: blank.plot(data['Date'], [30] * len(data['Close'])), \
           lambda blank: blank.plot(data['Date'], [70] * len(data['Close']))


def plot_MACD(lenData, data, shortwindow=12, longwindow=26, signalwindow=9):
    macd_all = MACD(data['Close'], shortwindow, longwindow, signalwindow)

    macd = macd_all[0]
    macdsignal = macd_all[1]
    macdhist = macd_all[2]

    macd = macd[(-lenData):]
    macdsignal = macdsignal[(-lenData):]
    macdhist = macdhist[(-lenData):]
    data = data[(-lenData):]


    if (macdhist[-1] <= macdsignal[-1] and macdhist[-2] > macdsignal[-2]):
        n = 0
    elif (macdhist[-1] >= macdsignal[-1] and macdhist[-2] < macdsignal[-2]):
        n = 2
    else:
        n = 1

    return n, \
           lambda blank: blank.plot(data['Date'], macdsignal, zorder=3), \
           lambda blank: blank.bar(data['Date'], macdhist, zorder=2),\
           lambda blank: blank.bar(data['Date'], macd, zorder=1)



def plot_bulls(lenData, data, window=50):
    bulls = Bulls_power(data, window)

    bulls = bulls[(-lenData):]
    data = data[(-lenData):]

    if (bulls.values[-1] < bulls.values[-2] and bulls.values[-1] > 0 and bulls.values[-2] > 0):
        n = 0
    else:
        n = 1

    return n, \
           (lambda blank: blank.bar(data['Date'], bulls)), \
           (lambda blank: blank.plot(data['Date'], data['Close']))


def plot_bears(lenData, data, window=50):
    bears = Bears_power(data, window);

    bears = bears[(-lenData):]
    data = data[(-lenData):]

    if (bears.values[-1] > bears.values[-2] and bears.values[-1] < 0 and bears.values[-2] < 0):
        n = 2
    else:
        n = 1

    return n, \
           (lambda blank: blank.bar(data['Date'], bears)), \
           (lambda blank: blank.plot(data['Date'], data['Close']))


def plot_ER(lenData, data, window=50):
    ema = Elder_Rays(data, window)[0]
    bulls = Elder_Rays(data, window)[1]
    bears = Elder_Rays(data, window)[2]

    ema = ema[(-lenData):]
    bears = bears[(-lenData):]
    bulls = bulls[(-lenData):]
    data = data[(-lenData):]

    if (bears.values[-1] > bears.values[-2] and bears.values[-1] < 0 and bears.values[-2] < 0):
        n = 2
    elif (bulls.values[-1] < bulls.values[-2] and bulls.values[-1] > 0 and bulls.values[-2] > 0):
        n = 0
    else:
        n = 1

    return n, \
           (lambda blank: blank.plot(data['Date'], ema)), \
           (lambda blank: blank.bar(data['Date'], bulls)), \
           (lambda blank: blank.bar(data['Date'], bears)), \
           (lambda blank: blank.plot(data['Date'], data['Close']))


def plot_MI(lenData, data, window=9):
    mi = MI(data, window)

    result = []
    for i in range(len(mi) - 49):
        result.append(sum(mi[i + 25:i + 50]))

    mi = result

    mi = mi[(-lenData):]
    data = data[(-lenData):]

    mislice = mi[-20:-1]
    flag = 0

    for i in range(len(mislice)):
        if (mi[i] > 26.5 and mi[i] < 27):
            flag = 1

    if (flag == 1 and mi[-1] < 26.5):
        n = 2
    else:
        n = 1

    return n, \
           lambda blank: blank.plot(data['Date'], mi), \
           lambda blank: blank.plot(data['Date'], [27] * len(data['Close'])), \
           lambda blank: blank.plot(data['Date'], [26.5] * len(data['Close']))


def plot_CHV(lenData, data, window=50):
    chv = CHV(data, window)

    chv = chv[(-lenData):]
    data = data[(-lenData):]

    if all(chv[i - 1] <= chv[i] for i in range(10)):
        n = 2
    elif all(chv[i - 1] >= chv[i] for i in range(10)):
        n = 0
    else:
        n = 1

    return n, \
           (lambda blank: blank.plot(data['Date'], chv)), \
           (lambda blank: blank.plot(data['Date'], data['Close']))
