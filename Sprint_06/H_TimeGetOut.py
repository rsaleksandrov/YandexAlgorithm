"""
Вам дан ориентированный граф. Известно, что все его вершины достижимы из
вершины s=1. Найдите время входа и выхода при обходе в глубину, производя
первый запуск из вершины s. Считайте, что время входа в стартовую вершину
равно 0. Соседей каждой вершины обходите в порядке увеличения номеров.

Формат ввода
В первой строке дано число вершин n (1 ≤ n ≤ 2⋅ 10^5) и рёбер
(0 ≤ m ≤ 2 ⋅ 10^5). В каждой из следующих m строк записаны рёбра графа в
виде пар (from, to), 1 ≤ from ≤ n — начало ребра, 1 ≤ to ≤ n — его конец.
Гарантируется, что в графе нет петель и кратных рёбер.

Формат вывода
Выведите n строк, в каждой из которых записана пара чисел tini, touti — время
входа и выхода для вершины i.
"""


def DFSline(startv, nodes, colors):
    stack = [startv]
    entertime = [None] * len(nodes)
    leavetime = [None] * len(nodes)
    steptime = -1
    while len(stack) > 0:
        v = stack.pop()
        if colors[v] == 'w':
            if nodes[v] is not None:
                if nodes[v][0] == -1:
                    nodes[v].sort()
                    nodes[v][0] = 1
                colors[v] = 'g'
                steptime += 1
                entertime[v] = steptime
                stack.append(v)

                for i in range(len(nodes[v]) - 1, 0, -1):
                    if colors[nodes[v][i]] == 'w':
                        stack.append(nodes[v][i])
            else:
                steptime += 1
                entertime[v] = steptime
                colors[v] = 'b'
                steptime += 1
                leavetime[v] = steptime
        else:
            if colors[v] == 'g':
                steptime += 1
                leavetime[v] = steptime
                colors[v] = 'b'
    for i in range(1, len(nodes)):
        print(entertime[i], leavetime[i])
    pass


def main():
    n, m = list(map(int, input().split()))
    vertex = [None] * (n + 1)
    colors = ['w'] * (n + 1)
    for i in range(m):
        u, v = list(map(int, input().split()))
        if vertex[u] is None:
            vertex[u] = [-1]
        vertex[u].append(v)
    DFSline(1, vertex, colors)


if __name__ == '__main__':
    main()
