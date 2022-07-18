"""
Рита по поручению Тимофея наводит порядок в правильных скобочных
последовательностях (ПСП), состоящих только из круглых скобок ().
Для этого ей надо сгенерировать все ПСП длины 2n в алфавитном порядке —–
алфавит состоит из ( и ) и открывающая скобка идёт раньше закрывающей.

Помогите Рите —– напишите программу, которая по заданному n выведет все ПСП в
нужном порядке.

Рассмотрим второй пример. Надо вывести ПСП из четырёх символов.
Таких всего две:
(())
()()
(()) идёт раньше ()(), так как первый символ у них одинаковый, а на второй
позиции у первой ПСП стоит (, который идёт раньше ).

Формат ввода
На вход функция принимает n — целое число от 0 до 10.

Формат вывода
Функция должна напечатать все возможные скобочные последовательности заданной
длины в алфавитном (лексикографическом) порядке.

Пояснения:
Пусть нам известно число n. Надо вывести все правильные скобочные
последовательности в лексикографическом порядке с n открывающимися скобками:

Для запуска алгоритма необходимо сделать вызов gen(n, 0, 0, "").

ans — строка, в которой мы считаем ответ
counter_open - количество открывающих скобок в данный момент
counter_close - количество закрывающих скобок в данный момент

 function gen(n: int, counter_open: int, counter_close: int, ans: string):
   if counter_open + counter_close == 2 * n
     print(ans)
     return
   if counter_open < n
     gen(n, counter_open + 1, counter_close, ans + '(')
   if counter_open > counter_close
     gen(n, counter_open, counter_close + 1, ans + ')')
Если есть возможность поставить открывающую скобку, то мы ставим её.
Аналогично после этого если есть возможность поставить закрывающую скобку,
то после этого мы ставим и её.
Таким образом строки будут выведены в лексографическом порядке, так как
сначала мы мы пытаемся поставить открывающую скобку. При этом мы перебираем
все возможные варианты последующих скобок для каждого возможного префикса ans,
а следовательно в результате получаем все возможножные правильные скобочные
последовательности
"""


def pps(pBn, pBo, pBc, pResStr):
    if pBo + pBc == 2 * pBn:
        print(pResStr)
    else:
        if pBo < pBn:
            pps(pBn, pBo + 1, pBc, pResStr + '(')
        if pBo > pBc:
            pps(pBn, pBo, pBc + 1, pResStr + ')')


n = int(input())
pps(n, 0, 0, '')
