"""
У Риты была строка s, Гоша подарил ей на 8 марта ещё n других строк
ti, 1≤ i≤ n. Теперь Рита думает, куда их лучше поставить.
Один из вариантов —– расположить подаренные строки внутри имеющейся строки s,
поставив строку ti сразу после символа строки s с номером ki (в частности,
если ki=0, то строка вставляется в самое начало s).

Помогите Рите и определите, какая строка получится после вставки в s всех
подаренных Гошей строк.

Формат ввода
В первой строке дана строка s. Строка состоит из строчных букв английского
алфавита, не бывает пустой и её длина не превышает 10^5 символов.

Во второй строке записано количество подаренных строк — натуральное
число n, 1 ≤ n ≤ 10^5.

В каждой из следующих n строк через пробел записаны пары ti и ki.
Строка ti состоит из маленьких латинских букв и не бывает пустой.
ki — целое число, лежащее в диапазоне от 0 до |s|. Все числа ki уникальны.
Гарантируется, что суммарная длина всех строк ti не превосходит 10^5.

Формат вывода
Выведите получившуюся в результате вставок строку.
"""
bases = input()
n = int(input())
insStrs = []
for i in range(n):
    tmps, tmpk = input().split()
    insStrs.append([int(tmpk), tmps])
insStrs.sort()
# res = ''
stpos = 0
res1 = []
for el in insStrs:
    # tmps = bases[stpos:el[0]]
    # res = res + tmps + el[1]
    res1.append(bases[stpos:el[0]])
    res1.append(el[1])
    stpos = el[0]

if stpos != len(bases):
    # res = res + bases[stpos:len(bases)]
    res1.append(bases[stpos:len(bases)])
# print(res)
print(''.join(res1))
