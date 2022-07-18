"""
Вам даны строки в запакованном виде. Определим запакованную строку (ЗС)
рекурсивно. Строка, состоящая только из строчных букв английского алфавита
является ЗС. Если A и B —– корректные ЗС, то и AB является ЗС. Если A —– ЗС,
а n — однозначное натуральное число, то n[A] тоже ЗС. При этом запись n[A]
означает, что при распаковке строка A записывается подряд n раз. Найдите
наибольший общий префикс распакованных строк и выведите его (в распакованном
виде). Иными словами, пусть сложение —– это конкатенация двух строк, а
умножение строки на число — повтор строки соответствующее число раз.
Пусть функция f умеет принимать ЗС и распаковывать её. Если ЗС D имеет вид
D=AB, где A и B тоже ЗС, то f(D) = f(A) + f(B). Если D=n[A],
то f(D) = f(A) × n.

Формат ввода
В первой строке записано число n (1 ≤ n ≤ 1000) –— число строк.
Далее в n строках записаны запакованные строки.
Гарантируется, что эти строки корректны, то есть удовлетворяют указанному
рекурсивному определению. Длина строк после распаковки не превосходит 10^5.

Формат вывода
Выведите наибольший общий префикс распакованных строк.
"""
import sys
import random
import time


def unpackStr(s):
    prevpos = 0
    curpos = 0
    stack = []
    for ch in s:
        if ch.isalpha():
            curpos += 1
        elif ch.isdigit():
            stack.append(s[prevpos:curpos])
            stack.append(int(ch))
            curpos += 1
            prevpos = curpos
        elif ch == '[':
            stack.append(ch)
            curpos += 1
            prevpos = curpos
        elif ch == ']':
            if curpos != prevpos:
                stack.append(s[prevpos:curpos])
            ts = []
            tmpstr = stack.pop()
            while tmpstr != '[':
                ts.append(tmpstr)
                tmpstr = stack.pop()
            ts.reverse()
            num = stack.pop()
            stack.append(''.join(ts) * num)
            curpos += 1
            prevpos = curpos
    if curpos != prevpos:
        stack.append(s[prevpos:len(s)])
    res = ''.join(stack)
    return res


def main():
    n = int(input())
    maxPrefixLen = -1
    basestr = ''
    for i in range(n):
        ps = input()
        ups = unpackStr(ps)

        if maxPrefixLen == -1:
            maxPrefixLen = len(ups)
            basestr = ups
        else:
            if len(ups) < maxPrefixLen:
                maxPrefixLen = len(ups)
            for i in range(maxPrefixLen):
                if ups[i] != basestr[i]:
                    maxPrefixLen = i
                    break
            if maxPrefixLen == 0:
                break

    print(basestr[:maxPrefixLen])


def test():
    elcount = 1000
    alf = [chr(i) for i in range(97, 123)]
    f = open('pp.txt', 'w')
    f.write(str(elcount) + '\n')
    for i in range(elcount):
        f.write(('a' * 999) + random.choice(alf) + '\n')
    f.close()


if __name__ == '__main__':
    # test()
    # oldin = sys.stdin
    # sys.stdin = open('pp.txt', 'r')
    # tb = time.perf_counter_ns()
    main()
    # te = time.perf_counter_ns()
    # sys.stdin.close()
    # sys.stdin = oldin
    # print(f'Time: {((te-tb)/10**9)}')
