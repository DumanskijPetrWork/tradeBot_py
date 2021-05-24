# Статический парсер котировок

import pandas_datareader as web
import datetime as dt
import yfinance as yf
import json


# Таблица котировок указанной ценной бумаги за период, таймфрейм 1d
# Формат: Date, Adj Close, Close, High, Low, Open, Volume
# Получить список котировок тикера за указанный период
def get_quotes(_ticker, _start, _end):
    try:
        data = web.DataReader([_ticker], "yahoo", _start, _end)
    except Exception as err:
        print(f'При получении списка котировок возникла ошибка: {err}')
    else:
        quotes = []
        # Фильтр нужных категорий
        data_lite = data.drop(['Adj Close', 'High', 'Low', 'Volume'], 1)
        # Котировки открытия
        open_data = data_lite[('Open', _ticker)].values
        # Котировки закрытия
        close_data = data_lite[('Close', _ticker)].values

        # Добавление котировок в список quotes
        for price in range(len(open_data)):
            quotes.append((open_data[price], close_data[price]))
            # quotes.append(open_data[price])
            # quotes.append(close_data[price])

        return json.dumps(quotes, indent=2)  # json формат
    return None


# Таблица котировок yahoo указанной ценной бумаги за период
# с возможностью выбора интервала
# Формат: Date, Open, High, Low, Close, Adj Close, Volume
def get_quotesY(_ticker, _start, _end, _timeframe='15m'):
    try:
        data = yf.download(_ticker, _start, _end, interval=_timeframe)
    except Exception as err:
        print(f'При получении списка котировок возникла ошибка: {err}')
    else:
        quotesY = []
        # Фильтр нужных категорий
        data_lite = data.drop(['Adj Close', 'High', 'Low', 'Volume'], 1)
        # Котировки открытия
        open_data = data_lite['Open'].values
        # Котировки закрытия
        close_data = data_lite['Close'].values

        # Добавление котировок в список quotes
        for price in range(len(open_data)):
            quotesY.append((open_data[price], close_data[price]))
            # quotes.append(open_data[price])
            # quotes.append(close_data[price])

        return json.dumps(quotesY, indent=2)  # json формат
    return None


if __name__ == "__main__":
    # Тикер
    ticker = 'SBER.ME'

    # Таймфрейм
    timeframe = '5m'

    # Временные рамки для получения котировок
    start = dt.date(2021, 5, 1)
    end = dt.date.today()

    # список списков [цена открытия, цена закрытия]
    get_quotes(ticker, start, end)

    # список списков [цена открытия, цена закрытия]
    get_quotesY(ticker, start, end, timeframe)

    # Таблица котировок yahoo указанной ценной бумаги за период
    # с возможностью выбора интервала
    # Формат: Date, Open, High, Low, Close, Adj Close, Volume
    # Котировки AAPL, таймфрейм 15m
    try:
        dataY = yf.download('AAPL', start, end, interval="15m")
    except Exception as err:
        print(f'При получении списка котировок возникла ошибка: {err}')
    else:
        print(dataY)
