"""
Задан неориентированный граф. Обойдите поиском в ширину все вершины,
достижимые из заданной вершины s, и выведите их в порядке обхода, если
начинать обход из s.

Формат ввода
В первой строке дано количество вершин n (1 ≤ n ≤ 10^5) и
рёбер m (0 ≤ m ≤ 10^5). Далее в m строках описаны рёбра графа.
Каждое ребро описывается номерами двух вершин u и v (1 ≤ u, v ≤ n).
В последней строке дан номер стартовой вершины s (1 ≤ s ≤ n).

Гарантируется, что в графе нет петель и кратных рёбер.

Формат вывода
Выведите вершины в порядке обхода, считая что при запуске от каждой
конкретной вершины её соседи будут рассматриваться в порядке возрастания
(то есть если вершина 2 соединена с 1 и 3, то сначала обход пойдёт в 1, а
уже потом в 3).
"""

from collections import deque


def BFS(startv, vertex):
    colors = [-1] * len(vertex)
    bypass = deque()
    colors[startv] = 0
    bypass.append(startv)
    while len(bypass) > 0:
        curv = bypass.popleft()
        print(curv, end=' ')
        if vertex[curv] is not None:
            if vertex[curv][0] == -1:
                vertex[curv].sort()
                vertex[curv][0] = 1
            for i in range(1, len(vertex[curv])):
                if colors[vertex[curv][i]] == -1:
                    bypass.append(vertex[curv][i])
                    colors[vertex[curv][i]] = 0
        colors[curv] = 1
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
    BFS(s, vertex)
    pass


if __name__ == '__main__':
    main()
