"""
Вася решил запутать маму —– делать дела в обратном порядке.
Список его дел теперь хранится в двусвязном списке. Напишите функцию,
которая вернёт список в обратном порядке.
Внимание: в этой задаче не нужно считывать входные данные. Нужно написать
только функцию, которая принимает на вход голову двусвязного списка и
возвращает голову перевёрнутого списка. Ниже дано описание структуры,
которая задаёт вершину списка.
Мы рекомендуем воспользоваться заготовками кода для данной задачи,
расположенными по ссылке.
Решение надо отправлять только в виде файла с расширением, которое
соответствует вашему языку. Иначе даже корректно написанное решение
не пройдёт тесты.

Формат ввода
Функция принимает на вход единственный аргумент — голову двусвязного списка.
Длина списка не превосходит 1000 элементов. Список не бывает пустым.
Следуйте следующим правилам при отправке решений:

Нужно выбирать компилятор Make.
Решение нужно отправлять в виде файла с расширением соответствующем вашему
языку программирования.
Для Java файл должен называться Solution.java, для C# – Solution.cs
Для остальных языков программирования это имя использовать нельзя
(имя «solution» тоже).
Для Go укажите package main.
Python:
Если вы пишете на Python, функция должна называться solution и принимать
на вход вершину node.
Узел списка описывается следующим классом:

class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
Сигнатура функции:
solution(node: DoubleConnectedNode) -> DoubleConnectedNode
"""


# Comment it before submitting
class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def solution(node: DoubleConnectedNode) -> DoubleConnectedNode:
    newHead = None
    while node is not None:
        node.next, node.prev = node.prev, node.next
        newHead = node
        node = node.prev
    return newHead


def printNodes(node: DoubleConnectedNode) -> None:
    while node is not None:
        print(node.value, end=" -> ")
        node = node.next
    print("None")


if __name__ == "__main__":
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1

    node1.prev = node0
    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2

    printNodes(node0)

    newHead = solution(node0)
    printNodes(newHead)
