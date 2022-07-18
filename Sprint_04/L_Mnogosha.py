"""
Дана длинная строка, состоящая из маленьких латинских букв. Нужно найти все
её подстроки длины n, которые встречаются хотя бы k раз.

Формат ввода
В первой строчке через пробел записаны два натуральных числа n и k.

Во второй строчке записана строка, состоящая из маленьких латинских букв.
Длина строки 1 ≤ L ≤ 106.
n ≤ L, k ≤ L.

Формат вывода
Для каждой найденной подстроки выведите индекс начала её первого вхождения
(нумерация в строке начинается с нуля).

Выводите индексы в любом порядке, в одну строку, через пробел.
"""


def poliHash(k, m, s) -> int:
    if len(s) == 0:
        return 0
    else:
        h = ord(s[0])
        for i in range(1, len(s)):
            h = (h * k) % m + ord(s[i])
        return h % m


def main(n, k, s):
    if len(s) >= n:
        # подготовительные мероприятия
        phm = 2 ** 64
        phk = 31
        pown = pow(phk, n - 1, phm)
        ht = {}
        ans = []
        h = 0
        for i in range(len(s) - n + 1):
            if i == 0:
                ss = s[0: n]
                h = poliHash(phk, phm, ss)
            else:
                a1k = (ord(s[i - 1]) * pown) % phm
                r1 = ((h - a1k) * phk) % phm
                h = r1 + ord(s[i + n - 1])
            if h in ht:
                ht[h][1] += 1
            else:
                ht[h] = [i, 1, False]
            if ht[h][1] >= k and not ht[h][2]:
                ht[h][2] = True
                ans.append(ht[h][0])
        print(*ans)
    else:
        print('0')


if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    s = input()
    main(n, k, s)
