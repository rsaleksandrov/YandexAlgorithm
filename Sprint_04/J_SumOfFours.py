"""
В первой строке дано общее количество элементов массива n (0 ≤ n ≤ 1000).
Во второй строке дано целое число S, |s|<=10^9.

В третьей строке задан сам массив. Каждое число является целым и не
превосходит по модулю 10^9.

Формат вывода
В первой строке выведите количество найденных четвёрок чисел.

В последующих строках выведите найденные четвёрки. Числа внутри одной четверки
должны быть упорядочены по возрастанию. Между собой четвёрки упорядочены
лексикографически.
"""

n = int(input())
s = int(input())
iData = list(map(int, input().split()))

if n >= 4:
    iData.sort()
    sum2 = {}
    for i in range(n - 1):
        for j in range(i + 1, n):
            s2 = iData[i] + iData[j]
            # if s2 >= s:
            #     continue
            if s2 in sum2:
                sum2[s2].append([i, j])
            else:
                sum2[s2] = [[i, j]]

    res = []
    for s2 in sum2:
        x = s - s2
        if x in sum2:
            for l in sum2[s2]:
                for r in sum2[x]:
                    if r[0] > l[1]:
                        t = [iData[l[0]], iData[l[1]], iData[r[0]],
                             iData[r[1]]]
                        if t not in res:
                            res.append(t)
    res.sort()
    print(len(res))
    for el in res:
        print(*el)
    pass
else:
    print('0')
