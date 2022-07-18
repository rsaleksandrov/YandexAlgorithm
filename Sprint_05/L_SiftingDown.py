"""
Напишите функцию, совершающую просеивание вниз в куче на максимум.
Гарантируется, что порядок элементов в куче может быть нарушен только
элементом, от которого запускается просеивание.
Функция принимает в качестве аргументов массив, в котором хранятся элементы
кучи, и индекс элемента, от которого надо сделать просеивание вниз.
Функция должна вернуть индекс, на котором элемент оказался после просеивания.
Также необходимо изменить порядок элементов в переданном в функцию массиве.
Индексация в массиве, содержащем кучу, начинается с единицы.
Таким образом, сыновья вершины на позиции v это 2v и 2v+1.
Обратите внимание, что нулевой элемент в передаваемом массиве фиктивный,
вершина кучи соответствует 1-му элементу.

Формат ввода
Элементы кучи —– целые числа, лежащие в диапазоне от −10^9 до 10^9.
Все элементы кучи уникальны. Передаваемый в функцию индекс лежит в
диапазоне от 1 до размера передаваемого массива.
В куче содержится от 1 до 10^5 элементов.

Python
def sift_down(heap: list, idx: int) -> int
"""


def sift_down(heap, idx) -> int:
    left = idx * 2
    right = idx * 2 + 1

    lchp = left < len(heap)  # Left child is present
    rchp = right < len(heap)  # Right child is present

    if not lchp and not rchp:
        return idx

    if lchp and rchp:
        if heap[left] < heap[right]:
            largest_index = right
        else:
            largest_index = left
    elif lchp:
        largest_index = left
    else:
        largest_index = right

    if heap[idx] < heap[largest_index]:
        heap[idx], heap[largest_index] = heap[largest_index], heap[idx]
        return sift_down(heap, largest_index)
    else:
        return idx
    pass


def test():
    # sample = [-1, 12, 1, 8, 3, 4, 7]
    sample = [-1, 12, 4, 7, 3, 1, 8]
    assert sift_down(sample, 3) == 6


def test2():
    # sample = [-1, 12, 1, 8, 3, 4, 7]
    sample = [-1, 60, 70, 50]
    res = sift_down(sample, 1)
    print(res, sample)


if __name__ == '__main__':
    test()
