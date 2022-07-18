"""
Дано бинарное дерево поиска, в котором хранятся ключи. Ключи — уникальные
целые числа. Найдите вершину с заданным ключом и удалите её из дерева так,
чтобы дерево осталось корректным бинарным деревом поиска. Если ключа в дереве
нет, то изменять дерево не надо.
На вход вашей функции подаётся корень дерева и ключ, который надо удалить.
Функция должна вернуть корень изменённого дерева. Сложность удаления узла
должна составлять O(h), где h — высота дерева.
Создавать новые вершины (вдруг очень захочется) нельзя.

Формат ввода
Ключи дерева – натуральные числа, не превышающие 10^9.
В итоговом решении не надо определять свою структуру/свой класс,
описывающий вершину дерева.
Мы рекомендуем воспользоваться заготовками кода для данной задачи,
расположенными по ссылке.

Формат вывода

По умолчанию выбран компилятор Make. Решение нужно отправлять в виде файла
с расширением, которое соответствует вашему языку программирования.
Ниже приведены сигнатуры функций, которые надо реализовать.
Python
# do not declare Node in your submit-file
class Node:
    def __init__(self, left=None, right=None, value=0):
        self.value = value
        self.right = right
        self.left = left

def remove(root: Node, key: int) -> Node
"""


# Comment it before submitting
class Node:
    def __init__(self, left=None, right=None, value=0):
        # def __init__(self, value=0, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value

    def __repr__(self):
        return str(self.value)


class NodeDirect:
    left = 1
    right = 2
    undefine = -1


def findElem(root, parent, direct: int, key):
    if root is None:
        return parent, root, direct

    if root.value == key:
        return parent, root, direct

    if key < root.value:
        return findElem(root.left, root, NodeDirect.left, key)
    else:
        return findElem(root.right, root, NodeDirect.right, key)


def findFarRightNode(root, parent):
    if root is None:
        return parent, root

    if root.right is None:
        return parent, root
    else:
        return findFarRightNode(root.right, root)


def remove(root, key):
    delNodeParent, delNode, delNodeDirect = findElem(root, None,
                                                     NodeDirect.undefine, key)
    if delNode is None:
        return root

    if delNode is root:  # Удаляемая вершина - корень
        # Потомков нет
        if delNode.left is None and delNode.right is None:
            return None

        # Только левый потомок
        if delNode.left is not None and delNode.right is None:
            newroot = delNode.left
            delNode.left = None
            return newroot

        # Только правый потомок
        if delNode.left is None and delNode.right is not None:
            newroot = delNode.right
            delNode.right = None
            return newroot

        # Оба потомка
        if delNode.left is not None and delNode.right is not None:
            # Ищем крайний правый узел в левом поддереве
            farRightParent, farRight = findFarRightNode(delNode.left, delNode)

            # Родитель крайнего правого узла совпадает с удаляемым узлом
            if farRightParent is delNode:
                farRight.right = delNode.right
                delNode.left = None
                delNode.right = None
                return farRight
            else:
                if farRight.left is None:
                    farRight.left = delNode.left
                    farRight.right = delNode.right
                    delNode.left = None
                    delNode.right = None
                    farRightParent.right = None
                    return farRight
                else:
                    farRightParent.right = farRight.left
                    farRight.left = delNode.left
                    farRight.right = delNode.right
                    delNode.left = None
                    delNode.right = None
                    return farRight
        pass
    else:  # Удаляемая вершина - не корень
        # У удаляемого узла отсутствуют потомки
        if delNode.left is None and delNode.right is None:
            if delNodeDirect == NodeDirect.left:
                delNodeParent.left = None
            else:
                delNodeParent.right = None
            return root

        # У удаляемого узла есть только правый потомок
        if delNode.left is None:
            if delNodeDirect == NodeDirect.left:
                delNodeParent.left = delNode.right
            else:
                delNodeParent.right = delNode.right
            delNode.right = None
            return root
        # Ищем крайний правый узел в левом поддереве удаляемого узла
        farRightParent, farRight = findFarRightNode(delNode.left, delNode)

        # Родитель крайнего правого узла совпадает с удаляемым
        if farRightParent is delNode:
            if delNodeDirect == NodeDirect.left:
                delNodeParent.left = farRight
            else:
                delNodeParent.right = farRight
            farRight.right = delNode.right
            delNode.left = None
            delNode.right = None
            farRightParent.right = None
            return root

        # У крайнего правого узла нет потомков
        if farRight.left is None and farRight.right is None:
            if delNodeDirect == NodeDirect.left:
                delNodeParent.left = farRight
            else:
                delNodeParent.right = farRight
            farRight.left = delNode.left
            farRight.right = delNode.right
            delNode.left = None
            delNode.right = None
            farRightParent.right = None
            return root
        else:
            if delNodeDirect == NodeDirect.left:
                delNodeParent.left = farRight
            else:
                delNodeParent.right = farRight
            farRightParent.right = farRight.left
            farRight.left = delNode.left
            farRight.right = delNode.right
            delNode.left = None
            delNode.right = None
            return root
        pass
    pass


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    newHead = remove(node7, 10)

    assert newHead.value == 5
    assert newHead.right is node5
    assert newHead.right.value == 8
    pass


def test2():
    # node10 = Node(99, None, None)
    # node9 = Node(72, None, None)
    # node8 = Node(91, node9, node10)
    # node7 = Node(50, None, None)
    # node6 = Node(32, None, None)
    # node5 = Node(29, None, node6)
    # node4 = Node(11, None, None)
    # node3 = Node(65, node7, node8)
    # node2 = Node(20, node4, node5)
    # node1 = Node(41, node2, node3)
    # newhead = remove(node1, 41)
    # print(newhead)
    pass


def test3():
    # node2 = Node(2, None, None)
    # node1 = Node(1, None, node2)
    # newhead = remove(node1, 1)
    # print(newhead)
    pass


def test4():
    # node4 = Node(4, None, None)
    # node3 = Node(3, None, node4)
    # node2 = Node(2, None, node3)
    # node1 = Node(1, None, node2)
    # newhead = remove(node1, 3)
    # print(newhead)
    pass


def test5():
    # node10 = Node(840, None, None)
    # node9 = Node(708, None, None)
    # node8 = Node(609, None, None)
    # node7 = Node(568, None, node8)
    # node6 = Node(626, node7, None)
    # node5 = Node(649, node6, node9)
    # node4 = Node(818, node5, node10)
    # node3 = Node(270, None, None)
    # node2 = Node(355, node3, None)
    # node1 = Node(460, node2, node4)
    # newhead = remove(node1, 568)
    # print(newhead)
    pass


def test6():
    tmp = input()
    n = int(input())
    iData = [''] * n
    for i in range(n):
        iData[i] = input()
    nodes = [None] * n
    for el in iData[::-1]:
        nnode, nvalue, nleft, nright = list(map(int, el.split()))
        node = Node(None if nleft == -1 else nodes[nleft - 1],
                    None if nright == -1 else nodes[nright - 1], nvalue)
        nodes[nnode - 1] = node
    key = int(input())
    newhead = remove(nodes[0], key)
    print(tmp, newhead)
    pass


if __name__ == '__main__':
    test6()
