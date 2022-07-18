"""
Гоше очень понравилось слушать рассказ Тимофея про деревья.
Особенно часть про сбалансированные деревья. Он решил написать функцию,
которая определяет, сбалансировано ли дерево.
Дерево считается сбалансированным, если левое и правое поддеревья каждой
вершины отличаются по высоте не больше, чем на единицу.
См рисунок

Формат ввода
На вход функции подаётся корень бинарного дерева.
Python:
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left
Ваша функция должна иметь сигнатуру solution(Node root) -> bool.

Формат вывода
Функция должна вернуть True, если дерево сбалансировано в соответствии
с критерием из условия, иначе - False.
"""


# Comment it before submitting
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self):
        return str(self.value)


def checkTreeBal(root):
    tmpCorr = True
    tLMH = 0
    tRMH = 0

    if root.left is None and root.right is None:
        return True, 1  # Correct, maxHight

    if root.left is not None:
        tmpCorr, tLMH = checkTreeBal(root.left)

    if tmpCorr and root.right is not None:
        tmpCorr, tRMH = checkTreeBal(root.right)

    tmpTreeHight = max(tLMH, tRMH) + 1

    tmpCorr = tmpCorr and abs(tLMH - tRMH) <= 1

    return tmpCorr, tmpTreeHight
    pass


def solution(root):
    Corr, TH = checkTreeBal(root)
    # print(f'Correct {Corr}, Tree hight {TH}')
    return Corr
    pass


def test():
    node1 = Node(1)
    # node6 = Node(-7)
    # node2 = Node(-5, node6)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


if __name__ == '__main__':
    test()
