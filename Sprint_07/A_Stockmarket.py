"""
Рита хочет попробовать поиграть на бирже. Но для начала она решила
потренироваться на исторических данных.

Даны стоимости акций в каждый из n дней. В течение дня цена акции не меняется.
Акции можно покупать и продавать, но только по одной штуке в день. В один
день нельзя совершать более одной операции (покупки или продажи).
Также на руках не может быть более одной акции в каждый момент времени.

Помогите Рите выяснить, какую максимальную прибыль она могла бы получить.

Формат ввода
В первой строке записано количество дней n —– целое число в диапазоне
от 0 до 10 000.

Во второй строке через пробел записано n целых чисел в диапазоне
от 0 до 1000 –— цены акций.

Формат вывода
Выведите число, равное максимально возможной прибыли за эти дни.
"""


def main():
    n = int(input())
    iData = list(map(int, input().split()))
    isStockPresent = False
    stockPrice = 0
    profit = 0
    day = 0
    while day < n - 1:
        if isStockPresent:
            while iData[day] < iData[day + 1]:
                day += 1
                if day == n - 1:
                    break
            else:
                profit += iData[day] - stockPrice
                isStockPresent = False
        else:
            while iData[day] > iData[day + 1]:
                day += 1
                if day == n - 1:
                    break
            else:
                stockPrice = iData[day]
                isStockPresent = True
        day += 1
    if isStockPresent:
        profit += iData[n - 1] - stockPrice

    print(profit)


if __name__ == '__main__':
    main()
