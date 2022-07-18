"""
ID 68943662
Алгоритм работы:
1. Из исходных данных строим ОРИЕНТИРОВАННЫЙ граф: ребра 'R' идут от меньшей
   вершины к большей, ребра 'B' - от большей к меньшей.
2. С помощью алгоритма поиска в глубину определяем, есть ли в графе циклы.
   Если есть, то это значит, что из одного города в другой можно добраться
   путями разного цвета и карта не оптимальна. Если циклов нет, то карта
   оптимальна.
Примечание:
Сначала был реализован алгоритм нахождения возможных путей и сравнение их
цвета (ID 68908402). Но он упёрся в TL. Попытки оптимизации в виде хранения
всех промежуточных путей в хеш-таблице с последующей проверкой на наличие
уже построенного пути сделали его еще более громоздким и совершенно
нечитаемым (в тестовую систему не отправлялся, т.к. валился на доступных
тестах).
Приведенное алгоритм был реализован после штудирования форума.

Вычислительная сложность:
Вычислительная сложность формирования графа - O(n(n-1)/2)
Вычислительная сложность функции DFS - O(n(n-1)/2), т.к. количество ребер
больше количества вершин.
Общая вычислительная сложность - O(n(n-1)) или O(n^2)

Пространственная сложность:
Память для хранения графа - O(n+n(n-1)/2)
Вспомогательный массив для хранения цвета вершины - O(n)
В функции DFS - память для стека - O(n)
Общая оценка - O(n+n+n+n(n-1)/2) => O(n+n(n-1)/2))

ЗЫ: Наличие длинного комментария увеличивает время выполнения и не
попадает в лимит времени :( (ID 68915088)
"""


def DFS(startv, nodes, colors):
    stack = []
    stack.append(startv)
    res = True
    while len(stack) > 0 and res:
        v = stack.pop()
        if colors[v] == 0:
            if nodes[v] is not None:
                colors[v] = 1
                stack.append(v)
                for i in range(len(nodes[v])):
                    if colors[nodes[v][i]] == 0:
                        stack.append(nodes[v][i])
                    elif colors[nodes[v][i]] == 1:
                        res = False
            else:
                colors[v] = 2
        else:
            if colors[v] == 1:
                colors[v] = 2
    return res
    pass


def main():
    n = int(input())
    vertex = [None] * (n + 1)
    colors = [0] * (n + 1)
    for i in range(n - 1):
        s = input()
        startv = i + 1
        for j in range(len(s)):
            endv = startv + j + 1
            if s[j] == 'R' or s[j] == 'r':
                if vertex[startv] is None:
                    vertex[startv] = []
                vertex[startv].append(endv)
            if s[j] == 'B' or s[j] == 'b':
                if vertex[endv] is None:
                    vertex[endv] = []
                vertex[endv].append(startv)

    for i in range(1, n + 1):
        if colors[i] == 0:
            if not DFS(i, vertex, colors):
                print('NO')
                break
    else:
        print('YES')
    pass


if __name__ == '__main__':
    main()
