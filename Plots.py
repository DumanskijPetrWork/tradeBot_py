import Strategy
import matplotlib.pyplot as plt
import Indicators
import Data
import datetime as dt


def plot_SMA(ticker, start, end, window):
    data = Data.getAllQuotes(ticker, start, end)
    data = data['Close']
    sma = Indicators.SMA(data, window)
    plt.plot(data)
    plt.plot(sma)
    plt.show()


def plot_twoSMA(ticker, start, end):
    data = Data.getAllQuotes(ticker, start, end)
    data = data['Close']
    smaShort = Indicators.SMA(data, 70)
    smaLong = Indicators.SMA(data, 140)
    plt.plot(data)
    plt.plot(smaShort)
    plt.plot(smaLong)
    plt.show()


def plot_EMA(ticker, start, end, window):
    data = Data.getAllQuotes(ticker, start, end)
    data = data['Close']
    ema = Indicators.SMA(data, window)
    plt.plot(data)
    plt.plot(ema)
    plt.show()


plot_EMA('SBER.ME', dt.datetime(2019, 1, 1), dt.datetime(2021, 5, 1), 100)


def plot_MACD(ticker, start, end, shortwindow, longwindow, signalwindow):
    data = Data.getAllQuotes(ticker, start, end)
    macd = Indicators.MACD(data['Close'], shortwindow, longwindow, signalwindow)

    plt.bar(data['Date'], macd[0])
    plt.bar(data['Date'], macd[1])
    plt.bar(data['Date'], macd[2])

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
