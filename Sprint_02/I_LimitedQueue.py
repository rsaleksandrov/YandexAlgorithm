"""
Астрологи объявили день очередей ограниченного размера.
Тимофею нужно написать класс MyQueueSized, который принимает
параметр max_size, означающий максимально допустимое количество
элементов в очереди.

Помогите ему —– реализуйте программу, которая будет эмулировать работу такой
очереди. Функции, которые надо поддержать, описаны в формате ввода.

Формат ввода
В первой строке записано одно число — количество команд, оно не
превосходит 5000.
Во второй строке задан максимально допустимый размер очереди, он не
превосходит 5000.
Далее идут команды по одной на строке. Команды могут быть следующих видов:
push(x) — добавить число x в очередь;
pop() — удалить число из очереди и вывести на печать;
peek() — напечатать первое число в очереди;
size() — вернуть размер очереди;
При превышении допустимого размера очереди нужно вывести «error».
При вызове операций pop() или peek() для пустой очереди нужно вывести «None».
Формат вывода
Напечатайте результаты выполнения нужных команд, по одному на строке.
"""


class MyQueueSized:
    def __init__(self, querysize=1):
        self.query = [None] * querysize
        self.head = 0
        self.tail = 0
        self.maxquerysize = querysize
        self.sizequery = 0

    def push(self, x):
        if self.sizequery == self.maxquerysize:
            print("error")
        else:
            self.query[self.tail] = x
            self.tail = (self.tail + 1) % self.maxquerysize
            self.sizequery += 1

    def pop(self):
        if self.sizequery == 0:
            print("None")
        else:
            print(self.query[self.head])
            self.query[self.head] = None
            self.head = (self.head + 1) % self.maxquerysize
            self.sizequery -= 1

    def peek(self):
        if self.sizequery == 0:
            print("None")
        else:
            print(self.query[self.head])

    def size(self):
        return self.sizequery


n = int(input())
qs = int(input())
mQuery = MyQueueSized(qs)
for i in range(n):
    cmds = input().split()
    if cmds[0] == "push":
        mQuery.push(int(cmds[1]))
    elif cmds[0] == "pop":
        mQuery.pop()
    elif cmds[0] == "peek":
        mQuery.peek()
    elif cmds[0] == "size":
        print(mQuery.size())
