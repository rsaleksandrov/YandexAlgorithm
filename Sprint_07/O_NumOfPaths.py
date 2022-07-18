"""
Вам дан ациклический ориентированный граф. Найдите в нем количество путей от
вершины A до вершины B. Так как потенциально различных путей может быть очень
много, то выведите остаток этого числа по модулю 10^9 + 7.

Формат ввода
В первой строке дано количество вершин в графе n и ребер m
(1 ≤ n ≤ 10^5, 0 ≤ m ≤ 5 ⋅ 10^5). В каждой из следующих m строк описаны ребра.
Каждое ребро задается своим началом и концом. В последней строке даны вершины
A и B (1 ≤ A, B ≤ n).

Формат вывода
Выведите единственное число – количество путей от A до B по модулю 10^9 + 7.
"""


def NumOfPaths(startNode, nodes, visitNodes, dp, mod):
    visitNodes[startNode] = True

    for node in nodes[startNode]:
        if not visitNodes[node]:
            NumOfPaths(node, nodes, visitNodes, dp, mod)
        dp[startNode] += dp[node]
        dp[startNode] %= mod
    pass


n, m = list(map(int, input().split()))
iNodes = [[] for _ in range(n+1)]
for i in range(m):
    u, v = list(map(int, input().split()))
    iNodes[u].append(v)
a, b = list(map(int, input().split()))
dp = [0] * (n + 1)
visit = [False] * (n + 1)
dp[b] = 1
mod = 10 ** 9 + 7
NumOfPaths(a, iNodes, visit, dp, mod)
res = dp[a]
print(res)
