"""
Вася размышляет, что ему можно не делать из того списка дел, который он
составил. Но, кажется, все пункты очень важные! Вася решает загадать число и
удалить дело, которое идёт под этим номером. Список дел представлен в виде
односвязного списка. Напишите функцию solution, которая принимает на вход
голову списка и номер удаляемого дела и возвращает голову обновлённого списка.
Внимание: в этой задаче не нужно считывать входные данные. Нужно написать
только функцию, которая принимает на вход голову списка и номер удаляемого
элемента и возвращает голову обновлённого списка. Ниже дано описание структуры,
которая задаёт вершину списка.
Мы рекомендуем воспользоваться заготовками кода для данной задачи,
расположенными по ссылке.
Решение надо отправлять только в виде файла с расширением, которое
соответствует вашему языку. Иначе даже корректно написанное решение не
пройдет тесты.

Формат ввода
Функция принимает голову списка и индекс элемента, который надо удалить
(нумерация с нуля). Список содержит не более 5000 элементов.
Список не бывает пустым.
Следуйте следующим правилам при отправке решений:

Нужно выбирать компилятор Make.
Решение нужно отправлять в виде файла с расширением соответствующем вашему
языку программирования.
Для Java файл должен называться Solution.java, для C# – Solution.cs
Для остальных языков программирования это имя использовать нельзя (имя «solution» тоже).
Для Go укажите package main.
Python:
Если вы пишете на Python, функция должна называться solution и принимать на
вход вершину node и номер удаляемого элемента.
Узел списка описывается следующим классом:

class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item
Сигнатура функции: solution(node, idx) -> Node
"""


# Uncomment it before local run
class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node, idx) -> Node:
    if idx == 0:
        return node.next_item
    i = 1
    prevNode = node
    currentNode = node.next_item
    while i < idx:
        prevNode = currentNode
        currentNode = prevNode.next_item
        i += 1
    if currentNode is not None:
        prevNode.next_item = currentNode.next_item
    else:
        prevNode.next_item = None
    return node


def printNodes(node) -> None:
    while node is not None:
        print(node.value)
        node = node.next_item


if __name__ == "__main__":
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    printNodes(node0)
    print("---------------")
    new_head = solution(node0, 3)
    printNodes(new_head)
