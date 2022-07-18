"""
Тимофей решил соединить все компьютеры в своей компании в единую сеть.
Для этого он придумал построить минимальное остовное дерево, чтобы эффективнее
использовать ресурсы. Но от начальства пришла новость о том, что выделенный
на сеть бюджет оказался очень большим и его срочно надо израсходовать.
Поэтому Тимофея теперь интересуют не минимальные, а максимальные остовные
деревья. Он поручил вам найти вес такого максимального остовного дерева в
неориентированном графе, который задаёт схему офиса.

Формат ввода
В первой строке дано количество вершин n и ребер m графа
(1 ≤ n ≤ 1000, 0 ≤ m ≤ 100000). В каждой из следующих m строк заданы рёбра
в виде троек чисел u, v, w. u и v — вершины, которые соединяет это ребро.
w — его вес ( 1 ≤ u, v ≤ n, 0 ≤ w ≤ 10000).
В графе могут быть петли и кратные ребра. Граф может оказаться несвязным.

Формат вывода
Если максимальное остовное дерево существует, то выведите его вес.
Иначе (если в графе несколько компонент связности) выведите фразу
«Oops! I did it again».
"""


class HeapFullExeption(Exception):
    pass


class HeapEmptyExeption(Exception):
    pass


# Класс кучи (приоритетная очередь)
class Heap:
    heap = []
    heapsize = 0
    maxfirst = True

    # Инициализация класса
    def __init__(self, baseheapsize=10, isMaxFirst=True) -> None:
        self.heap = [None] * (baseheapsize + 1)
        self.maxfirst = isMaxFirst
        pass

    # формирование представление
    def __repr__(self) -> str:
        return ' '.join(map(str, self.heap))

    # Функция сравнения. Если isMaxFirst=True, максимальный элемент первый,
    # иначе - минимальный
    def __compare(self, value1, value2, isMaxFirst=True) -> bool:
        if isMaxFirst:
            return value1 < value2
        else:
            return value1 > value2

    # Просеивание вверх (восстановление порядка при добавлении элемента)
    def __sift_up(self, idx):
        if idx == 1:
            return
        parent_index = idx // 2
        if self.__compare(self.heap[parent_index], self.heap[idx],
                          self.maxfirst):
            self.heap[parent_index], self.heap[idx] = self.heap[idx], \
                                                      self.heap[parent_index]
            self.__sift_up(parent_index)
        pass

    # Просеивание вниз (восстановление структуры при удалении элемента)
    def __sift_down(self, idx):
        left = idx * 2
        right = idx * 2 + 1

        lchp = left <= self.heapsize  # Left child is present
        rchp = right <= self.heapsize  # Right child is present

        if not lchp and not rchp:
            return

        if lchp and rchp:
            if self.__compare(self.heap[left], self.heap[right],
                              self.maxfirst):
                largest_index = right
            else:
                largest_index = left
        elif lchp:
            largest_index = left
        else:
            largest_index = right

        if self.__compare(self.heap[idx], self.heap[largest_index],
                          self.maxfirst):
            self.heap[idx], self.heap[largest_index] = self.heap[
                                                           largest_index], \
                                                       self.heap[idx]
            return self.__sift_down(largest_index)

    # Добавление элемента
    def add(self, value):
        index = self.heapsize + 1
        if index >= len(self.heap):
            raise HeapFullExeption()
        else:
            self.heap[index] = value
            self.heapsize = index
            self.__sift_up(index)

    # Получение элемента с вершины кучи. Если isRemove=True, элемент удаляется
    def getheadelem(self, isRemove=True):
        if self.heapsize == 0:
            raise HeapEmptyExeption()

        tmpvalue = self.heap[1]

        if isRemove:
            self.heap[1] = self.heap[self.heapsize]
            self.heap[self.heapsize] = None
            self.heapsize -= 1
            self.__sift_down(1)

        return tmpvalue

    def isEmpty(self):
        return self.heapsize == 0


# Алгоритм Прима на очереди с приоритетами
def ostovTree(startv, vertex, edgescount, isOstovTreeMin=True):
    ostovWeight = -1  # Вес остовного дерева
    addedVertexCount = 0  # Количество вершин, добавленных в остов
    addedVertexes = [False] * len(vertex)
    edges = Heap(edgescount, True)

    addedVertexes[startv] = True
    addedVertexCount += 1

    if vertex[startv] is None:
        if (len(vertex) - 1) == 1:
            return 0
        else:
            return -1

    for el in vertex[startv]:
        edges.add([el[1], startv, el[0]])

    while addedVertexCount < (len(vertex) - 1) and not edges.isEmpty():
        try:
            el = edges.getheadelem()
        except HeapEmptyExeption:
            break
        edgebegin = el[1]
        edgeend = el[2]
        edgeweigth = el[0]
        if not addedVertexes[edgebegin] or not addedVertexes[edgeend]:
            addingVertex = edgeend if addedVertexes[edgebegin] else edgebegin
            if ostovWeight == -1:
                ostovWeight = edgeweigth
            else:
                ostovWeight += edgeweigth
            addedVertexes[addingVertex] = True
            addedVertexCount += 1
            if vertex[addingVertex] is not None:
                for el in vertex[addingVertex]:
                    if not addedVertexes[el[0]]:
                        edges.add([el[1], addingVertex, el[0]])
        pass
    if addedVertexCount != (len(vertex) - 1):
        return -1
    else:
        return ostovWeight
    pass


def main():
    n, m = list(map(int, input().split()))
    vertex = [None] * (n + 1)
    for i in range(m):
        u, v, w = list(map(int, input().split()))
        if vertex[u] is None:
            vertex[u] = []
        if vertex[v] is None:
            vertex[v] = []
        vertex[u].append([v, w])
        vertex[v].append([u, w])
    weight = ostovTree(1, vertex, m * 2, False)
    if weight != -1:
        print(weight)
    else:
        print('Oops! I did it again')
    pass


if __name__ == '__main__':
    main()
