"""
Жители Алгосов любят устраивать турниры по спортивному программированию.
Все участники разбиваются на пары и соревнуются друг с другом. А потом два
самых сильных программиста встречаются в финальной схватке, которая состоит
из нескольких раундов. Если в очередном раунде выигрывает первый участник,
в таблицу с результатами записывается 0, если второй, то 1. Ничьей в раунде
быть не может.

Нужно определить наибольший по длине непрерывный отрезок раундов, по
результатам которого суммарно получается ничья. Например, если дана
последовательность 0 0 1 0 1 1 1 0 0 0, то раунды с 2-го по 9-й (нумерация
начинается с единицы) дают ничью.

Формат ввода
В первой строке задаётся n (0 ≤ n ≤ 10^5) –— количество раундов. Во второй
строке через пробел записано n чисел –— результаты раундов. Каждое число
равно либо 0, либо 1.

Формат вывода
Выведите длину найденного отрезка.
"""

n = int(input())
if n >= 2:
    iData = input().split()
    ht = {}
    ht[0] = [-1, 0]
    tmpSum = 0
    for i in range(n):
        tmpSum += 1 if iData[i] == '1' else -1
        if tmpSum not in ht.keys():
            ht[tmpSum] = [i, 0]
        else:
            ht[tmpSum][1] = i
    maxLen = ht[0][1] - ht[0][0]
    for el in ht.values():
        if maxLen < el[1] - el[0]:
            maxLen = el[1] - el[0]
    if maxLen == 1:
        print(0)
    else:
        print(maxLen)
    pass
else:
    print(0)