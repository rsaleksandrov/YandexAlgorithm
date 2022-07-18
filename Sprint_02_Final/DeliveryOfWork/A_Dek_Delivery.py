"""
ID 66552817

Решение задачи реализовано на основе кольцевого буфера заданного размера.
Кольцевой буфер реализован в виде массива и двух указателей: первый элемент
дека (head) и последний элемент дека (tail).
Алгоритмы работы при добалении и извлечении элемента из дека приведены ниже.

Алгоритм добавления элементов в конец дека:
1. Проверяем, заполнен дек или нет. Если да, выводим "error" и выходим из
функции. Если нет, идем дальше.
2. Добавляем в ячейку, на которую указывает tail, переданный в качестве 
параметра элемент.
3. Увеличиваем значение tail на 1. Если текущее значение tail превышает 
максимальное количество элементов дека, устанавливаем tail на начало массива 
данных.
4. Увеличиваем на 1 количество элементов дека.

Алгоритм получения элемента с конца дека:
1. Проверяем, пустой дек или нет. Если да, то выводим "error" и выходим из
функции. Если нет, идем дальше.
2. Уменьшаем tail на 1. Если tail меньше 0, то смещаем его на конец массива 
данных.
3. Выводим значение ячейки, на которую указывает tail, и записываем в нее 
значение None.
4. Уменьшаем на 1 количество элементов в деке.

Алгоритм добавления элемента в начало дека:
1. Проверяем, заполнен дек или нет. Если да, выводим "error" и выходим из
функции. Если нет, идем дальше.
2. Уменьшаем head на 1. Если head меньше 0, то смещаем его на конец массива 
данных.
3. Добавляем в ячейку, на которую указывает head, переданный в качестве 
параметра элемент.
4. Увеличиваем на 1 количество элементов дека.


Алгоритм получения элемента из начала дека:
1. Проверяем, пустой дек или нет. Если да, то выводим "error" и выходим из
функции. Если нет, идем дальше.
2. Выводим значение ячейки, на которую указывает head, и записываем в нее 
значение None.
3. Увеличиваем head на 1. Если текущее значение head превышает 
максимальное количество элементов дека, устанавливаем head на начало массива 
данных.
4. Уменьшаем на 1 количество элементов в деке.

Оценка вычислительной сложности:
Сложность выполнения операций добавления и извлечения из дека О(1), так как мы
всегда знаем место хранения первого и последнего элемента дека, а добавление и
извлечение происходит или в начало или в конец дека. Поэтому нет необходимости
проходить по всем элементам.
Вычислительную сложность всей программы можно оценить как О(n).
Необходимо выполнить n операций считывая и n операций с деком:
    О(2*n)=>O(n).

Оценка пространственной сложности:
Основную память при выполнении программы будет занимать массив, на базе
которого реализован дек. Его размер задается один раз в начале программы и
не меняется во время ее выполнения.
Поэтому пространственную сложность можно оценить как O(m), где m - максимальный
размер дека.

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
