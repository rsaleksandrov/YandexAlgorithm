"""
Вася реализовал функцию, которая переводит целое число из десятичной
системы в двоичную. Но, кажется, она получилась не очень оптимальной.

Попробуйте написать более эффективную программу.
Не используйте встроенные средства языка по переводу чисел в
бинарное представление.

Формат ввода
На вход подаётся целое число в диапазоне от 0 до 10000.

Формат вывода
Выведите двоичное представление этого числа.
"""
n = int(input())
res = []
while n != 1:
    res.append(str(n % 2))
    n = n // 2
res.append(str(n))
res.reverse()
print("".join(res))
