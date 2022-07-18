"""
Под расстоянием между двумя вершинами в графе будем понимать длину кратчайшего
пути между ними в рёбрах. Для данной вершины s определите максимальное
расстояние от неё до другой вершины неориентированного графа.

Формат ввода
В первой строке дано количество вершин n (1 ≤ n ≤ 105) и
рёбер m (0 ≤ m ≤ 105). Далее в m строках описаны рёбра графа.
Каждое ребро описывается номерами двух вершин u и v (1 ≤ u, v ≤ n).
В последней строке дан номер вершины s (1 ≤ s ≤ n). Гарантируется,
что граф связный и что в нём нет петель и кратных рёбер.

Формат вывода
Выведите длину наибольшего пути от s до одной из вершин графа.
"""
from collections import deque


def BFSdist(startv, vertex):
    colors = [-1] * len(vertex)
    distances = [None] * len(vertex)
    bypass = deque()
    colors[startv] = 0
    bypass.append(startv)
    distances[startv] = 0
    maxdist = 0
    while len(bypass) > 0:
        curv = bypass.popleft()
        # print(curv, end=' ')
        if vertex[curv] is not None:
            if vertex[curv][0] == -1:
                vertex[curv].sort()
                vertex[curv][0] = 1
            for i in range(1, len(vertex[curv])):
                nextv = vertex[curv][i]
                if colors[nextv] == -1:
                    bypass.append(nextv)
                    colors[nextv] = 0
                    distances[nextv] = distances[curv] + 1
                    if maxdist < distances[nextv]:
                        maxdist = distances[nextv]
        colors[curv] = 1
    print(maxdist)
    pass


def main():
    n, m = list(map(int, input().split()))
    vertex = [None] * (n + 1)
    for i in range(m):
        u, v = list(map(int, input().split()))
        if vertex[u] is None:
            vertex[u] = [-1]
        if vertex[v] is None:
            vertex[v] = [-1]
        vertex[v].append(u)
        vertex[u].append(v)
    s = int(input())
    BFSdist(s, vertex)
    pass


if __name__ == '__main__':
    main()
