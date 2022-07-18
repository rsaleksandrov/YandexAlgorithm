"""
Найдите кратчайшее расстояние между парой вершин в неориентированном графе.
Граф может быть несвязным. Формат ввода В первой строке дано количество
вершин n (1 ≤ n ≤ 10^5) и рёбер m (1 ≤ m ≤ 10^5).
Далее в m строках описаны рёбра графа. Каждое ребро описывается номерами
двух вершин u и v (1 ≤ u, v ≤ n).
В последней строке дан номер стартовой вершины s (1 ≤ s ≤ n)
и конечной t (1 ≤ t ≤ n). Гарантируется, что в графе нет петель и кратных
рёбер. Формат вывода Выведите длину кратчайшего пути (в рёбрах) между
заданной парой вершин. Если пути не существует, то выведите -1.
"""

from collections import deque
from math import inf


def VertexToVertexDist(startv, endv, vertex):
    bypass = deque()
    dist = [inf] * len(vertex)
    # -1 - не посящали, 0 - были
    colors = [-1] * len(vertex)

    bypass.append(startv)
    dist[startv] = 0
    colors[startv] = 0

    while len(bypass) > 0:
        v = bypass.popleft()
        if v == endv:
            break
        if vertex[v] is not None:
            for el in vertex[v]:
                if dist[el] > dist[v] + 1:
                    dist[el] = dist[v] + 1
                if colors[el] == -1:
                    bypass.append(el)
                    colors[el] = 0
        pass
    return dist[endv] if dist[endv] != inf else -1
    pass


def main():
    n, m = list(map(int, input().split()))
    vertex = [None] * (n + 1)
    for i in range(m):
        u, v = list(map(int, input().split()))
        if vertex[u] is None:
            vertex[u] = []
        if vertex[v] is None:
            vertex[v] = []
        vertex[u].append(v)
        vertex[v].append(u)
    sv, ev = list(map(int, input().split()))
    d = VertexToVertexDist(sv, ev, vertex)
    print(d)
    pass


if __name__ == '__main__':
    main()
