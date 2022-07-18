"""
Расстоянием Левенштейна между двумя строками s и t называется количество
атомарных изменений, с помощью которых можно одну строку превратить в другую.
Под атомарными изменениями подразумеваются: удаление одного символа, вставка
одного символа, замена одного символа на другой.

Найдите расстояние Левенштейна для предложенной пары строк.
https://ru.wikipedia.org/wiki/Расстояние_Левенштейна

Выведите единственное число — расстояние между строками.

Формат ввода
В первой строке дана строка s, во второй — строка t. Длины обеих строк не
превосходят 1000. Строки состоят из маленьких латинских букв.
"""


def main2():
    s1 = input()
    s2 = input()
    rows = len(s2) + 1
    cols = len(s1) + 1
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    for j in range(cols):
        dp[0][j] = j
    for i in range(1, rows):
        dp[i][0] = i
        for j in range(1, cols):
            d1 = dp[i - 1][j] + 1
            d2 = dp[i][j - 1] + 1
            d3 = dp[i - 1][j - 1] + (0 if s1[j - 1] == s2[i - 1] else 1)
            dp[i][j] = min([d1, d2, d3])

    print(dp[rows - 1][cols - 1])


def main3():
    s1 = input()
    s2 = input()
    rows = len(s2) + 1
    cols = len(s1) + 1
    cur = []
    # prev = []
    for i in range(1, rows):
        if i == 1:
            prev = [j for j in range(cols)]
        else:
            prev = cur
        cur = [i] + [0] * (cols - 1)
        for j in range(1, cols):
            d1 = prev[j] + 1
            d2 = cur[j - 1] + 1
            d3 = prev[j - 1] + (0 if s1[j - 1] == s2[i - 1] else 1)
            cur[j] = min([d1, d2, d3])

    print(cur[-1])


if __name__ == '__main__':
    main3()
