"""
Задан неориентированный граф. Обойдите с помощью DFS все вершины, достижимые
из заданной вершины s, и выведите их в порядке обхода,
если начинать обход из s.

Формат ввода
В первой строке дано количество вершин n (1 ≤ n ≤ 10^5) и рёбер m (0 ≤ m ≤ 10^5).
Далее в m строках описаны рёбра графа. Каждое ребро описывается номерами двух
вершин u и v (1 ≤ u, v ≤ n).
В последней строке дан номер стартовой вершины s (1 ≤ s ≤ n).
В графе нет петель и кратных рёбер.

Формат вывода
Выведите вершины в порядке обхода, считая что при запуске от каждой конкретной
вершины её соседи будут рассматриваться в порядке возрастания (то есть если
вершина 2 соединена с 1 и 3, то сначала обход пойдёт в 1, а уже потом в 3).
"""


class StackEmptyException(Exception):
    pass


class StackFullException(Exception):
    pass


class StackArray:
    __data = []
    __stackmaxsize = 0
    __head = -1
    __resize = 0

    def __init__(self, stacksize=10):
        self.__data = [None] * stacksize
        self.__stackmaxsize = stacksize
        self.__resize = stacksize // 2
        self.__head = -1

    def isEmpty(self):
        return self.__head == -1

    def isFull(self):
        return self.__head == self.__stackmaxsize - 1

    def push(self, value):
        if self.isFull():
            # raise StackFullException()
            self.__data.extend([None] * self.__resize)
            self.__stackmaxsize += self.__resize
        self.__head += 1
        self.__data[self.__head] = value

    def pop(self):
        if self.isEmpty():
            raise StackEmptyException()
        tmpval = self.__data[self.__head]
        self.__data[self.__head] = None
        self.__head -= 1
        return tmpval

    def __repr__(self):
        if self.isEmpty():
            return 'Empty'
        res = []
        for i in range(self.__head + 1):
            res.append(str(self.__data[i]))
        return ' '.join(res)


def DFSline(startv, nodes, colors, stacksize):
    stack = StackArray(stacksize)
    stack.push(startv)
    while not stack.isEmpty():
        v = stack.pop()
        if colors[v] == 'w':
            print(v, end=' ')
            if nodes[v] is not None:
                if nodes[v][0] == -1:
                    nodes[v].sort()
                    nodes[v][0] = 1
                colors[v] = 'g'
                stack.push(v)
                # for i in range(1, len(nodes[v])):
                for i in range(len(nodes[v]) - 1, 0, -1):
                    if colors[nodes[v][i]] == 'w':
                        stack.push(nodes[v][i])
            else:
                colors[v] = 'b'
        else:
            if colors[v] == 'g':
                colors[v] = 'b'
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
        if vertex[v] is None:
            vertex[v] = [-1]
        vertex[v].append(u)
    s = int(input())
    DFSline(s, vertex, colors, max(m, n) * 2)


if __name__ == '__main__':
    main()
