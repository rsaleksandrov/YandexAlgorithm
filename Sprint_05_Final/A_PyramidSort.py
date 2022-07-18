"""
В данной задаче необходимо реализовать сортировку кучей. При этом кучу
необходимо реализовать самостоятельно, использовать имеющиеся в языке
реализации нельзя. Сначала рекомендуется решить задачи про просеивание
вниз и вверх.

Тимофей решил организовать соревнование по спортивному программированию,
чтобы найти талантливых стажёров. Задачи подобраны, участники зарегистрированы,
тесты написаны. Осталось придумать, как в конце соревнования будет
определяться победитель.

Каждый участник имеет уникальный логин. Когда соревнование закончится,
к нему будут привязаны два показателя: количество решённых задач Pi и размер
штрафа Fi. Штраф начисляется за неудачные попытки и время, затраченное
на задачу.

Тимофей решил сортировать таблицу результатов следующим образом: при
сравнении двух участников выше будет идти тот, у которого решено больше
задач. При равенстве числа решённых задач первым идёт участник с меньшим
штрафом. Если же и штрафы совпадают, то первым будет тот, у которого логин
идёт раньше в алфавитном (лексикографическом) порядке.

Тимофей заказал толстовки для победителей и накануне поехал за ними в магазин.
В своё отсутствие он поручил вам реализовать алгоритм сортировки кучей
(англ. Heapsort) для таблицы результатов.

Формат ввода
В первой строке задано число участников n, 1 ≤ n ≤ 100 000.
В каждой из следующих n строк задана информация про одного из участников.
i-й участник описывается тремя параметрами:
уникальным логином (строкой из маленьких латинских букв длиной не более 20)
числом решённых задач Pi
штрафом Fi
Fi и Pi — целые числа, лежащие в диапазоне от 0 до 10^9.

Формат вывода
Для отсортированного списка участников выведите по порядку их логины по
одному в строке.
"""
# Пирамидальная сортировка с использованием кучи
# import random


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


def test():
    maxFirst = False
    heapsize = 10
    heap = Heap(heapsize, maxFirst)
    for i in range(heapsize):
        # heap.add(random.randint(-100, 100))
        heap.add(i)
        # print(f'ADD: {i} -> {heap}')

    heapsort = []
    for i in range(heapsize):
        res = heap.getheadelem()
        heapsort.append(res)
        # print(f'REMOVE: {i} -> {heap}')

    if maxFirst:
        hs1 = sorted(heapsort, reverse=True)
    else:
        hs1 = sorted(heapsort, reverse=False)
    print(heapsort)
    print(hs1)

    print(heapsort == hs1)
    pass


def test2():
    # data = [92, 86, 62, 8, 6, 5, -17, -35, -96, -60]
    data = [86, 77, 74, 68, 50, 28, 23, 8, 1, 2]
    maxFirst = True
    heapsize = 10
    heap = Heap(heapsize, maxFirst)
    for el in data:
        heap.add(el)
        print(f'ADD: {el} -> {heap}')

    heapsort = []
    for i in range(heapsize):
        res = heap.getheadelem()
        heapsort.append(res)
        print(f'REMOVE: {i} -> {heap}')

    if maxFirst:
        hs1 = sorted(heapsort, reverse=True)
    else:
        hs1 = sorted(heapsort, reverse=False)
    print(heapsort)
    print(hs1)

    print(heapsort == hs1)


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
