"""
Вы приехали на архипелаг Алгосы (наконец-то!).
Здесь есть n достопримечательностей. Ваша лодка может высадить вас у одной из
них, забрать у какой-то другой, возможно, той же самой достопримечательности и
увезти на материк.

Чтобы более тщательно спланировать свой маршрут, вы хотите узнать расстояния
между каждой парой достопримечательностей Алгосов. Некоторые из них соединены
мостами, по которым вы можете передвигаться в любую сторону. Всего мостов m.

Есть вероятность, что карта архипелага устроена так, что нельзя добраться от
какой-то одной достопримечательности до другой без использования лодки.

Найдите кратчайшие расстояния между всеми парами достопримечательностей.

Формат ввода
В первой строке даны числа n (1 ≤ n ≤ 100) и m (0 ≤ m ≤ n (n-1)/2).
В следующих m строках описаны мосты. Каждый мост задаётся номерами двух
достопримечательностей 1 ≤ u, v ≤ n и длиной дороги 1 ≤ L ≤ 10^3.

Формат вывода
Выведите матрицу n × n кратчайших расстояний.
На пересечении i-й строки и j-го столбца должно стоять расстояние
от i-й до j-й достопримечательности. Если между какой-то парой нет пути,
то в соответствующей клетке поставьте -1.
"""
from math import inf


def getmindistnotvisitedvertex(curv, visit, dist):
    curminvalue = inf
    curminvertex = -1

    for i in range(1, len(visit)):
        if not visit[i] and dist[curv - 1][i - 1] < curminvalue:
            curminvalue = dist[curv - 1][i - 1]
            curminvertex = i
    return curminvertex


def Bypass(startv, vertex, dist):
    # dist = [inf] * len(vertex)
    # prev = [None] * len(vertex)
    visit = [False] * len(vertex)

    dist[startv - 1][startv - 1] = 0
    # visit[startv] = True
    u = getmindistnotvisitedvertex(startv, visit, dist)
    while u != -1:
        visit[u] = True
        if vertex[u] is not None:
            for el in vertex[u]:
                if dist[startv - 1][el[0] - 1] > dist[startv - 1][u - 1] + el[
                    1]:
                    dist[startv - 1][el[0] - 1] = dist[startv - 1][u - 1] + el[
                        1]
                    dist[el[0] - 1][startv - 1] = dist[startv - 1][el[0] - 1]
        u = getmindistnotvisitedvertex(startv, visit, dist)
    pass


def main():
    n, m = list(map(int, input().split()))
    vertex = [None] * (n + 1)
    for i in range(m):
        u, v, d = list(map(int, input().split()))
        if vertex[u] is None:
            vertex[u] = []
        if vertex[v] is None:
            vertex[v] = []
        vertex[u].append([v, d])
        vertex[v].append([u, d])
    result = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(1, n + 1):
        Bypass(i, vertex, result)

    for line in result:
        for el in line:
            if el == inf:
                print(-1, end=' ')
            else:
                print(el, end=' ')
        print()
    pass


if __name__ == '__main__':
    main()
