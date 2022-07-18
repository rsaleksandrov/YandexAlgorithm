"""
Напишите функцию, которая будет выводить по неубыванию все ключи от L до R
включительно в заданном бинарном дереве поиска.
Ключи в дереве могут повторяться. Решение должно иметь сложность O(h+k), где
h – глубина дерева, k — число элементов в ответе.
В данной задаче если в узле содержится ключ x, то другие ключи, равные x,
могут быть как в правом, так и в левом поддереве данного узла.
(Дерево строил стажёр, так что ничего страшного).
см рисунок

Формат ввода
На вход функции подаётся корень дерева и искомый ключ. Число вершин в дереве
не превосходит 10^5. Ключи – натуральные числа, не превосходящие 10^9.
Гарантируется, что L≤R.

В итоговом решении не надо определять свою структуру / свой класс,
описывающий вершину дерева.
Замечания про отправку решений

Python
# do not declare Node in your submit-file
class Node:
    def __init__(self, left=None, right=None, value=0):
        self.value = value
        self.right = right
        self.left = left
#################
def print_range(node: Node, l: int, r: int) -> pass\

----------------------------

Псевдокод для центрированного подхода выглядит так:
функция print_LMR(vertex)
  если vertex.left != None тогда print_LMR(vertex.left)
  print(vertex.value)
  если vertex.right != None тогда print_LMR(vertex.right)
"""


# Comment it before submitting
class Node:
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value

    def __repr__(self):
        return str(self.value)


def print_CLRM(root, l, r, res):
    if root.value >= l and root.left is not None:
        print_CLRM(root.left, l, r, res)
    if l <= root.value <= r:
        res.append(root.value)
    if (root.value <= r) and root.right is not None:
        print_CLRM(root.right, l, r, res)
    pass


def print_range(node, l, r):
    res = []
    print_CLRM(node, l, r, res)
    print(*res)
    pass


def test():
    node1 = Node(None, None, 2)
    node2 = Node(None, node1, 1)
    node3 = Node(None, None, 8)
    node4 = Node(None, node3, 8)
    node5 = Node(node4, None, 9)
    node6 = Node(node5, None, 10)
    node7 = Node(node2, node6, 5)
    print_range(node7, 2, 8)
    # expected output: 2 5 8 8


if __name__ == '__main__':
    test()
