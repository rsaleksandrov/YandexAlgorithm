"""
Вечером ребята решили поиграть в игру «Большое число».
Даны числа. Нужно определить, какое самое большое число можно из них составить.

Формат ввода
В первой строке записано n — количество чисел. Оно не превосходит 100.
Во второй строке через пробел записаны n неотрицательных чисел, каждое из
которых не превосходит 1000.

Формат вывода
Нужно вывести самое большое число, которое можно составить из данных чисел.
"""

"""
Лексикографическое сравнение
Сначала сравниваются первые элементы последовательностей, и, если они 
отличаются, то результат их сравнения определяет результат; если они равны, 
сравниваются следующие элементы и т.д., пока не будет определен результат 
или одна из последовательностей не будет исчерпана. 
Если два элемента сами являются последовательностями одного типа, 
то лексикографическое сравнение выполняется рекурсивно. Если все элементы 
двух последовательностей в результате сравнения оказываются равными, то 
последовательности считаются равными. Если одна из последовательностей 
является началом другой, то меньшей считается последовательность с меньшим 
количеством элементов. Лексикографический порядок строк определяется порядком 
следования ASCII символов.
"""


def leksCompare(s1, s2):
    """
    Функция производит лексикографическое сравнение строк
    :param s1: первая строка
    :param s2: вторая строка
    :return: 0 - строки равны, 1 - первая строка меньше второй, -1 - вторая
    строка меньше первой
    """
    if len(s1) == len(s2):
        lens = len(s1)
    else:
        lens = len(s1) + len(s2)

    for i in range(lens):
        if i < len(s1):
            ch1 = s1[i]
        else:
            # return True  # 1
            return -1

        if i < len(s2):
            ch2 = s2[i]
        else:
            # return False  # -1
            return 1

        if ch1 != ch2:
            if ch1 < ch2:
                # return True  # 1
                return 1
            else:
                # return False  # -1
                return -1
    # return False  # 0
    return 0


def mycompare(s1, s2):
    if len(s1) == len(s2):
        lens = len(s1)
    else:
        lens = len(s1) + len(s2)

    for i in range(lens):
        if i < len(s1):
            ch1 = s1[i]
        else:
            ch1 = s2[i - len(s1)]

        if i < len(s2):
            ch2 = s2[i]
        else:
            ch2 = s1[i - len(s2)]

        if ch1 != ch2:
            if ch1 < ch2:
                return True
            else:
                return False
    return False


def BubbleSort(pData, pCompare):
    """
    Сортировка массива pData с использованием функции сравнения pCompare
    :param pData: сортирууемый массив
    :param pCompare: функция сравнения
    """
    isStop = False
    while not isStop:
        needRepeat = False
        for i in range(len(pData) - 1):
            if pCompare(pData[i], pData[i + 1]) == 1:
                needRepeat = True
                # print('\t', pData[i], pData[i + 1], '-->', pData[i + 1],
                #       pData[i])
                pData[i], pData[i + 1] = pData[i + 1], pData[i]
        if not needRepeat:
            isStop = True
        # print(*pData)


if __name__ == '__main__':
    n = int(input())
    iData = input().split()
    # BubbleSort(iData, leksCompare)
    BubbleSort(iData, mycompare)
    print(''.join(iData))
