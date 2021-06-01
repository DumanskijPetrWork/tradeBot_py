# Статический парсер котировок yfinance

import yfinance as yf
import datetime as dt
import json


# Получить список списков yahoo-котировок тикера за указанный период в формате json
# с возможностью выбора таймфрейма
# Формат: [цена открытия, цена закрытия]
def get_quotesY_json(_ticker, _start, _end, _timeframe='1d'):
    try:
        dataY = yf.download(_ticker, _start, _end, interval=_timeframe)
    except Exception as err:
        print(f'При получении yahoo-котировок возникла ошибка: {err}')
    else:
        quotesY = []  # Список котировок
        # Фильтр нужных категорий
        dataY_lite = dataY.drop(['Adj Close', 'High', 'Low', 'Volume'], 1)
        # Котировки открытия
        open_dataY = dataY_lite['Open'].values
        # Котировки закрытия
        close_dataY = dataY_lite['Close'].values

        # Добавление котировок в список quotes
        for price in range(len(open_dataY)):
            # quotesY.append([open_dataY[price], close_dataY[price]])

            # Возможно последовательное добавление
            quotesY.append(open_dataY[price])
            quotesY.append(close_dataY[price])

        # return json.dumps(quotesY, indent=2)  # json формат
        return quotesY
    return None


# Получить индексированную таблицу котировок тикера за указанный период
# с возможностью выбора таймфрейма
# Формат: Index, Datetime, Open, High, Low, Close, Adj Close, Volume
def get_quotesY_tab(_ticker, _start, _end, _timeframe='15m'):
    try:
        dataY = yf.download(_ticker, _start, _end, interval=_timeframe)
        dataY = dataY.drop(['Volume', 'Adj Close'], axis=1)  # Удаление столбцов
    except Exception as err:
        print(f'При получении таблицы yahoo-котировок возникла ошибка: {err}')
    else:
        return dataY.reset_index()  # Индексация
    return None


if __name__ == '__main__':
    # Тикер
    ticker = 'AAPL'

    # Таймфрейм
    timeframe = '15m'

    # Временные рамки для получения котировок
    start = dt.date.today() - dt.timedelta(days=30)
    end = dt.date.today()

    # Список списков [цена открытия, цена закрытия]
    print(get_quotesY_json(ticker, start, end, timeframe))

    # Таблица котировок
    print(get_quotesY_tab(ticker, start, end, timeframe))
