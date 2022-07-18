"""
Вот какую задачу Тимофей предложил на собеседовании одному из кандидатов.
Если вы с ней ещё не сталкивались, то наверняка столкнётесь –— она
довольно популярная.

Дана скобочная последовательность. Нужно определить, правильная ли она.

Будем придерживаться такого определения:
пустая строка —– правильная скобочная последовательность;
правильная скобочная последовательность, взятая в скобки одного типа, –—
правильная скобочная последовательность;
правильная скобочная последовательность с приписанной слева или справа
правильной скобочной последовательностью —– тоже правильная.
На вход подаётся последовательность из скобок трёх видов: [], (), {}.
Напишите функцию is_correct_bracket_seq, которая принимает на вход скобочную
последовательность и возвращает True, если последовательность правильная,
а иначе False.

Формат ввода
На вход подаётся одна строка, содержащая скобочную последовательность.
Скобки записаны подряд, без пробелов.

Формат вывода
Выведите «True» или «False».
"""


class SimpleStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0


def is_correct_bracket_seq(bs) -> bool:
    if len(bs) == 0:
        return True
    isCorrect = True
    mStack = SimpleStack()
    for ch in bs:
        if ch == '[':
            mStack.push(']')
        elif ch == '(':
            mStack.push(')')
        elif ch == '{':
            mStack.push('}')
        if ch in [']', ')', '}']:
            chst = mStack.pop()
            if (chst is None) or (chst != ch):
                isCorrect = False
                break
    if not mStack.isEmpty():
        isCorrect = False
    return isCorrect


s = input()
if is_correct_bracket_seq(s):
    print('True')
else:
    print('False')
