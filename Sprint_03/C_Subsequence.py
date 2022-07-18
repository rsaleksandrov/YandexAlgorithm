"""
Гоша любит играть в игру «Подпоследовательность»: даны 2 строки, и нужно
понять, является ли первая из них подпоследовательностью второй. Когда строки д
остаточно длинные, очень трудно получить ответ на этот вопрос, просто
посмотрев на них. Помогите Гоше написать функцию, которая решает эту задачу.

Формат ввода
В первой строке записана строка s.
Во второй —- строка t.

Обе строки состоят из маленьких латинских букв, длины строк не
превосходят 150000. Строки могут быть пустыми.

Формат вывода
Выведите True, если s является подпоследовательностью t, иначе —– False.


"""


def isSubsequence_v1(s1, s2) -> bool:
    """
    Проверяем, является ли строка s1 подстрокой s2
    :return: True - является, False - нет
    """
    i = 0
    findpos = 0
    if s1 == '' and s2 == '':
        return True
    elif s1 == '' and s2 != '':
        return True
    elif s1 != '' and s2 == '':
        return False
    else:
        while i < len(s1):
            findpos = s2.find(s1[i], findpos)
            if findpos == -1:
                return False
            i += 1
            findpos += 1
        if findpos != -1:
            return True


def isSubsequence_v2(s1, s2) -> bool:
    """
    Проверяем, является ли строка s1 подстрокой s2
    :return: True - является, False - нет
    """
    i = j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            j += 1
    return i == len(s1)


s1 = input()
s2 = input()
# if isSubsequence_v1(s1, s2):
#     print('True')
# else:
#     print('False')

if isSubsequence_v2(s1, s2):
    print('True')
else:
    print('False')
