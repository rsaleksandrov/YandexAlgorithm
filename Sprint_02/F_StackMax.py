"""
Нужно реализовать класс StackMax, который поддерживает операцию определения
максимума среди всех элементов в стеке. Класс должен поддерживать операции
push(x), где x – целое число, pop() и get_max().

Формат ввода
В первой строке записано одно число n — количество команд, которое не
превосходит 10000. В следующих n строках идут команды. Команды могут быть
следующих видов:
push(x) — добавить число x в стек;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max() нужно напечатать «None»,
для команды pop() — «error».

Формат вывода
Для каждой команды get_max() напечатайте результат её выполнения.
Если стек пустой, для команды get_max() напечатайте «None».
Если происходит удаление из пустого стека — напечатайте «error».
"""


class StackElem:
    def __init__(self, value=None, maxvalue=None):
        self.value = value
        self.maxvalue = maxvalue


class StackMax:
    def __init__(self):
        self.stack = []
        self.maxvalue = None

    def push(self, x):
        if (self.maxvalue is None) or (x > self.maxvalue):
            self.maxvalue = x
        tmpElem = StackElem(x, self.maxvalue)
        self.stack.append(tmpElem)

    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop(len(self.stack) - 1)
            if len(self.stack) != 0:
                self.maxvalue = self.stack[len(self.stack) - 1].maxvalue
            else:
                self.maxvalue = None
        else:
            print("error")

    def get_max(self):
        if len(self.stack) > 0:
            print(self.maxvalue)
        else:
            print("None")


mStack = StackMax()
n = int(input())
for i in range(n):
    cmds = input().split()
    if cmds[0] == "push":
        mStack.push(int(cmds[1]))
        pass
    elif cmds[0] == "pop":
        mStack.pop()
    elif cmds[0] == "get_max":
        mStack.get_max()
