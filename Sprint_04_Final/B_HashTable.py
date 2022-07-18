"""
Тимофей, как хороший руководитель, хранит информацию о зарплатах своих
сотрудников в базе данных и постоянно её обновляет. Он поручил вам написать
реализацию хеш-таблицы, чтобы хранить в ней базу данных с зарплатами
сотрудников.
Хеш-таблица должна поддерживать следующие операции:
put key value —– добавление пары ключ-значение. Если заданный ключ уже есть в
таблице, то соответствующее ему значение обновляется.
get key –— получение значения по ключу. Если ключа нет в таблице, то вывести
«None». Иначе вывести найденное значение.
delete key –— удаление ключа из таблицы. Если такого ключа нет, то вывести
«None», иначе вывести хранимое по данному ключу значение и удалить ключ.
В таблице хранятся уникальные ключи.
Требования к реализации:
Нельзя использовать имеющиеся в языках программирования реализации хеш-таблиц
(std::unordered_map в С++, dict в Python, HashMap в Java, и т. д.)
Число хранимых в таблице ключей не превосходит 10^5.
Разрешать коллизии следует с помощью метода цепочек или с помощью открытой
адресации.
Все операции должны выполняться за O(1) в среднем.
Поддерживать рехеширование и масштабирование хеш-таблицы не требуется.
Ключи и значения, id сотрудников и их зарплата, —– целые числа. Поддерживать
произвольные хешируемые типы не требуется.
Формат ввода
В первой строке задано общее число запросов к таблице n (1≤ n≤ 10^6).
В следующих n строках записаны запросы, которые бывают трех видов –— get, put,
delete —– как описано в условии.
Все ключи и значения –— целые неотрицательные числа, не превосходящие 10^9.
Формат вывода
На каждый запрос вида get и delete выведите ответ на него в отдельной строке.
"""


# Реализация хэш-таблицы

# Класс, описывающий элемент хеш-таблицы
class myHashTableElement():
    def __init__(self):
        self.value = None  # Уточнить по условию диапозон значений
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
