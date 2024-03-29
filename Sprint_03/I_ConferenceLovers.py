"""
На IT-конференции присутствовали студенты из разных вузов со всей страны.
Для каждого студента известен ID университета, в котором он учится.

Тимофей предложил Рите выяснить, из каких k вузов на конференцию пришло
больше всего учащихся.

Формат ввода
В первой строке дано количество студентов в списке —– n (1 ≤ n ≤ 15 000).
Во второй строке через пробел записаны n целых чисел —– ID вуза каждого
студента. Каждое из чисел находится в диапазоне от 0 до 10 000.
В третьей строке записано одно число k.

Формат вывода
Выведите через пробел k ID вузов с максимальным числом участников.
Они должны быть отсортированы по убыванию популярности (по количеству гостей
от конкретного вуза). Если более одного вуза имеет одно и то же количество
учащихся, то выводить их ID нужно в порядке возрастания.
"""

n = int(input())
iData = list(map(int, input().split()))
k = int(input())
resArray = [[0, -1]] * 10000

for el in iData:
    resArray[el] = [resArray[el][0] - 1, el]

resArray.sort()

for el in resArray[:k]:
    print(el[1], end=' ')
