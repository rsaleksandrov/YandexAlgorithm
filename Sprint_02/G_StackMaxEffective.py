"""
Реализуйте класс StackMaxEffective, поддерживающий операцию определения
максимума среди элементов в стеке. Сложность операции должна быть O(1).
Для пустого стека операция должна возвращать None. При этом push(x) и pop()
также должны выполняться за константное время.

Формат ввода
В первой строке записано одно число — количество команд, оно не
превосходит 100000. Далее идут команды по одной в строке.
Команды могут быть следующих видов:
push(x) — добавить число x в стек;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max нужно напечатать «None»,
для команды pop — «error».

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
