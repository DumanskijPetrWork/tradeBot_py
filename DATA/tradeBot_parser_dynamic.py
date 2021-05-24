# Динамический парсер котировок

import datetime as dt
import matplotlib.pyplot as plt
from DATA.tradeBot_parser_static import get_quotes_list


# Генератор динамических значений котировок
def get_dynamic_quotes(_quotes):
    quotes = _quotes
    for _ in range(len(quotes)):
        yield quotes[_]


if __name__ == '__main__':
    # Инициализация
    data = get_quotes_list('AAPL',
                           dt.date.today() - dt.timedelta(days=30),
                           dt.date.today())
    quotes_generator = get_dynamic_quotes(data)  # Генератор котировок

    # Значения по осям
    x_values = []
    y_values = []

    # Динамическое обновление
    for i in range(len(data)):
        # Добавление последней точки графика
        try:
            y_values.append(next(quotes_generator))
            x_values.append(i)
        except StopIteration:
            break

        # Стиль графика
        plt.style.use('fivethirtyeight')
        plt.tight_layout()

        plt.cla()  # Очистка графика
        plt.plot(x_values, y_values, color='black')  # Обновление графика
        plt.pause(0.5)  # Интервал отрисовки

    plt.show()
