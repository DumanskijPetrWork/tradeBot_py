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

