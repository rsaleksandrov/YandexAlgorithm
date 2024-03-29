"""
Вася решил накопить денег на два одинаковых велосипеда — себе и сестре.
У Васи есть копилка, в которую каждый день он может добавлять деньги
(если, конечно, у него есть такая финансовая возможность). В процессе
накопления Вася не вынимает деньги из копилки.

У вас есть информация о росте Васиных накоплений — сколько у Васи в
копилке было денег в каждый из дней.

Ваша задача — по заданной стоимости велосипеда определить:
первый день, в которой Вася смог бы купить один велосипед,
и первый день, в который Вася смог бы купить два велосипеда.

Подсказка: решение должно работать за O(log n).

Формат ввода
В первой строке дано число дней n, по которым велись наблюдения за
Васиными накоплениями. 1 ≤ n ≤ 10^6.

В следующей строке записаны n целых неотрицательных чисел.
Числа идут в порядке неубывания. Каждое из чисел не превосходит 10^6.

В третьей строке записано целое положительное число s — стоимость велосипеда.
Это число не превосходит 10^6.

Формат вывода
Нужно вывести два числа — номера дней по условию задачи.
Если необходимой суммы в копилке не нашлось, нужно вернуть -1 вместо номера дня.
"""


def BinarySearch(pData, pValue, pLeftBound, pRightBound):
    if pLeftBound >= pRightBound:
        # Элемент не найден. Возможны 2 случая:
        # 1. Элемент в позиции min(pLeftBound, pRightBound) больше или
        #    равен заданному. Тогда возвращаем min(pLeftBound, pRightBound),
        #    т.к. денег в копилке достаточно.
        # 2. Элемент в позиции min(pLeftBound, pRightBound) меньше заданного.
        #    Тогда возвращаем -1
        id = min(pLeftBound, pRightBound)
        if pData[id] >= pValue:
            return id
        else:
            return -1
    mid = (pLeftBound + pRightBound) // 2
    if pData[mid] >= pValue:  # Ищем самое первое вхождение pValue
        return BinarySearch(pData, pValue, pLeftBound, mid)
    else:
        return BinarySearch(pData, pValue, mid + 1, pRightBound)


if __name__ == '__main__':
    n = int(input())
    iAccumulated = list(map(int, input().split()))
    cost = int(input())
    d1 = BinarySearch(iAccumulated, cost, 0, n - 1)
    d2 = BinarySearch(iAccumulated, cost * 2, 0, n - 1)
    if d1 != -1:
        d1 += 1
    if d2 != -1:
        d2 += 1
    print(d1, d2)
