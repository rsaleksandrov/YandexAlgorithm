"""
ID 69290114

Алгоритм (общий):
1. Читаем запакованную строку
2. Распаковываем ее (см далее)
3. Если это первая строка (maxPrefixLen = -1), то запоминаем ее (basestr) и
   считаем максимальным префиксом.
4. Если нет, то сравниваем первые maxPrefixLen символов. При необходимости
   корректируем maxPrefixLen
5. Выводим первые maxPrefixLen символов строки basestr

Алгоритм распаковки:
В основе алгоритма лежит перевод инфиксной формы выражения в польскую запись с
одновременным вычислением.
1. Инициализируем тип собираемой части выражения как "не понятно что"
2. Посимвольно проходим запакованную строку
3. Если текущий символ - буква, идем дальше
4. Если текущий символ - цифра:
   4.1 Добавляем в стек часть строки до цифры
   4.2 Добавляем в стек цифру
5. Если текущий символ - "[", добавляем его в стек, идем дальше
6. Если текущий символ - "]":
   6.1 Добавляем в стек часть строки до "]", если она есть
   6.2 Вытаскиваем из стека строки до тех пор, пока не встретим "["
   6.3 Объединяем их в одну строку
   6.4 Вытаскиваем из стека число
   6.5 Умножаем строку из 6.3 на число из 6.4 и кладем результат в стек
7. По окончании символов в строке, проверяем, есть ли необработанный остаток.
   Если есть, кладем его в стек
8. Объединяем строки стека в одну строку и возвращаем ее

Вычислительная сложность:
1. Считывание всех строк - O(n), n - число строк
2. Распаковка строки - O(maxL), maxL - максимальная длина строк
3. Получение префикса - О(maxL)
4. Общая вычислительная сложность - O(n*(2*maxL))

Пространственная сложность:
1. Так как храним только одну строку для анализа - сложность O(maxL)
2. Для распаковки строки используем стек - сложность О(maxL)
3. Возврат распакованной строки - сложность O(maxL)
4. Общая сложность - O(3*maxL)
"""


def unpackStr(s):
    prevpos = 0
    curpos = 0
    stack = []
    for ch in s:
        if ch.isalpha():
            curpos += 1
        elif ch.isdigit():
            stack.append(s[prevpos:curpos])
            stack.append(int(ch))
            curpos += 1
            prevpos = curpos
        elif ch == '[':
            stack.append(ch)
            curpos += 1
            prevpos = curpos
        elif ch == ']':
            if curpos != prevpos:
                stack.append(s[prevpos:curpos])
            ts = []
            tmpstr = stack.pop()
            while tmpstr != '[':
                ts.append(tmpstr)
                tmpstr = stack.pop()
            ts.reverse()
            num = stack.pop()
            stack.append(''.join(ts) * num)
            curpos += 1
            prevpos = curpos

    if curpos != prevpos:
        stack.append(s[prevpos:len(s)])

    return ''.join(stack)


def main():
    n = int(input())
    maxPrefixLen = -1
    basestr = ''
    for i in range(n):
        ps = input()
        ups = unpackStr(ps)

        if maxPrefixLen == -1:
            maxPrefixLen = len(ups)
            basestr = ups
        else:
            if len(ups) < maxPrefixLen:
                maxPrefixLen = len(ups)
            for i in range(maxPrefixLen):
                if ups[i] != basestr[i]:
                    maxPrefixLen = i
                    break
            if maxPrefixLen == 0:
                break

    print(basestr[:maxPrefixLen])


if __name__ == '__main__':
    main()
