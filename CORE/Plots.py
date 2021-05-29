import matplotlib.pyplot as plt
import Indicators
from DATA.tradeBot_parser_static import get_quotes_tab
import datetime as dt


def plot_SMA(ticker, start, end, window):
    data = get_quotes_tab(ticker, start, end)
    data = data['Close']
    sma = Indicators.SMA(data, window)
    plt.plot(data)
    plt.plot(sma)
    plt.show()


def plot_twoSMA(ticker, start, end):
    data = get_quotes_tab(ticker, start, end)
    data = data['Close']
    smaShort = Indicators.SMA(data, 70)
    smaLong = Indicators.SMA(data, 140)
    plt.plot(data)
    plt.plot(smaShort)
    plt.plot(smaLong)
    plt.show()


def plot_EMA(ticker, start, end, window):
    data = get_quotes_tab(ticker, start, end)
    data = data['Close']
    ema = Indicators.SMA(data, window)
    plt.plot(data)
    plt.plot(ema)
    plt.show()


plot_EMA('SBER.ME', dt.datetime(2019, 1, 1), dt.datetime(2021, 5, 1), 100)


def plot_MACD(ticker, start, end, shortwindow, longwindow, signalwindow):
    data = get_quotes_tab(ticker, start, end)
    macd = Indicators.MACD(data['Close'], shortwindow, longwindow, signalwindow)

    plt.bar(data['Date'], macd[0])
    plt.bar(data['Date'], macd[1])
    plt.bar(data['Date'], macd[2])

    plt.show()


def plot_RSI(ticker, start, end, window):
    data = Data.getAllQuotes(ticker, start, end)
    data = data['Close']

    rsi = Indicators.RSI(data, window)

    plt.plot(rsi)
    plt.plot([30] * len(data))
    plt.plot([70] * len(data))

    plt.show()


def plot_DEMA(ticker, start, end, window):
    data = Data.getAllQuotes(ticker, start, end)
    data = data['Close']

    dema = Indicators.DEMA(data, window)

    plt.plot(data)
    plt.plot(dema)

    plt.show()


def plot_TEMA(ticker, start, end, window):
    data = Data.getAllQuotes(ticker, start, end)
    data = data['Close']

    tema = Indicators.TEMA(data, window)

    plt.plot(data)
    plt.plot(tema)

    plt.show()


def plot_RSI(ticker, start, end, window):
    data = get_quotes_tab(ticker, start, end)
    data = data['Close']

    rsi = Indicators.RSI(data, window)

    plt.plot(rsi)
    plt.plot([30] * len(data))
    plt.plot([70] * len(data))

    plt.show()


def plot_DEMA(ticker, start, end, window):
    data = get_quotes_tab(ticker, start, end)
    data = data['Close']

    dema = Indicators.DEMA(data, window)

    plt.plot(data)
    plt.plot(dema)

    plt.show()


def plot_TEMA(ticker, start, end, window):
    data = get_quotes_tab(ticker, start, end)
    data = data['Close']

    tema = Indicators.TEMA(data, window)

    plt.plot(data)
    plt.plot(tema)

    plt.show()


import pandas_datareader as web
import datetime as dt
import plotly.graph_objs as go

ticker = 'TSLA'

start = dt.datetime(2020, 1, 1)
end = dt.datetime.now()

df = web.DataReader(ticker, "yahoo", start, end)

df = df.reset_index()

fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Adj Close']

)])

# fig.show()
