"""
ID 69277869

Алгоритм:
1. Из слов формируем префиксное дерево из строк словаря
2. В основу анализа строку положена "задача о рюкзаке":
   2.1 Заводим вспомогательный массив dp размером равным длине анализируемой
       строки + 1, в котором на позиции i хранится True, если до этой позиции
       строку можно составить из строк словаря, False - в противном случае.
       Нулевой элемент устанавливаем в True, т.к. пустую строку можно создать
       всегда.
   2.2 Идем по исходной строке. Если префикс строки до текущей позиции можно
       составить из слов словаря (dp[i] = True), то проводим сопоставление со
       словами из словаря с заполнением массива dp.
3. Возможность получения строки из слов словаря будет находиться в последнем
   элементе массива dp

Вычислительная сложность:
1. Формирование префиксного дерева - O(L), L - суммарная длина слов в словаре
2. Анализ строки - O(n*L), n - длина строки
3. Общая сложность - O(L+n*L)

Пространственная сложность:
1. Хранение префиксного дерева - O(L)
2. Вспомогательный массив dp - O(n)
3. Анализируемая строка - O(n)
4. Общая сложность - O(2n+L)

"""


class PrefixTreeNode:
    def __init__(self):
        self.edges = dict()
        self.isTerminate = False


class PrefixTree:
    def __init__(self):
        self.head = PrefixTreeNode()

    def addWord(self, word):
        if len(word) == 0:
            return

        curNode = self.head
        for i in range(len(word)):
            if word[i] not in curNode.edges:
                curNode.edges[word[i]] = PrefixTreeNode()
            curNode = curNode.edges[word[i]]
        curNode.isTerminate = True

    def checkString(self, value):
        if len(value) == 0:
            return False
        pos = 0
        dp = [True] + [False] * len(value)
        while pos < len(value):
            if not dp[pos]:
                pos += 1
                continue
            curNode = self.head
            offset = 0
            mismathNotFound = True
            while mismathNotFound and ((pos + offset) < len(value)):
                ch = value[pos + offset]
                if ch in curNode.edges:
                    curNode = curNode.edges[ch]
                    if curNode.isTerminate:
                        dp[pos + offset + 1] = True
                    offset += 1
                else:
                    mismathNotFound = False
            pos += 1

        return dp[-1]
        pass


def main():
    s = input()
    n = int(input())
    pt = PrefixTree()
    for i in range(n):
        w = input()
        pt.addWord(w)
    res = pt.checkString(s)
    if res:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
