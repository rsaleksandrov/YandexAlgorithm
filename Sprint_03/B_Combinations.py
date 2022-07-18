"""
На клавиатуре старых мобильных телефонов каждой цифре соответствовало
несколько букв. Примерно так:
2:'abc',
3:'def',
4:'ghi',
5:'jkl',
6:'mno',
7:'pqrs',
8:'tuv',
9:'wxyz'

Вам известно в каком порядке были нажаты кнопки телефона, без учета повторов.
Напечатайте все комбинации букв, которые можно набрать такой
последовательностью нажатий.

Формат ввода
На вход подается строка, состоящая из цифр 2-9 включительно. Длина строки не
превосходит 10 символов.

Формат вывода
Выведите все возможные комбинации букв через пробел.
"""
symbolDict = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def GenSequence(pDigitStr, pCurrentDigit, pResultSequence):
    if pCurrentDigit >= len(pDigitStr):
        print(pResultSequence, end=' ')
    else:
        tmpsd = symbolDict[pDigitStr[pCurrentDigit]]
        for ch in tmpsd:
            GenSequence(pDigitStr, pCurrentDigit + 1, pResultSequence + ch)


if __name__=='__main__':
    s = input()
    GenSequence(s, 0, '')
