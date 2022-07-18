"""
ID 68914712

В задаче используется приоритетная очередь с пирамидальной сортировкой,
реализованная на куче (класс Heap).

Алгоритм:
Для формирования остовного дерева используется алгоритм Прима, но в первую
очередь берутся ребра с максимальным весом. Для хранения и быстрого получения
ребра с максимальным весом используется приоритетная очередь, реализованная с
использованием кучи.
"Модифицированный" алгоритм Прима:
1. Берем стартовую вершину. Если у нее нет смежных вершин и она не одна в
   графе, то построить остовное дерево нельзя. Если она одна, то вес итогового
   дерева - 0.
2. Добавляем в приоритетную очередь (максимальный элемент всегда на вершине)
   все ребра к смежным вершинам с указанием их веса.
3. Пока количество добавленных в остов вершин меньше, чем количество вершин в
   графе, и в приоритетной очереди есть элементы:
   - берем ребро с вершины приоритетной очереди
   - если какой-то из концов ребра еще не добавлен в остов, то:
     - добавляем ребро и тот конец, которого нет в остове, в остов.
     - увеличиваем вес остова на вес добавленного ребра
     - добавляем в приоритетную очередь все ребра к смежным вершинам, при
       условии, что эти вершины отсутствуют в остове.
4. Если количество вершин, добавленных в остов меньше, чем количество вершин
   в графе, значит остонвное дерево не построено (возвращаем -1), иначе
   возвращаем вес остовного дерева.

Вычислительная сложность:
Вычислительная сложность класса Heap в худшем случае - O(log(m)), где m -
количество ребер.
Вычислительная сложность функции ostovTree в худшем случае - O(max(n,m)log(m)),
где n - количество вершин в графе, т.к. добавление и извлечение из приоритетной
очереди делаем в худшем случае для каждого ребра.
Вычислительная сложность формирования графа - О(m)
Общая вычислительная сложность - O(m + max(n,m)log(m))

Пространственная сложность:
В классе Heap выделяется память под хранение элементов кучи. Ее объем прямо
зависит от количества элементов кучи (количества ребер графа m).
Такими образом пространственная сложность оценивается как O(m).
Затраты на рекурсивные вызовы - O(log(m))
Общая пространственная сложность класса Heap - O(m+log(m))
В функции ostovTree дополнительная память выделяется для хранения признака
добавления вершины в остов - оценка O(n)
В основной программе выделяется память для хранения вершин графа и его ребер -
оценка O(n+m)
Общая пространственная сложность - O(2*(n+m)+log(m))
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
