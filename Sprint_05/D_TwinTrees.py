"""
Гоше на день рождения подарили два дерева. Тимофей сказал, что они
совершенно одинаковые. Но, по мнению Гоши, они отличаются.
Помогите разрешить этот философский спор!
см рис

Формат ввода
На вход подаются корни двух деревьев.

Класс, представляющий узел дерева.
Python:
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left
Ваша функция должна иметь сигнатуру solution(root1: Node, root2: Node) -> bool.

Формат вывода
Функция должна вернуть True если деревья являются близнецами. Иначе - False.
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
    lnpc = (root1.left is None and root2.left is None) or (
            root1.left is not None and root2.left is not None)
    rnpc = (root1.right is None and root2.right is None) or (
            root1.right is not None and root2.right is not None)
    res = vc and lnpc and rnpc

    if not res:
        return False

    if root1.left is not None:
        res = checkTrees(root1.left, root2.left)

    if res and root1.right is not None:
        res = checkTrees(root1.right, root2.right)

    return res
    pass


def solution(root1, root2):
    res = checkTrees(root1, root2)
    return res
    pass


def test():
    node1 = Node(1, None, None)
    # node7 = Node(4, None, None)
    node2 = Node(2, None, None)
    node3 = Node(3, node1, node2)

    node4 = Node(1, None, None)
    node5 = Node(2, None, None)
    node6 = Node(3, node4, node5)

    assert solution(node3, node6)


if __name__ == '__main__':
    test()
