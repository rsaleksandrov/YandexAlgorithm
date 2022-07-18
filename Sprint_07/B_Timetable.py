"""
Дано количество учебных занятий, проходящих в одной аудитории.
Для каждого из них указано время начала и конца. Нужно составить расписание,
в соответствии с которым в классе можно будет провести как можно больше
занятий. Если возможно несколько оптимальных вариантов, то выведите любой.
Возможно одновременное проведение более чем одного занятия нулевой
длительности.

Формат ввода
В первой строке задано число занятий. Оно не превосходит 1000.
Далее для каждого занятия в отдельной строке записано время начала и конца,
разделённые пробелом. Время задаётся одним целым числом h, если урок
начинается/заканчивается ровно в h часов. Если же урок начинается/
заканчивается в h часов m минут, то время записывается как h.m.
Гарантируется, что каждое занятие начинается не позже, чем заканчивается.
Указываются только значащие цифры.

Формат вывода
Выведите в первой строке наибольшее число уроков, которое можно провести в
аудитории. Далее выведите время начала и конца каждого урока в отдельной
строке в порядке их проведения.
"""

n = int(input())
iData = []
for i in range(n):
    tb, te = list(map(float, input().split()))
    iData.append([te, tb])

iData.sort()
taskend = -1.0
res = []

for el in iData:
    if el[1] >= taskend:
        taskend = el[0]
        res.append(el)

print(len(res))
for el in res:
    print(el[1], el[0])