# Статический парсер котировок pandas_datareader

import pandas_datareader as web
import datetime as dt
import json


# Получить индексированную таблицу котировок тикера за указанный период
# Формат: Index, Date, High, Low, Open, Close, Volume, Adj Close
def get_quotes_tab(_ticker, _start, _end):
    try:
        data = web.DataReader(_ticker, "yahoo", _start, _end)
    except Exception as err:
        print(f'При получении котировок возникла ошибка: {err}')
    else:
        return data.reset_index()  # Индексация
    return None


# Получить список котировок тикера за указанный период
def get_quotes_list(_ticker, _start, _end):
    try:
        data = web.DataReader([_ticker], "yahoo", _start, _end)
    except Exception as err:
        print(f'При получении котировок возникла ошибка: {err}')
    else:
        quotes = []  # Список котировок
        # Фильтр нужных категорий
        data_lite = data.drop(['Adj Close', 'High', 'Low', 'Volume'], 1)
        # Котировки открытия
        open_data = data_lite[('Open', _ticker)].values
        # Котировки закрытия
        close_data = data_lite[('Close', _ticker)].values

        # Добавление котировок в список quotes
        for price in range(len(open_data)):
            quotes.append(open_data[price])
            quotes.append(close_data[price])

        return quotes
    return None


# Получить список списков котировок тикера за указанный период в формате json
# Формат: [цена открытия, цена закрытия]
def get_quotes_json(_ticker, _start, _end):
    try:
        data = web.DataReader([_ticker], "yahoo", _start, _end)
    except Exception as err:
        print(f'При получении котировок возникла ошибка: {err}')
    else:
        quotes = []  # Список котировок
        # Фильтр нужных категорий
        data_lite = data.drop(['Adj Close', 'High', 'Low', 'Volume'], 1)
        # Котировки открытия
        open_data = data_lite[('Open', _ticker)].values
        # Котировки закрытия
        close_data = data_lite[('Close', _ticker)].values

        # Добавление котировок в список quotes
        for price in range(len(open_data)):
            quotes.append([open_data[price], close_data[price]])

        return json.dumps(quotes, indent=2)  # json формат
    return None


if __name__ == "__main__":
    # Тикер
    ticker = 'SBER.ME'

    # Таймфрейм
    timeframe = '5m'

    # Временные рамки для получения котировок
    start = dt.date.today() - dt.timedelta(days=30)
    end = dt.date.today()

    # Таблица котировок
    print(get_quotes_tab(ticker, start, end))

    # Список котировок
    print(get_quotes_list(ticker, start, end))

    # Список списков [цена открытия, цена закрытия]
    print(get_quotes_json(ticker, start, end))
