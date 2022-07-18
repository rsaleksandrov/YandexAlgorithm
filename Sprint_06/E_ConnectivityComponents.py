"""
Вам дан неориентированный граф. Найдите его компоненты связности.

Формат ввода
В первой строке дано количество вершин n (1≤ n ≤ 10^5) и
рёбер m (0 ≤ m ≤ 2 ⋅ 10^5).
В каждой из следующих m строк записано по ребру в виде пары
вершин 1 ≤ u, v ≤ n.

Гарантируется, что в графе нет петель и кратных рёбер.

Формат вывода
Выведите все компоненты связности в следующем формате: в первой строке
выведите общее количество компонент.

Затем на отдельных строках выведите вершины каждой компоненты, отсортированные
по возрастанию номеров. Компоненты между собой упорядочивайте по номеру
первой вершины.
"""


def DFS(startv, vertex, colors, componentnum, result):
    stack = [startv]
    while len(stack) > 0:
        v = stack.pop()
        if colors[v] == -1:
            if vertex[v] is not None:
                if vertex[v][0] == -1:
                    vertex[v].sort()
                    vertex[v][0] = 1
                colors[v] = 0
                stack.append(v)
                for i in range(len(vertex[v]) - 1, 0, -1):
                    if colors[vertex[v][i]] == -1:
                        stack.append(vertex[v][i])
            else:
                colors[v] = componentnum
                result[componentnum - 1].append(v)
        else:
            if colors[v] == 0:
                colors[v] = componentnum
                result[componentnum - 1].append(v)
    pass


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    vertex = [None] * (n + 1)
    colors = [-1] * (n + 1)
    for i in range(m):
        u, v = list(map(int, input().split()))
        if vertex[u] is None:
            vertex[u] = [-1]
        vertex[u].append(v)
        if vertex[v] is None:
            vertex[v] = [-1]
        vertex[v].append(u)
    cc = 0
    res = []
    for i in range(1, n + 1):
        if colors[i] == -1:
            res.append([])
            cc += 1
            DFS(i, vertex, colors, cc, res)

    print(cc)
    for el in res:
        el.sort()
        print(' '.join(list(map(str, el))))
