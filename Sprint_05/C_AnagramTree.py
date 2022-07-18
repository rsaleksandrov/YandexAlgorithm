"""
Гоша и Алла играют в игру «Удивительные деревья». Помогите ребятам определить,
является ли дерево, которое им встретилось, деревом-анаграммой?
Дерево называется анаграммой, если оно симметрично относительно своего центра.
см рис

Формат ввода
Напишите функцию, которая определяет, является ли дерево анаграммой.
На вход подаётся корень дерева.

Python:
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left
Ваша функция должна иметь сигнатуру solution(root: Node) -> bool.


Формат вывода
Функция должна вернуть True если дерево является анаграммой. Иначе - False.
"""


# Comment it before submitting
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self):
        return str(self.value)


def checkTrees(root1, root2):
    vc = root1.value == root2.value
    lnpc = (root1.left is None and root2.right is None) or (
            root1.left is not None and root2.right is not None)
    rnpc = (root1.right is None and root2.left is None) or (
            root1.right is not None and root2.left is not None)
    res = vc and lnpc and rnpc

    if not res:
        return False

    if root1.left is not None:
        res = checkTrees(root1.left, root2.right)

    if res and root1.right is not None:
        res = checkTrees(root1.right, root2.left)

    return res
    pass


def solution(root):
    if root.left is not None and root.right is not None:
        return checkTrees(root.left, root.right)

    if root.left is None and root.right is None:
        return True
    else:
        return False
    pass


def test():
    node8 = Node(5, None, None)
    node1 = Node(3, None, None)
    node2 = Node(4, node8, None)
    node3 = Node(4, None, None)
    node4 = Node(3, None, None)
    node5 = Node(2, node1, node2)
    node6 = Node(2, node3, node4)
    node7 = Node(1, node5, node6)
    assert not solution(node7)


if __name__ == '__main__':
    test()
