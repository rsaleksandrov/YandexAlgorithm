"""
Дан ациклический ориентированный граф (так называемый DAG,
directed acyclic graph). Найдите его топологическую сортировку, то есть
выведите его вершины в таком порядке, что все рёбра графа идут слева направо.
У графа может быть несколько подходящих перестановок вершин. Вам надо найти
любую топологическую сортировку.

Формат ввода
В первой строке даны два числа – количество вершин n (1 ≤ n ≤ 10^5) и
количество рёбер m (0 ≤ m ≤ 10^5). В каждой из следующих m строк описаны
рёбра по одному на строке. Каждое ребро представлено парой вершин (from, to),
1≤ from, to ≤ n, соответственно номерами вершин начала и конца.

Формат вывода
Выведите номера вершин в требуемом порядке.
"""


def DFS(startv, vertex, colors, topstack):
    stack = [startv]
    while len(stack) > 0:
        v = stack.pop()
        if colors[v] == 'w':
            if vertex[v] is not None:
                if vertex[v][0] == -1:
                    vertex[v].sort()
                    vertex[v][0] = 1
                colors[v] = 'g'
                stack.append(v)
                for i in range(len(vertex[v]) - 1, 0, -1):
                    if colors[vertex[v][i]] == 'w':
                        stack.append(vertex[v][i])
            else:
                colors[v] = 'b'
                topstack.append(v)
        else:
            if colors[v] == 'g':
                colors[v] = 'b'
                topstack.append(v)
    pass


def main():
    n, m = list(map(int, input().split()))
    nodes = [None] * (n + 1)
    colors = ['w'] * (n + 1)  # w - white, g - gray, b - black
    for i in range(m):
        v, u = list(map(int, input().split()))
        if nodes[v] is None:
            nodes[v] = [-1]
        nodes[v].append(u)

    res = []
    for i in range(1, n + 1):
        if colors[i] == 'w':
            DFS(i, nodes, colors, res)
    res.reverse()
    print(' '.join(list(map(str, res))))
    pass


if __name__ == '__main__':
    main()
