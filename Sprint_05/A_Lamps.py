"""
Гоша повесил на стену гирлянду в виде бинарного дерева, в узлах которого
находятся лампочки. У каждой лампочки есть своя яркость. Уровень яркости
лампочки соответствует числу, расположенному в узле дерева. Помогите Гоше
найти самую яркую лампочку в гирлянде, то есть такую, у которой яркость
наибольшая.
см рисунок

Формат ввода
На вход подается корень дерева.
Замечания про отправку решений
По умолчанию выбран компилятор make. Решение нужно отправлять в виде файла с
расширением, которое соответствует вашему языку программирования.

Мы рекомендуем воспользоваться заготовками кода для данной задачи,
расположенными по ссылке.
Python:
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left
Ваша функция должна иметь сигнатуру solution(Node) -> int.

Формат вывода
Функция должна вернуть максимальное значение яркости в узле дерева.
"""


# Comment it before submitting
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def findTreeMax(root, pMaxValue) -> int:
    if root is None:
        return pMaxValue

    if root.value > pMaxValue:
        pMaxValue = root.value

    if root.left is not None:
        tmpMax = findTreeMax(root.left, pMaxValue)
        if tmpMax > pMaxValue:
            pMaxValue = tmpMax

    if root.right is not None:
        tmpMax = findTreeMax(root.right, pMaxValue)
        if tmpMax > pMaxValue:
            pMaxValue = tmpMax

    return pMaxValue


def solution(root) -> int:
    return findTreeMax(root, root.value)
    pass


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node5 = Node(15)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, node5)
    assert solution(node4) == 15


if __name__ == '__main__':
    test()
