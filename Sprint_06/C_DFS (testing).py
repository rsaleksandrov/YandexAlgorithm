"""
Обход графа в глубину
"""
from math import inf
import time


class StackElem:
    value = 0
    prev = None

    def __init__(self, value=0, prevelem=None):
        self.value = value
        self.prev = prevelem

    def __repr__(self):
        return str(self.value)


class StackEmptyException(Exception):
    pass


class StackFullException(Exception):
    pass


class Stack:
    __tail: StackElem = None
    __stacksize = 0

    def __init__(self):
        self.__tail = None
        self.__stacksize = 0

    def push(self, value=0):
        newelem = StackElem(value, None)
        if self.__stacksize == 0:
            self.__tail = newelem
        else:
            newelem.prev = self.__tail
            self.__tail = newelem
        self.__stacksize += 1

    def pop(self):
        if self.__stacksize == 0:
            raise StackEmptyException()
        tmpvalue = self.__tail.value
        prevelem = self.__tail.prev
        self.__tail.prev = None
        self.__tail = prevelem
        self.__stacksize -= 1
        return tmpvalue

    def size(self):
        return self.__stacksize

    def isEmpty(self):
        return self.__stacksize == 0

    def __repr__(self):
        if self.__stacksize == 0:
            return 'Empty'
        res = []
        curElem = self.__tail
        while curElem is not None:
            res.append(str(curElem.value))
            curElem = curElem.prev
        return ' '.join(res)


class StackArray:
    __data = []
    __stackmaxsize = 0
    __head = -1

    def __init__(self, stacksize=10):
        self.__data = [None] * stacksize
        self.__stackmaxsize = stacksize
        self.__head = -1

    def isEmpty(self):
        return self.__head == -1

    def isFull(self):
        return self.__head == self.__stackmaxsize - 1

    def push(self, value):
        if self.isFull():
            raise StackFullException()
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


def test():
    stack = Stack()
    for i in range(10):
        stack.push([i, i * 2])

    while not stack.isEmpty():
        val = stack.pop()
        print(val)

    try:
        val = stack.pop()
        print(val)
    except StackEmptyException:
        print('ERROR: Stack is empty')

    for i in range(10):
        stack.push([i * 2])

    while not stack.isEmpty():
        val = stack.pop()
        print(val)


def DFSrecur(v, nodes, colors):
    colors[v] = 'g'  # посетили вершину, но еще не обработали
    print(v, end=' ')
    if nodes[v] is not None:  # Есть исходящие ребра
        if nodes[v][0] == -1:
            nodes[v].sort()
            nodes[v][0] = 1
        for i in range(1, len(nodes[v])):
            if colors[nodes[v][i]] == 'w':
                DFSrecur(nodes[v][i], nodes, colors)
    colors[v] = 'b'
    pass


def DFSline(startv, nodes, colors):
    stack = Stack()
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


def DFSline2(startv, nodes, colors):
    stack = StackArray(len(nodes) * 2)
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


if __name__ == '__main__':
    # test()
    # n - кол-во вершин
    # m - кол-во рёбер
    n, m = list(map(int, input().split()))
    nodes1 = [None] * (n + 1)
    nodes2 = [None] * (n + 1)
    nodes3 = [None] * (n + 1)
    colors1 = ['w'] * (n + 1)  # w - white, g - gray, b - black
    colors2 = ['w'] * (n + 1)  # w - white, g - gray, b - black
    colors3 = ['w'] * (n + 1)  # w - white, g - gray, b - black
    for i in range(m):
        v, u = list(map(int, input().split()))
        if nodes2[v] is None:
            nodes2[v] = [-1]
        if nodes1[v] is None:
            nodes1[v] = [-1]
        if nodes3[v] is None:
            nodes3[v] = [-1]
        nodes2[v].append(u)
        nodes1[v].append(u)
        nodes3[v].append(u)

    k = int(input())

    # MainDFS
    print('Recursive DFS')
    tb = time.perf_counter_ns()
    DFSrecur(k, nodes1, colors1)
    for i in range(1, n + 1):
        if colors1[i] == 'w':
            DFSrecur(i, nodes1, colors1)
    te = time.perf_counter_ns()
    print()
    print(f'Time {(te - tb) / 10 ** 9:.10f} sec.')

    print('Stack DFS')
    tb = time.perf_counter_ns()
    DFSline(k, nodes2, colors2)
    for i in range(1, n + 1):
        if colors2[i] == 'w':
            DFSline(i, nodes2, colors2)
    te = time.perf_counter_ns()
    print()
    print(f'Time {(te - tb) / 10 ** 9:.10f} sec.')

    print('StackArray DFS')
    tb = time.perf_counter_ns()
    DFSline2(k, nodes3, colors3)
    for i in range(1, n + 1):
        if colors3[i] == 'w':
            DFSline2(i, nodes3, colors3)
    te = time.perf_counter_ns()
    print()
    print(f'Time {(te - tb) / 10 ** 9:.10f} sec.')
