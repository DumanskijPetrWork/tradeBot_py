# Статический парсер котировок
# Дневой фрейм

# pip3 install pandas_datareader
# pip3 install datetime
# pip3 install yfinance
# pip3 install json
import pandas_datareader as web
import datetime as dt
import yfinance as yf
import json

# Временные рамки для получения котировок
start = dt.datetime(2021, 4, 1)
end = dt.datetime.now()

# Таблица котировок указанной ценной бумаги за период
# Формат: Date, Adj Close, Close, High, Low, Open, Volume
# Котировки Сбербанка как пример
try:
    data = web.DataReader(["SBER.ME"], "yahoo", start, end)
except Exception as err:
    print(f'При получении списка котировок возникла ошибка: {err}')

# Вывод цен закрытия и открытия
print(data.drop(['Adj Close', 'High', 'Low', 'Volume'], 1))

# Преобразование в json формат
data_lite = data.drop(['Adj Close', 'High', 'Low', 'Volume'], 1)[:5]
data_lite_json = data_lite.to_json(indent=2)
print(data_lite_json)


# Таблица котировок yahoo указанной ценной бумаги за период
# Формат: Date, Open, High, Low, Close, Adj Close, Volume
# Котировки AAPL, таймфрейм 5 минут
try:
    dataY = yf.download('AAPL', start, end, interval="5m")
except Exception as err:
    print(f'При получении списка котировок возникла ошибка: {err}')

print(dataY)
