"""
Гоша измерял температуру воздуха n дней подряд. В результате у него получился
некоторый временной ряд. Теперь он хочет посмотреть, как часто встречается
некоторый шаблон в получившейся последовательности. Однако температура — вещь
относительная, поэтому Гоша решил, что при поиске шаблона длины m
(a1, a2, ..., am) стоит также рассматривать сдвинутые на константу вхождения.
Это значит, что если для некоторого числа c в исходной последовательности
нашёлся участок вида (a1 + c, a2 + c, ... , am + c), то он тоже считается
вхождением шаблона (a1, a2, ..., am).
По заданной последовательности измерений X и шаблону A=(a1, a2, ..., am)
определите все вхождения A в X, допускающие сдвиг на константу.

Подсказка: если вы пишете на питоне и сталкиваетесь с TL, то попробуйте
заменить какие-то из циклов операциями со срезами.

Формат ввода
В первой строке дано количество сделанных измерений n — натуральное число,
не превышающее 10^4.
Во второй строке через пробел записаны n целых чисел xi, 0 ≤ xi ≤ 10^3 –—
результаты измерений.
В третьей строке дано натуральное число m –— длина искомого шаблона, 1≤ m ≤ n.
В четвёртой строке даны m целых чисел ai — элементы шаблона, 0 ≤ ai ≤ 10^3.

Формат вывода
Выведите через пробел в порядке возрастания все позиции, на которых начинаются
вхождения шаблона A в последовательность X.
Нумерация позиций начинается с единицы.
"""


def myFind(d, p, start):
    for offset in range(start, len(d) - len(p) + 1):
        tmp = d[offset:offset + len(p)]
        c = set([x - y for x, y in zip(tmp, p)])
        if len(c) == 1:
            return offset
    return -1


n = int(input())
data = list(map(int, input().split()))
m = int(input())
pattern = list(map(int, input().split()))
ins = []
start = 0
isStop = False
while not isStop:
    f = myFind(data, pattern, start)
    if f == -1:
        isStop = True
        continue
    ins.append(f + 1)
    start = f + 1
print(*ins)