"""
Гоша понял, что такое дерево поиска, и захотел написать функцию, которая
определяет, является ли заданное дерево деревом поиска. Значения в левом
поддереве должны быть строго меньше, в правом —- строго больше значения в узле.
Помогите Гоше с реализацией этого алгоритма.
см рис.

Формат ввода
На вход функции подается корень бинарного дерева.
Замечания про отправку решений
По умолчанию выбран компилятор make. Решение нужно отправлять в виде файла
с расширением, которое соответствует вашему языку программирования.

Python:
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left
Ваша функция должна иметь сигнатуру solution(root: Node) -> bool.
"""


# Comment it before submitting
class Node:
    def __init__(self, value: int = 0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def treeByPass(root: Node, maxel):
    result = True
    if root.left is not None:
        maxel, result = treeByPass(root.left, maxel)
    if result:
        if maxel is None:
            maxel = root.value
        else:
            if root.value > maxel:
                maxel = root.value
            else:
                result = False
    if result:
        if root.right is not None:
            maxel, result = treeByPass(root.right, maxel)
    return maxel, result


def solution(root: Node) -> bool:
    maxel, res = treeByPass(root, None)
    return res


def test():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n10 = Node(10)

    n5.left = n2
    n5.right = n8
    n2.left = n1
    n2.right = n3
    n3.right = n4
    n8.left = n7
    n8.right = n9
    n7.left = n6
    n9.right = n10

    print(solution(n5))
    pass


def test2():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


if __name__ == '__main__':
    test2()
