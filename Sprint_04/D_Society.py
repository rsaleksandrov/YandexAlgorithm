"""
В компании, где работает Тимофей, заботятся о досуге сотрудников и устраивают
различные кружки по интересам. Когда кто-то записывается на занятие, в лог
вносится название кружка.

По записям в логе составьте список всех кружков, в которые ходит хотя бы
один человек.

Формат ввода
В первой строке даётся натуральное число n, не превосходящее 10 000 —
количество записей в логе.

В следующих n строках —– названия кружков.

Формат вывода
Выведите уникальные названия кружков по одному на строке, в порядке появления
во входных данных.
"""

n = int(input())
res = {}
for i in range(n):
    s = input()
    if s not in res.keys():
        res[s] = 1
for key in res.keys():
    print(key)
