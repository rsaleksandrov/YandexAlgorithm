import time
import sys


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = {} if next is None else next
        self.terminal = False


def create_tree(words):
    root = Node('')
    for word in words:
        node = root
        for index, char in enumerate(word):
            node.next[char] = node.next.get(char, Node(char))
            node = node.next[char]
        node.terminal = len(word)
    return root


def is_split_words(string, words):
    root = create_tree(words)
    dp = [True] + [False] * len(string)
    for i in range(len(string)):
        node = root
        if dp[i]:
            for j in range(i, len(string) + 1):
                if node.terminal:
                    dp[j] = True
                if j == len(string) or not node.next.get(string[j], False):
                    break
            node = node.next[string[j]]
    return dp[-1]


if __name__ == '__main__':
    oldstdin = sys.stdin
    sys.stdin = open('019.txt', 'r')
    tb = time.perf_counter_ns()
    # sys.setrecursionlimit(2000)
    s = input()
    n = int(input())
    words = []
    # memo = dict()
    for i in range(n):
        w = input()
        words.append(w)

    res = is_split_words(s, words)
    if res:
        print('YES')
    else:
        print('NO')
    te = time.perf_counter_ns()
    sys.stdin.close()
    sys.stdin = oldstdin
    print((te - tb) / 10**9)

