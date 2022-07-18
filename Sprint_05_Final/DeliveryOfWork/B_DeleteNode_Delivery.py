"""
ID 68629785

Реализованы два вспомогательных метода:
findElem - поиск узла в дереве
findFarRightNode - поиск крайнего правого узла

Алгоритм удаления:
1. Ищем в дереве удаляемый узел, его родителя и какой он у родителя (левый или
правый).
2. Если узел не найден, возвращаем переданный корень дерева
3. Если удаляемый узел является корнем дерева, то:
3.1 Если у него нет потомков, то это последний узел, возвращаем None.
3.2 Если у него есть только один потомок, то назначаем его в качестве ного
корня, разрываем связь и возвращаем новый корень.
3.3 Если присутствую оба потомка, то ищем в левом поддереве крайний правый
узел и его родителя.
3.3.1 Если родитель крайнего правого узла совпадает с удаляемым
узлом, то подцепляем правое поддерево удаляемого узла как правое
поддерево крайнего правого узла, разрываем связи удаляемого узла с потомками
и возвращаем в качестве нового корня крайний правый узел.
3.3.2 В противном случае к правой ветке родителя крайнего равого узла
подцепляем левое поддерево крайнего правого узла, перебрасываем левое и
правое поддеревья удаляемого узла на крайний правый узел, разрываем связи
удаляемого узла со своими потомками и возвращаем в качестве нового корня
крайний правый узел.
4. Удаляемый узел не является корнем.
4.1 Если у удаляемого узла нет потомков, то разрываем соответствующую (левую
или правую) связь с родителем и возвращаем исходный корень.
4.2 Если у удаляемого узла есть только правое поддерево, по подцепляем его к
соответствующей (левой или правой) ветке родителя удаляемого элемента,
разрываем связь удаляемого элемента с родителем и возвращаем исходный корень.
4.3 У удаляемого узла есть или только левое поддерево или и левое и правое
поддеревья:
4.3.1 Ищем крайний правый узел в левом поддереве удаляемого узла и
его родителя
4.3.2 Если родитель крайнего правого узла совпадает с удаляемым
узлом, то привязываем карйний правый узел к соответствующей (левой
или правой) ветви родителя удаляемого узла, правое поддерево удаляемого
узла привязываем к правой ветке крайнего правого узла, разрываем связи
удаляемого узла со своими поддеревьями и возвращаем исходный корень
4.3.2 В противном случае привязываем крайний правый узел к соответствующей
(левой или правой) ветке родителя удаляемого узла, левое поддерево крайнего
правого узла привязываем к правой ветке родителя крайнего правого узла,
перепривязываем левое и правое поддеревья удаляемого узла к крайнему правому
узлу, разрываем связи удаляемого узлас поддеревьями и возвращаем исходный
корень.

Вычислительная сложность:
Поиск удаляемого узла и поиск кранего правого узла в худшем случае O(log(h)),
где h - высота дерева. Так как операции последовательные, то общая
вычислительная сложность - O(log(h))

Пространственная сложность:
Так как алгоритм работает с передаваемым деревом и не выделяет
дополнительной памяти, то пространственная сложность - O(1)
Затраты на рекурсивные вызовы - O(log(h))
Общая пространственная сложность алгоритма - O(log(h))
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


if __name__ == '__main__':
    test()
