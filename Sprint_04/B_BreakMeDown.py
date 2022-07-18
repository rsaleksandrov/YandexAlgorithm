"""
Гоша написал программу, которая сравнивает строки исключительно по их хешам. Если хеш равен, то и строки равны. Тимофей увидел это безобразие и поручил вам сломать программу Гоши, чтобы остальным неповадно было.

В этой задаче вам надо будет лишь найти две различные строки, которые для
заданной хеш-функции будут давать одинаковое значение.

Гоша использует следующую хеш-функцию:


для a = 1000 и m = 123 987 123.
В данной задаче необходимо использовать в качестве значений отдельных
символов их коды в таблице ASCII.

Формат ввода
В задаче единственный тест без ввода

Формат вывода
Отправьте две строки, по одной в строке. Строки могут состоять только из
маленьких латинских букв и не должны превышать в длину 1000 знаков каждая.
Код отправлять не требуется. Строки из примера использовать нельзя.

Пример вывода:
ezhgeljkablzwnvuwqvp
gbpdcvkumyfxillgnqrv
"""


def poliHash(a, m, s) -> int:
    if len(s) == 0:
        return 0
    else:
        h = ord(s[0])
        for i in range(1, len(s)):
            h = (h * a) % m + ord(s[i])
        return h % m


def calcStrs(a, m):
    d = {}
    for strlen in range(1, 6):
        s = ['a'] * strlen
        isStop = False
        while not isStop:
            tmps = ''.join(s)
            h = poliHash(a, m, tmps)
            if h not in d.keys():
                d[h] = [h, tmps]
            else:
                print('FOUND:')
                print(f'\t{h}')
                print(f'\t{d[h][1]}')
                print(f'\t{tmps}')

            ii = len(s) - 1
            while ii >= 0:
                s[ii] = chr(ord(s[ii]) + 1)
                if s[ii] > 'z':
                    if ii > 0:
                        s[ii] = 'a'
                    ii -= 1
                else:
                    break
            isStop = s[0] > 'z'


a = 1000
m = 123987123
calcStrs(a, m)
# print(poliHash(a, m, 'ezhgeljkablzwnvuwqvp'))
# print(poliHash(a, m, 'gbpdcvkumyfxillgnqrv'))
