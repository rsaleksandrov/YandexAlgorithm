import time
import sys
from collections import deque


def checkStr(s, substr, memo):
    if s == '':
        return True
    if s in memo:
        return memo[s]

    memo[s] = False
    for w in substr:
        wlen = len(w)
        start = s[:wlen]
        end = s[wlen:]
        if start == w and checkStr(end, substr, memo):
            memo[s] = True

    return memo[s]


def checkStr2(s, substr):
    tmps = s
    isCorrect = True
    # delstr = []
    while len(tmps) > 0 and isCorrect:
        tmpCorrect = False
        maxlen = 0
        # tmpdelstr = ''
        for w in substr:
            chstr = tmps[-len(w):]
            if chstr == w:
                if len(w) > maxlen:
                    maxlen = len(w)
                    # tmpdelstr = w
                tmpCorrect = True
        isCorrect = tmpCorrect
        if tmpCorrect:
            tmps = tmps[:-maxlen]
            # delstr.append(tmpdelstr)
        # else:
        #     isCorrect = False
    return isCorrect


def checkStr3(s, substrs):
    eque = deque()
    eque.append([s, 0])
    isCorrect = False
    while len(eque) > 0 and not isCorrect:
        chkstr, seglen = eque.popleft()
        if chkstr == '' and seglen == len(s):
            isCorrect = True
            continue
        for w in substrs:
            lenw = len(w)
            startstr = chkstr[0:lenw]
            endstr = chkstr[lenw:]
            if startstr == w:
                eque.append([endstr, seglen + lenw])
    return isCorrect
    pass


if __name__ == '__main__':
    oldstdin = sys.stdin
    sys.stdin = open('052.txt', 'r')
    tb = time.perf_counter_ns()
    # sys.setrecursionlimit(2000)
    s = input()
    n = int(input())
    words = []
    memo = dict()
    for i in range(n):
        w = input()
        words.append(w)

    # res = checkStr2(s, words)
    # res = checkStr(s, words, memo)
    res = checkStr3(s, words)
    if res:
        print('YES')
    else:
        print('NO')
    te = time.perf_counter_ns()
    sys.stdin.close()
    sys.stdin = oldstdin
    print((te - tb) / 10**9)

