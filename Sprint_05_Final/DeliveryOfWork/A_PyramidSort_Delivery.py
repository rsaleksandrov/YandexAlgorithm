"""
ID 68629275

Алгоритм пирамидльной сортировки реализован на базе класса Heap.
При чтении входных данных они формируются в массив
[<число решенных задач (с обратным знаком)>, <штраф>, <имя>]
Это массив кладется в кучу. При добавлении элемента в кучу поддерживается ее
направленность (максимальный или минимальный элемент на вершине).
После добавления всех элементов в кучу последовательно забираем из кучи
верхний элемент одновременно удаляя его. При этом поддерживается корректность
расположения элементов в куче. Из полученного элемента кучи в результирующий
массив добавляем элемент с индексом 2 (имя).
После получения всех элементов из кучи выводим результирующий массив.

Класс Heap.
Класс реализует кучу с возможностью указания, какой элемент будет находится на
ее вершине - максимальный или минимальный.
Добавление элемента в кучу осуществляется с помощью метода Add. Если
свободного места в куче нет генерится исключение HeapFullExeption,
в противном случае элемент добавляется в конец кучи и вызывается метод
__sift_up (просеивание вверх) для обеспечения корректности расположения
элементов кучи. Для сравнения элементов используется метод __compare.
Получение элемента с вершины кучи реализуется методом getheadelem. В качестве
параметра можно указать ьребется или нет удалять элемент из кучи. Если
элемент удаляется из кучи, то на его место ставиться последний элемент кучи и
с помощью метода __sift_down восстанавливается структура кучи.

Вычислительная сложность:
Вычислительная сложность основной программы - O(n) (два последовательных цикла
по количеству элементов)
Вычислительная сложность класса Heap в худшем случае - O(log(n))
Вычислительная сложность всей программы - O(nlog(n)), так как для каждого
элемента вызывается или добавление в кучу или удаление из кучи.

Пространственная сложность:
В классе Heap выделяется память под хранение элементов кучи. Ее объем прямо
зависит от количества элементов кучи (n) и размера самого элемента (k).
Такми образом пространственная сложность оценивается как O(n*k).
В основной программе основной объем памяти потребляется для формирования
результирующего массива - пространственная сложность O(n*m), где m - объем
памяти, занимаемый строкой.
Затраты на рекурсивные вызовы - O(log(n))
Общая пространственная сложность алгоритма - O(n*(k+m)+log(n)).
"""


class HeapFullExeption(Exception):
    pass


class HeapEmptyExeption(Exception):
    pass


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


def main():
    n = int(input())
    heap = Heap(n, False)
    for i in range(n):
        name, p, f = input().split()
        try:
            heap.add([-int(p), int(f), name])
        except HeapFullExeption:
            print('ERROR: Heap is full')

    res = []
    for i in range(n):
        try:
            tmpr = heap.getheadelem()
            res.append(tmpr[2])
        except HeapEmptyExeption:
            print('ERROR: Heap is empty')
            break

    print('\n'.join(res))
    pass


if __name__ == '__main__':
    main()
