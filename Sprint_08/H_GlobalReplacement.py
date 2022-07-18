"""
Напишите программу, которая будет заменять в тексте все вхождения строки s на
строку t. Гарантируется, что никакие два вхождения шаблона s не пересекаются
друг с другом.

Формат ввода
В первой строке дан текст —– это строка из строчных букв английского алфавита,
длина которой не превышает 10^6.
Во второй строке записан шаблон s, вхождения которого будут заменены.
В третьей строке дана строка t, которая будет заменять вхождения.
Обе строки s и t состоят из строчных букв английского алфавита, длина каждой
строки не превосходит 10^5. Размер итоговой строки не превосходит 2⋅ 10^6.

Формат вывода
В единственной строке выведите результат всех замен — текст, в котором все
вхождения s заменены на t.
"""


def search(pattern, text):
    res = []
    h = [0] * len(pattern)
    s = pattern + '#' + text
    h_prev = 0
    for i in range(1, len(s)):
        k = h_prev
        while k > 0 and s[k] != s[i]:
            k = h[k - 1]
        if s[k] == s[i]:
            k += 1
        if i < len(pattern):
            h[i] = k
        h_prev = k
        if k == len(pattern):
            res.append(i - 2 * len(pattern))
    return res


s = input()
pattern = input()
t = input()
idp = search(pattern, s)
res = []
startp = 0
for id in idp:
    res.append(s[startp:id])
    res.append(t)
    startp = id + len(pattern)
if startp < len(s):
    res.append(s[startp:len(s)])
print(''.join(res))
