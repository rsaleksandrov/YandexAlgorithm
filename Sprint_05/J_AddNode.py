"""
Дано BST. Надо вставить узел с заданным ключом. Ключи в дереве могут
повторяться. На вход функции подаётся корень корректного бинарного дерева
поиска и ключ, который надо вставить в дерево. Осуществите вставку этого
ключа. Если ключ уже есть в дереве, то его дубликаты уходят в правого сына.
Таким образом вид дерева после вставки определяется однозначно.
Функция должна вернуть корень дерева после вставки вершины.
Ваше решение должно работать за O(h), где h — высота дерева.
На рисунках ниже даны два примера вставки вершин в дерево.

Формат ввода
Ключи дерева – натуральные числа, не превосходящие 10^9.
Число вершин в дереве не превосходит 10^5.

Замечания про отправку решений
Python
# do not declare Node in your submit-file
class Node:
    def __init__(self, left=None, right=None, value=0):
        self.value = value
        self.right = right
        self.left = left

from node import Node # Attention!
def insert(root: Node, key: int) -> Node
"""

# Uncomment it before submitting
from node import Node

# Comment it before submitting
# class Node:
#     def __init__(self, left=None, right=None, value=0):
#         self.right = right
#         self.left = left
#         self.value = value


def insert(root, key):
    if key < root.value:
        if root.left is not None:
            insert(root.left, key)
        else:
            root.left = Node(None, None, key)
    else:
        if root.right is not None:
            insert(root.right, key)
        else:
            root.right = Node(None, None, key)
    return root
    pass


def test():
    node1 = Node(None, None, 7)
    node2 = Node(node1, None, 8)
    node3 = Node(None, node2, 7)
    new_head = insert(node3, 6)
    assert new_head is node3
    assert new_head.left.value == 6


if __name__ == '__main__':
    test()
