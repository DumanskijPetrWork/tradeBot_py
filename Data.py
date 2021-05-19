import pandas_datareader as web
import datetime as dt
import json

# Тикер
ticker = 'SBER.ME'

# Временные рамки для получения котировок
start = dt.datetime(2020, 1, 1)
end = dt.datetime.now()


# Таблица котировок указанной ценной бумаги за период
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
            quotes.append(open_data[price])
            quotes.append(close_data[price])

        return json.dumps(quotes, indent=2)  # json формат
    return None


def quotes(_ticker, _start, _end):
    data = get_quotes(ticker, start, end)
    data = json.loads(data)
    return data


def getAllQuotes(ticker, start, end):
    df = web.DataReader(ticker, "yahoo", start, end)
    df = df.reset_index()
    return df

df = getAllQuotes('SBER.ME', dt.datetime(2019, 1, 1), dt.datetime(2021, 5, 1))
print(df)