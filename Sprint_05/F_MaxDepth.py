"""
Алла хочет побывать на разных островах архипелага Алгосы. Она составила карту.
Карта представлена в виде дерева: корень обозначает центр архипелага,
узлы –— другие острова. А листья —– это дальние острова, на которые
Алла хочет попасть.
Помогите Алле определить максимальное число островов, через которые ей нужно
пройти для совершения одной поездки от стартового острова до места назначения,
включая начальный и конечный пункты.
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
Функция должна вернуть число, равное максимальному числу островов в пути
(включая начальный и конечный пункты).
"""


# Comment it before submitting
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def calcMaxDepth(root):
    tLMH = 0
    tRMH = 0

    if root.left is None and root.right is None:
        return 1

    if root.left is not None:
        tLMH = calcMaxDepth(root.left)

    if root.right is not None:
        tRMH = calcMaxDepth(root.right)

    tmpTreeHight = max(tLMH, tRMH) + 1

    return tmpTreeHight
    pass


def solution(root) -> int:
    return calcMaxDepth(root)
    pass


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5) == 3


if __name__ == '__main__':
    test()
