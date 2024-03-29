"""
На Алгосах устроили турнир по настольному теннису. Гоша выиграл n партий,
получив при этом некоторое количество очков за каждую из них.

Гоше стало интересно, можно ли разбить все заработанные им во время турнира
очки на две части так, чтобы сумма в них была одинаковой.

Формат ввода
В первой строке записано целое число n (0 ≤ n ≤ 300) –— количество выигранных
партий.
Во второй строке через пробел записано n целых неотрицательных чисел, каждое
из которых не превосходит 300 –— заработанные в партиях очки.

Формат вывода
Нужно вывести True, если произвести такое разбиение возможно, иначе —– False
"""


def main():
    n = int(input())
    iData = list(map(int, input().split()))
    datasum = sum(iData)
    if datasum % 2 != 0:
        print(False)
    else:
        datahalfsum = datasum // 2
        dp = [True] + [False] * datahalfsum
        for num in iData:
            for j in range(datahalfsum, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
                if j == datahalfsum and dp[j]:
                    print(True)
                    return

        print(dp[-1])


if __name__ == '__main__':
    main()
