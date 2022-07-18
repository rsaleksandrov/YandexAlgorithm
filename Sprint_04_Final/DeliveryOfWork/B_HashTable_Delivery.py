"""
ID 67681508

Основа алгоритма - класс, реализующий хэш таблицу.
Коллизии разрешаются методом цепочек. Цепочки реализуются на основе
двусвязанного списка (пока писал описание так и не понял зачем делал
двусвязанный список. Можно было обойтись односвязанным)
При добавлении элемента в хэш расчитывается его ключ. Если такой ключ
уже существует, то проверяется наличие элемента в цепочке. Если он найден,
то обновляется его значение. Если не найден, элемент добавляется в
начало цепочки. Если ключа нет, то элемент становится первым в цепочке.
В самой хеш таблице хранятся ссылки на начало цепочек.

Вычислительная сложность:
Если не учитывать заданные в задаче ограничения, то сложность можно оценить как
O(n), где n - максимальное количество элементов в цепочке (время тратится на
поиск элементов при возникновении коллизий)
С учетом ограничений задачи сложность в среднем можно считать как O(1), т.к.
максимальное количесво элементов в цепочке коллизий не превышает 10 элементов,
что много меньше количества ключей.

Пространственная сложность:
В общем худшем случае  - O(k*n), k - размер хэш таблицы, n - максимальное
количество элементов в цепочке.
В условиях задачи - O(k), т.к. размер хэш таблицы много больше длины цепочек.
"""


# Реализация хэш-таблицы

# Класс, описывающий элемент хеш-таблицы
class myHashTableElement():
    def __init__(self):
        self.value = None
        self.key = None
        self.next = None
        self.prev = None
        pass


# Основной класс хеш-таблицы
class myHashTable():
    __hashtablesize__ = 0
    __hashtable__ = []

    def __init__(self, size=1000):
        self.__hashtablesize__ = size
        self.__hashtable__ = [None] * size
        pass

    def __gethashid__(self, key):
        return key % self.__hashtablesize__

    def __findelem__(self, key):
        hashID = self.__gethashid__(key)
        elemPoint = self.__hashtable__[hashID]
        while elemPoint is not None:
            if elemPoint.key == key:
                return elemPoint
            elemPoint = elemPoint.next
        return None

    def put(self, key, value):
        fElem = self.__findelem__(key)
        if fElem is None:
            hashID = self.__gethashid__(key)
            newValue = myHashTableElement()
            newValue.value = value
            newValue.key = key
            newValue.next = self.__hashtable__[hashID]
            if self.__hashtable__[hashID] is not None:
                self.__hashtable__[hashID].prev = newValue
            self.__hashtable__[hashID] = newValue
        else:
            fElem.value = value

    def get(self, key):
        fElem = self.__findelem__(key)
        if fElem is not None:
            return fElem.value
        else:
            return None

    def delete(self, key):
        fElem = self.__findelem__(key)
        if fElem is not None:
            tmpValue = fElem.value
            if fElem.prev is not None:
                fElem.prev.next = fElem.next
                if fElem.next is not None:
                    fElem.next.prev = fElem.prev
            else:
                hashID = self.__gethashid__(key)
                self.__hashtable__[hashID] = fElem.next
                if self.__hashtable__[hashID] is not None:
                    self.__hashtable__[hashID].prev = None
            return tmpValue
        else:
            return None

    def printelements(self, key):
        hashID = self.__gethashid__(key)
        elemPoint = self.__hashtable__[hashID]
        while elemPoint is not None:
            print(elemPoint.value, '->', sep='', end='')
            elemPoint = elemPoint.next
        print('None')

    def printall(self):
        for i in range(self.__hashtablesize__):
            if self.__hashtable__[i] is not None:
                print(f'[{i}]->', end='')
                self.printelements(i)


def test():
    ht = myHashTable()
    ht.put(10, 1)
    ht.put(10, 2)
    ht.put(10, 3)
    ht.put(1011, 101)
    ht.put(1010, 102)
    ht.put(10011, 103)
    ht.printall()

    val = ht.get(1011)
    if val is not None:
        print(val)
    else:
        print('-1')

    if ht.delete(10) is not None:
        print('ok')
    else:
        print('error')

    ht.printall()

    if ht.delete(10011) is not None:
        print('ok')
    else:
        print('error')

    ht.printall()

    if ht.delete(1010) is not None:
        print('ok')
    else:
        print('error')

    ht.printall()


def main():
    ht = myHashTable(100000)
    n = int(input())
    for i in range(n):
        cmd = input().split()
        if cmd[0] == 'put':
            ht.put(int(cmd[1]), int(cmd[2]))
            pass
        elif cmd[0] == 'get':
            val = ht.get(int(cmd[1]))
            print(val if val is not None else 'None')
            pass
        elif cmd[0] == 'delete':
            val = ht.delete(int(cmd[1]))
            print(val if val is not None else 'None')
            pass


if __name__ == '__main__':
    # test()
    main()
