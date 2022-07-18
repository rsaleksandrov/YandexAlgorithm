"""
Любимый вариант очереди Тимофея — очередь, написанная с использованием
связного списка. Помогите ему с реализацией. Очередь должна поддерживать
выполнение трёх команд:
get() — вывести элемент, находящийся в голове очереди, и удалить его.
Если очередь пуста, то вывести «error».
put(x) — добавить число x в очередь
size() — вывести текущий размер очереди

Формат ввода
В первой строке записано количество команд n — целое число, не превосходящее
1000. В каждой из следующих n строк записаны команды по одной строке.

Формат вывода
Выведите ответ на каждый запрос по одному в строке.
"""


class QueueNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class ListQueue:
    def __init__(self):
        self.head: QueueNode = None
        self.tail: QueueNode = None
        self.queuesize = 0

    def get(self):
        if self.queuesize == 0:
            print("error")
        else:
            print(self.head.value)
            self.head = self.head.next
            self.queuesize -= 1
            if self.queuesize == 0:
                self.head = None
                self.tail = None

    def put(self, value):
        tmpNode = QueueNode(value)
        if self.queuesize == 0:
            self.head = tmpNode
            self.tail = tmpNode
        else:
            self.tail.next = tmpNode
            self.tail = tmpNode
        self.queuesize += 1

    def size(self):
        print(self.queuesize)


n = int(input())
mQueue = ListQueue()
for i in range(n):
    cmds = input().split()
    if cmds[0] == 'get':
        mQueue.get()
    elif cmds[0] == 'size':
        mQueue.size()
    elif cmds[0] == 'put':
        mQueue.put(int(cmds[1]))
