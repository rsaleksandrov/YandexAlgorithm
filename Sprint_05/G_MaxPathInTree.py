"""
Тимофей устраивает соревнования по спортивному ориентированию в своём офисе.
Схема офиса представлена в виде дерева. Посещая каждый пункт, можно
зарабатывать или терять очки. Если в узле записано положительное число,
это значение добавляется к текущему количеству очков участника.
Если отрицательное —– очки вычитаются. Если 0 — их количество не меняется.
Нужно определить, какое максимальное число очков можно заработать, пройдя
по пути из какого-то пункта A в какой-то (возможно, тот же) пункт B.
Путь не обязательно должен проходить через корень или содержать лист.
Путь должен содержать по крайней мере один узел.

Пример 1 (см рисунки):
В дереве всего три вершины, во всех вершинах записаны положительные числа,
поэтому объединим все три вершины в один путь. В ответе получим:
1+1+2=4.
Пример 2:
Теперь в дереве есть вершина с отрицательным весом,
через неё в данном случае проходить будет невыгодно. Оптимальный путь:
2+7+3=12.
Пример 3:
Оптимальный путь:
7+2+3+9=21.
Пример 4:
В этот раз имеет смысл пройти через вершину с отрицательным весом,
так как в левом поддереве вершины −3 лежит 5. Оптимальный путь:
2+2−3+5=6.

Требования к решению: передаваемое в качестве аргумента дерево нельзя менять.
Не храните вспомогательную информацию в вершинах.

Формат ввода
На вход подается корень дерева.
Python:
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left
Ваша функция должна иметь сигнатуру solution(node: Node) -> int.

Формат вывода
Функция должна вернуть число, равное максимальному количеству очков,
которое можно заработать, попав из города А в город В.
"""


# Comment it before submitting
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self):
        return str(self.value)


def searchMaxPath(root, maxSum=None):
    tmpMaxSum = maxSum

    if root is None:
        return 0, maxSum
    # Расчитываем максимальную сумму в левой и правой ветках текущего узла
    lms, tmpMaxSum = searchMaxPath(root.left, tmpMaxSum)
    rms, tmpMaxSum = searchMaxPath(root.right, tmpMaxSum)

    # определяем максимальную сумму ветки с учетом текущего узла
    branchMaxSum = max(max(lms, rms) + root.value, root.value)

    # Определяем максимальную сумму поддерева с текущим узлом в корне
    subTreeMaxSum = max(branchMaxSum, lms + rms + root.value)

    # Корректируем "глобальную" максимальную сумму
    if tmpMaxSum is None:
        tmpMaxSum = subTreeMaxSum
    else:
        tmpMaxSum = max(subTreeMaxSum, tmpMaxSum)

    # Возвращаем максимальную сумму по ветке (левой или правой) с учетом
    # текущего узла и "глобальную" максимальную сумму
    return branchMaxSum, tmpMaxSum


def solution(root) -> int:
    mbs, mts = searchMaxPath(root, None)
    return mts
    pass


def test():
    node1 = Node(5, None, None)
    node2 = Node(1, None, None)
    node3 = Node(-3, node2, node1)
    node4 = Node(2, None, None)
    node5 = Node(2, node4, node3)
    assert solution(node5) == 6


if __name__ == '__main__':
    test()
