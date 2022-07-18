"""
Тимофей решил купить несколько домов на знаменитом среди разработчиков
Алгосском архипелаге. Он нашёл n объявлений о продаже, где указана стоимость
каждого дома в алгосских франках. А у Тимофея есть k франков. Помогите ему
определить, какое наибольшее количество домов на Алгосах он сможет приобрести
за эти деньги.

Формат ввода
В первой строке через пробел записаны натуральные числа n и k.
n — количество домов, которые рассматривает Тимофей, оно не превосходит 1000;
k — общий бюджет, не превосходит 10000;
В следующей строке через пробел записано n стоимостей домов.
Каждое из чисел не превосходит 10000. Все стоимости — натуральные числа.

Формат вывода
Выведите одно число — наибольшее количество домов, которое может
купить Тимофей.
"""

n, k = list(map(int, input().split()))
iData = list(map(int, input().split()))
iData.sort()
sum = 0
h = 0
if iData[0] > k:
    print(h)
else:
    for el in iData:
        if sum + el > k:
            break
        else:
            h += 1
            sum += el
    print(h)