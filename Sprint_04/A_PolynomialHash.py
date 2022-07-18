"""
Алле очень понравился алгоритм вычисления полиномиального хеша.
Помогите ей написать функцию, вычисляющую хеш строки s.
В данной задаче необходимо использовать в качестве значений отдельных
символов их коды в таблице ASCII.

Полиномиальный хеш считается по формуле (см рис.).


Формат ввода
В первой строке дано число a (1 ≤ a ≤ 1000) –— основание, по которому
считается хеш.

Во второй строке дано число m (1 ≤ m ≤ 10^9) –— модуль.

В третьей строке дана строка s (0 ≤ |s| ≤ 10^6), состоящая из больших и
маленьких латинских букв.

Формат вывода
Выведите целое неотрицательное число –— хеш заданной строки.
"""


def poliHash(a, m, s) -> int:
    if len(s) == 0:
        return 0
    else:
        h = ord(s[0])
        for i in range(1, len(s)):
            h = (h * a) % m + ord(s[i])
        return h % m


a = int(input())
m = int(input())
s = input()
print(poliHash(a, m, s))