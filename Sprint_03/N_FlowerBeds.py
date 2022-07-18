"""
Алла захотела, чтобы у неё под окном были узкие клумбы с тюльпанам.
На схеме земельного участка клумбы обозначаются просто горизонтальными
отрезками, лежащими на одной прямой. Для ландшафтных работ было нанято n
садовников. Каждый из них обрабатывал какой-то отрезок на схеме. Процесс был
организован не очень хорошо, иногда один и тот же отрезок или его часть могли
быть обработаны сразу несколькими садовниками. Таким образом, отрезки,
обрабатываемые двумя разными садовниками, сливаются в один. Непрерывный
обработанный отрезок затем станет клумбой. Нужно определить границы будущих
клумб.

Рассмотрим примеры.
Пример 1:
Два одинаковых отрезка [7, 8] и [7, 8] сливаются в один, но потом их накрывает
отрезок [6, 10]. Таким образом, имеем две клумбы с координатами [2,3] и [6,10].

Пример 2
Отрезки [2,3], [3, 4] и [3,4] сольются в один отрезок [2,4]. Отрезок [5,6] ни
с кем не объединяется, добавляем его в ответ.

Формат ввода
В первой строке задано количество садовников n. Число садовников не
превосходит 100 000.
В следующих n строках через пробел записаны координаты клумб в формате: s
tart end, где start —– координата начала, end —– координата конца.
Оба числа целые, неотрицательные и не превосходят 10^7.
start строго меньше, чем end.

Формат вывода
Нужно вывести координаты каждой из получившихся клумб в отдельных строках.
Данные должны выводится в отсортированном порядке —– сначала клумбы с меньшими
координатами, затем —– с бОльшими.
"""


# def merge(arr, lf, mid, rg):
#     # newLength = mid - lf + rg - mid
#     resArray = []
#     id1 = lf
#     id2 = mid
#
#     while id1 < mid and id2 < rg:
#         if arr[id1][0] < arr[id2][0]:
#             resArray.append(arr[id1])
#             id1 += 1
#         elif arr[id1][0] > arr[id2][0]:
#             resArray.append(arr[id2])
#             id2 += 1
#         else:
#             resArray.append(arr[id1])
#             resArray.append(arr[id2])
#             id1 += 1
#             id2 += 1
#
#     while id1 < mid:
#         resArray.append(arr[id1])
#         id1 += 1
#
#     while id2 < rg:
#         resArray.append(arr[id2])
#         id2 += 1
#
#     return resArray
#
#
# def merge_sort(arr, lf, rg):
#     if rg - lf <= 1:
#         return
#     mid = (lf + rg) // 2
#     merge_sort(arr, lf, mid)
#     merge_sort(arr, mid, rg)
#     newArray = merge(arr, lf, mid, rg)
#     for i in range(len(newArray)):
#         arr[lf + i] = newArray[i]
#     # pass

# import sys
# import time


def merge_sort_classic(array):
    if len(array) == 1:
        return array
    left = merge_sort_classic(array[0:len(array) // 2])
    right = merge_sort_classic(array[len(array) // 2:len(array)])
    result = [None] * len(array)
    l, r, k = 0, 0, 0
    while l < len(left) and r < len(right):
        # выбираем, из какого массива забрать минимальный элемент
        if left[l][0] <= right[r][0]:
            result[k] = left[l]
            l += 1
        else:
            result[k] = right[r]
            r += 1
        k += 1

    # Если один массив закончился раньше, чем второй, то
    # переносим оставшиеся элементы второго массива в результирующий
    while l < len(left):
        result[k] = left[l]  # перенеси оставшиеся элементы left в result
        l += 1
        k += 1
    while r < len(right):
        result[k] = right[r]  # перенеси оставшиеся элементы right в result
        r += 1
        k += 1

    return result


if __name__ == "__main__":
    # oldstdin = sys.stdin
    # sys.stdin = open('N_12.txt', 'r')
    # tr_s = time.perf_counter()
    n = int(input())
    iData = []
    for i in range(n):
        tmpb, tmpe = input().split()
        iData.append([int(tmpb), int(tmpe)])
    # tr_e = time.perf_counter()
    # ts_s = time.perf_counter()
    # iData = merge_sort_classic(iData)
    iData.sort(key=lambda x: x[0])
    # ts_e = time.perf_counter()
    ids = 0
    ide = 0
    # ta_s = time.perf_counter()
    while ids < n:
        tmpe = ide
        while ide < n - 1 and iData[tmpe][1] >= iData[ide + 1][0]:
            ide += 1
            if iData[ide][1] >= iData[tmpe][1]:
                tmpe = ide
        print(iData[ids][0], iData[tmpe][1])
        ids = ide = ide + 1
    # ta_e = time.perf_counter()
    # sys.stdin.close()
    # sys.stdin = oldstdin
    # print('Read time: {0:.3f}'.format(tr_e - tr_s))
    # print('Sort time: {0:.3f}'.format(ts_e - ts_s))
    # print('Process time: {0:.3f}'.format(ta_e - ta_s))
    # tt = (tr_e - tr_s) + (ts_e - ts_s) + (ta_e - ta_s)
    # print('Total time: {0:.3f}'.format(tt))
