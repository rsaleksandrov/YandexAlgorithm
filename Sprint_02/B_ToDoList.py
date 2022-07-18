"""
Васе нужно распечатать свой список дел на сегодня.
Помогите ему: напишите функцию, которая печатает все его дела.
Известно, что дел у Васи не больше 5000.
Внимание: в этой задаче не нужно считывать входные данные.
Нужно написать только функцию, которая принимает на вход голову списка и
печатает его элементы. Ниже дано описание структуры, которая задаёт узел
списка. Используйте компилятор Make.
Мы рекомендуем воспользоваться заготовками кода для данной задачи,
расположенными по ссылке.
Решение надо отправлять только в виде файла с расширением, которое
соответствует вашему языку. Иначе даже корректно написанное решение не
пройдет тесты.

Формат ввода
В качестве ответа сдайте только код функции, которая печатает элементы
списка. Длина списка не превосходит 5000 элементов. Список не бывает пустым.
Следуйте следующим правилам при отправке решений:

Нужно выбирать компилятор Make.
Решение нужно отправлять в виде файла с расширением соответствующем вашему
языку программирования.
Для Java файл должен называться Solution.java, для C# – Solution.cs
Для остальных языков программирования это имя использовать нельзя
(имя «solution» тоже).
Для Go укажите package main.

Python:
Если вы пишете на Python, функция должна принимать на вход вершину node и
иметь сигнатуру
solution(node) -> None
Узел списка описывается следующим классом:
class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

"""

# Uncomment before local run
# class Node:
#     def __init__(self, value, next_item=None):
#         self.value = value
#         self.next_item = next_item


def solution(node) -> None:
    while not (node is None):
        print(node.value)
        node = node.next_item


if __name__ == "__main__":
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    solution(node0)

