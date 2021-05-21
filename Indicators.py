import math
import pandas_datareader as web
import datetime as dt
import json


# usually close data

# Simple moving average
# https://en.wikipedia.org/wiki/Moving_average
def SMA(data, period):  
    if len(data) == 0:
        raise Exception("Empty data")
    if period <= 0:
        raise Exception("Invalid period")

    interm = 0
    result = []
    for i, v in enumerate(data):
        interm += v
        if (i + 1) < period:
            result.append(math.nan)
        else:
            result.append(interm / float(period))
            interm -= data[i + 1 - period]
    return result


# Exponential moving average
# https://en.wikipedia.org/wiki/Moving_average#Exponential_moving_average
def EMA(data, period):
    if period <= 1:
        raise Exception("Invalid period")

    sma = SMA(data, period)
    multiplier = 2 / (float(period + 1))
    result = []

    for k, v in enumerate(sma):
        if math.isnan(v):
            result.append(math.nan)
        else:
            prev = result[k - 1]
            if math.isnan(prev):
                result.append(v)
                continue
            ema = (data[k] - prev) * multiplier + prev
            result.append(ema)
    return result


# Moving average convergence/divergence
# https://en.wikipedia.org/wiki/MACD
# usuall take 12,26,9, but u can take 5,35,5 for more risky trading
def MACD(data, shortperiod, longperiod, signalperiod):
    macd, macdsignal, macdhist = [], [], []

    short_ema = EMA(data, shortperiod)
    long_ema = EMA(data, longperiod)

    diff = []

    for k, short in enumerate(short_ema):
        if math.isnan(short) or math.isnan(long_ema[k]):
            macd.append(math.nan)
            macdsignal.append(math.nan)
        else:
            macd.append(short - long_ema[k])
            diff.append(macd[k])

    diff_ema = EMA(diff, signalperiod)
    macdsignal = macdsignal + diff_ema

    for k, ms in enumerate(macdsignal):
        if math.isnan(ms) or math.isnan(macd[k]):
            macdhist.append(math.nan)
        else:
            macdhist.append(macd[k] - macdsignal[k])

    return macd, macdsignal, macdhist


