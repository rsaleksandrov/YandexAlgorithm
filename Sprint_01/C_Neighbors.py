"""
Дана матрица. Нужно написать функцию, которая для элемента возвращает всех
его соседей. Соседним считается элемент, находящийся от текущего на одну
ячейку влево, вправо, вверх или вниз. Диагональные элементы соседними не
считаются.

Например, в матрице A (см. рисунок)
соседними элементами для (0, 0) будут 2 и 0. А для (2, 1) –— 1, 2, 7, 7.

Формат ввода
В первой строке задано n — количество строк матрицы.
Во второй — количество столбцов m. Числа m и n не превосходят 1000.
В следующих n строках задана матрица. Элементы матрицы — целые числа,
по модулю не превосходящие 1000.
В последних двух строках записаны координаты элемента
(индексация начинается с нуля), соседей которого нужно найти.

Формат вывода
Напечатайте нужные числа в возрастающем порядке через пробел.
"""


def getNeighbors(pMatrix, pRows, pCols, pElRow, pElCol):
    """
    Функция ищет соседние элементы в pMatrix для элемента (pElRows, pElCols)
    :param pMatrix: матрица элементов
    :param pCols: количество столбцов в матрице
    :param pRows: количество столбцов в матрице
    :param pElCol: столбец элемента, для которого ищем соседей
    :param pElRow: строка элемента, для которого ищем соседей
    :return: список соседй элемента (pElRows, pElCols) в возрастающем порядке
    """
    mNeighbors = []

    if pElRow - 1 >= 0:
        mNeighbors.append(pMatrix[pElRow - 1][pElCol])
    if pElRow + 1 < pRows:
        mNeighbors.append(pMatrix[pElRow + 1][pElCol])
    if pElCol - 1 >= 0:
        mNeighbors.append(pMatrix[pElRow][pElCol - 1])
    if pElCol + 1 < pCols:
        mNeighbors.append(pMatrix[pElRow][pElCol + 1])

    mNeighbors.sort()
    return mNeighbors


mRows = int(input())  # Row count
mCols = int(input())  # Col count
matrix = []
for i in range(mRows):
    tmpRow = list(map(int, input().split()))
    matrix.append(tmpRow)
elRow = int(input())
elCol = int(input())
res = getNeighbors(matrix, mRows, mCols, elRow, elCol)
print(*res)
