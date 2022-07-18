"""
Вася готовится к экзамену по алгоритмам и на всякий случай пишет шпаргалки.
Чтобы уместить на них как можно больше информации, он не разделяет слова
пробелами. В итоге получается одна очень длинная строка. Чтобы на самом
экзамене из-за нервов не запутаться в прочитанном, он просит вас написать
программу, которая по этой длинной строке и набору допустимых слов определит,
можно ли разбить текст на отдельные слова из набора.
Более формально: дан текст T и набор строк s1, ... ,sn. Надо определить,
представим ли T как sk1sk2...skr, где где ki — индексы строк. Индексы могут
повторяться. Строка si может встречаться в разбиении текста T произвольное
число раз. Можно использовать не все строки для разбиения. Строки могут идти
в любом порядке.

Формат ввода
В первой строке дан текст T, который надо разбить на слова. Длина T не
превосходит 10^5. Текст состоит из строчных букв английского алфавита.
Во второй строке записано число допустимых к использованию слов 1 ≤ n ≤ 100.
В последующих n строках даны сами слова, состоящие из маленьких латинских букв.
Длина каждого слова не превосходит 100.

Формат вывода Выведите «YES», если текст можно разбить на слова из данного
словаря, или «NO» в ином случае.
"""

# import sys
# import time


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

    # def __createWord(self, node, word):
    #     if node.isTerminate:
    #         print(word)
    #     for key in node.edges.keys():
    #         self.__createWord(node.edges[key], word + key)
    #     pass
    #
    # def printWords(self):
    #     self.__createWord(self.head, '')
    #     pass

    def __binSearch(self, value, data, leftbound, rightbound):
        if leftbound >= rightbound:
            return -1

        mid = (leftbound + rightbound) // 2
        if data[mid][1] == value:
            return mid
        elif data[mid][1] > value:
            return self.__binSearch(value, data, leftbound, mid)
        else:
            return self.__binSearch(value, data, mid + 1, rightbound)
        pass

    def checkString(self, value):
        if len(value) == 0:
            return False
        pos = 0
        lines = []
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
                        lines.append([pos, pos + offset])
                        dp[pos + offset + 1] = True
                    offset += 1
                else:
                    mismathNotFound = False
            pos += 1

        # lines.sort(key=lambda x: x[1])
        # curpos = lines[-1]
        # # isCorrect = True
        # isCorrect = curpos[1] == (len(value) - 1)
        #
        # while curpos[0] != 0 and isCorrect:
        #     nextId = self.__binSearch(curpos[0] - 1, lines, 0, len(lines))
        #     if nextId == -1:
        #         isCorrect = False
        #     else:
        #         curpos = lines[nextId]

        # if isCorrect:
        #     print('YES')
        # else:
        #     print('NO')

        return dp[-1]
        pass

    def checkString2(self, value):
        dp = [True] + [False] * len(value)
        for i in range(len(value)):
            curnode = self.head
            if dp[i]:  # Подстроку длиной i составить можно
                for j in range(i, len(value)):
                    if curnode.isTerminate:
                        dp[j] = True
                    isNextNodeExist = value[j] in curnode.edges
                    if j == len(value) or not isNextNodeExist:
                        break
                    curnode = curnode.edges[value[j]]
        return dp[-1]


# def test():
#     pt = PrefixTree()
#     while True:
#         word = input()
#         if word.lower() == 'exit':
#             break
#         pt.addWord(word)
#     print('------------------')
#     pt.printWords()
#     pass


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
    # oldstdin = sys.stdin
    # sys.stdin = open('052.txt', 'r')
    # tb = time.perf_counter_ns()
    main()
    # te = time.perf_counter_ns()
    # sys.stdin.close()
    # sys.stdin = oldstdin
    # print((te - tb) / 10 ** 9)
