"""
Гуляя по одному из островов Алгосского архипелага, Гоша набрёл на пещеру,
в которой лежат кучи золотого песка. К счастью, у Гоши есть с собой рюкзак
грузоподъёмностью до M килограмм, поэтому он может унести с собой какое-то
ограниченное количество золота. Всего золотых куч n штук, и все они разные.
В куче под номером i содержится mi килограммов золотого песка, а стоимость
одного килограмма — ci алгосских франков. Помогите Гоше наполнить рюкзак
так, чтобы общая стоимость золотого песка в пересчёте на алгосские франки
была максимальной.

Формат ввода
В первой строке задано целое число M — грузоподъёмность рюкзака Гоши
(0 ≤ M ≤ 108). Во второй строке дано количество куч с золотым песком — целое
число n (1 ≤ n ≤ 105). В каждой из следующих n строк описаны кучи: i-ая куча
задаётся двумя целыми числами ci и mi, записанными через пробел
(1 ≤ ci ≤ 107, 1 ≤ mi ≤ 108).

Формат вывода
Выведите единственное число —– максимальную сумму (в алгосских франках),
которую Гоша сможет вынести из пещеры в своём рюкзаке.
"""

m = int(input())
n = int(input())
data = []
for i in range(n):
    ci, mi = list(map(int, input().split()))
    data.append([ci, mi])
data.sort()
maxprofit = 0
maxmass = 0
for i in range(n - 1, -1, -1):
    tmpmass = data[i][1] if (maxmass + data[i][1]) <= m else (m - maxmass)
    maxprofit += data[i][0] * tmpmass
    maxmass += tmpmass
    if maxmass >= m:
        break
print(maxprofit)
