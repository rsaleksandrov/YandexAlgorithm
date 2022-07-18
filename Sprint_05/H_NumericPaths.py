"""
Вася и его друзья решили поиграть в игру. Дано дерево, в узлах которого
записаны цифры от 0 до 9. Таким образом, каждый путь от корня до листа
содержит число, получившееся конкатенацией цифр пути (склеиванием цифр пути
в одно число). Нужно найти сумму всех таких чисел в дереве.
Гарантируется, что ответ не превосходит 20 000.
см рис

Формат ввода
На вход подается корень дерева.

Python:
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left
Ваша функция должна иметь сигнатуру solution(root: Node) -> int.

Формат вывода
Функция должна вернуть число, равное сумме чисел всех путей в дереве.
"""


# Comment it before submitting
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self):
        return str(self.value)


def createTreePaths(root, curpath, totalsum):
    tmpts = totalsum
    curpath = curpath + str(root.value)

    if root.left is None and root.right is None:
        tmpts = totalsum + int(curpath)
        return tmpts

    if root.left is not None:
        tmpts = createTreePaths(root.left, curpath, tmpts)

    if root.right is not None:
        tmpts = createTreePaths(root.right, curpath, tmpts)

    return tmpts
    pass


def solution(root) -> int:
    ts = createTreePaths(root, '', 0)
    return ts
    pass


def test():
    node1 = Node(2, None, None)
    node2 = Node(1, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(2, None, None)
    node5 = Node(1, node4, node3)

    assert solution(node5) == 275


def test2():
    node9 = Node(9, None, None)
    node8 = Node(8, node9, None)
    node7 = Node(7, None, None)
    node6 = Node(6, None, None)
    node5 = Node(2, None, None)
    node4 = Node(4, node7, node8)
    node3 = Node(3, node5, node6)
    node2 = Node(2, None, node4)
    node1 = Node(1, node3, None)
    node0 = Node(1, node1, node2)
    assert solution(node0) == 16004


if __name__ == '__main__':
    test2()
