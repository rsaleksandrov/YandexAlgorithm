"""
Гоша реализовал структуру данных Дек, максимальный размер которого
определяется заданным числом. Методы push_back(x), push_front(x), pop_back(),
pop_front() работали корректно. Но, если в деке было много элементов,
программа работала очень долго. Дело в том, что не все операции выполнялись
за O(1). Помогите Гоше! Напишите эффективную реализацию.

Внимание: при реализации используйте кольцевой буфер.

Формат ввода
В первой строке записано количество команд n — целое число, не превосходящее
100000. Во второй строке записано число m — максимальный размер дека. Он не
превосходит 50000. В следующих n строках записана одна из команд:
push_back(value) – добавить элемент в конец дека. Если в деке уже
находится максимальное число элементов, вывести «error».
push_front(value) – добавить элемент в начало дека. Если в деке уже
находится максимальное число элементов, вывести «error».
pop_front() – вывести первый элемент дека и удалить его. Если дек был пуст,
то вывести «error».
pop_back() – вывести последний элемент дека и удалить его. Если дек был пуст,
то вывести «error».
Value — целое число, по модулю не превосходящее 1000.

Формат вывода
Выведите результат выполнения каждой команды на отдельной строке.
Для успешных запросов push_back(x) и push_front(x) ничего выводить не надо.
"""

"""
Алгоритм добавления элементов в конец дека:
0. указатель tail указывает на ячейку, в которую добавляется элемент.
1. Проверяем, заполнен дек или нет. Если да, выводим "error" и выходим из 
функции. Если нет, идем дальше.
2. Добавляем в ячейку, на которую указывает tail, переданный в качестве 
параметра элемент.
3. Увеличиваем значение tail на 1. Если текущее значение tail превышает 
максимальное количество элементов дека, устанавливаем tail на начало массива 
данных.
4. Увеличиваем на 1 количество элементов дека.
"""
"""
Алгоритм получения элемента с конца дека:
0. tail указывает на ячейку, следующую за последней ячейкой со значением.
1. Проверяем, пустой дек или нет. Если да, то выводим "error" и выходим из 
функции. Если нет, идем дальше.
2. Уменьшаем tail на 1. Если tail меньше 0, то смещаем его на конец массива 
данных.
3. Выводим значение ячейки, на которую указывает tail, и записываем в нее 
значение None.
4. Уменьшаем на 1 количество элементов в деке.
"""
"""
Алгоритм добавления элемента в начало дека:
0. head указывает на ячейку, в которой лежит 1-ое значение дека.
1. Проверяем, заполнен дек или нет. Если да, выводим "error" и выходим из 
функции. Если нет, идем дальше.
2. Уменьшаем head на 1. Если head меньше 0, то смещаем его на конец массива 
данных.
3. Добавляем в ячейку, на которую указывает head, переданный в качестве 
параметра элемент.
4. Увеличиваем на 1 количество элементов дека.
"""
"""
Алгоритм получения элемента из начала дека:
0. head указывает на ячейку, в которой лежит 1-ое значение дека.
1. Проверяем, пустой дек или нет. Если да, то выводим "error" и выходим из 
функции. Если нет, идем дальше.
2. Выводим значение ячейки, на которую указывает head, и записываем в нее 
значение None.
3. Увеличиваем head на 1. Если текущее значение head превышает 
максимальное количество элементов дека, устанавливаем head на начало массива 
данных.
4. Уменьшаем на 1 количество элементов в деке.
"""


class MyDecIsEmpty(Exception):
    pass


class MyDecIsFull(Exception):
    pass


class MyDek:
    def __init__(self, deksize=10):
        self.dek = [None] * deksize
        self.head = 0
        self.tail = 0
        self.maxdeksize = deksize
        self.countelem = 0

    def push_back(self, value):
        if self.countelem == self.maxdeksize:
            raise MyDecIsFull()
        else:
            self.dek[self.tail] = value
            self.tail = (self.tail + 1) % self.maxdeksize
            self.countelem += 1
        pass

    def push_front(self, value):
        if self.countelem == self.maxdeksize:
            raise MyDecIsFull()
        else:
            self.head -= 1
            if self.head < 0:
                self.head += self.maxdeksize
            self.dek[self.head] = value
            self.countelem += 1
        pass

    def pop_front(self):
        if self.countelem == 0:
            raise MyDecIsEmpty()
        else:
            el = self.dek[self.head]
            self.dek[self.head] = None
            self.head = (self.head + 1) % self.maxdeksize
            self.countelem -= 1
            return el
        pass

    def pop_back(self):
        if self.countelem == 0:
            raise MyDecIsEmpty()
        else:
            self.tail -= 1
            if self.tail < 0:
                self.tail += self.maxdeksize
            el = self.dek[self.tail]
            self.dek[self.tail] = None
            self.countelem -= 1
            return el
        pass

    def print_dek(self):
        print()
        print('Head: {:5d}\tTail: {:5d}\tLength: {:5d}'.format(self.head,
                                                               self.tail,
                                                               self.countelem))
        print('---------' * self.maxdeksize)
        for i in range(self.maxdeksize):
            if i == self.head:
                print('|', '-' * 3, 'H', '-' * 3, '|', sep='', end='')
            else:
                print('|', '-' * 7, '|', sep='', end='')
        print()
        for i in range(self.maxdeksize):
            if self.dek[i] is not None:
                print(f'|{self.dek[i]:^7d}|', end='')
            else:
                print('|  None |', end='')
        print()
        for i in range(self.maxdeksize):
            if i == self.tail:
                print('|', '-' * 3, 'T', '-' * 3, '|', sep='', end='')
            else:
                print('|', '-' * 7, '|', sep='', end='')
        print()
        print('---------' * self.maxdeksize)


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    mDek = MyDek(m)
    # mDek.print_dek()
    for i in range(n):
        cmds = input().split()
        try:
            if cmds[0] == 'push_front':
                mDek.push_front(int(cmds[1]))
            elif cmds[0] == 'push_back':
                mDek.push_back(int(cmds[1]))
            elif cmds[0] == 'pop_back':
                print(mDek.pop_back())
            elif cmds[0] == 'pop_front':
                print(mDek.pop_front())
        except MyDecIsEmpty:
            print('error')
        except MyDecIsFull:
            print('error')
    # mDek.print_dek()
