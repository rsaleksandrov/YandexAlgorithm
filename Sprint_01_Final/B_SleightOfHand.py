"""
Гоша и Тимофей нашли необычный тренажёр для скоростной печати и хотят
освоить его. Тренажёр представляет собой поле из клавиш 4× 4, в котором на
каждом раунде появляется конфигурация цифр и точек. На клавише написана либо
точка, либо цифра от 1 до 9. В момент времени t игрок должен одновременно
нажать на все клавиши, на которых написана цифра t. Гоша и Тимофей могут
нажать в один момент времени на k клавиш каждый. Если в момент времени t были
нажаты все нужные клавиши, то игроки получают 1 балл.

Найдите число баллов, которое смогут заработать Гоша и Тимофей,
если будут нажимать на клавиши вдвоём.
(см. рисунок)

Формат ввода
В первой строке дано целое число k (1 ≤ k ≤ 5).
В четырёх следующих строках задан вид тренажёра – по 4 символа в каждой
строке. Каждый символ — либо точка, либо цифра от 1 до 9.
Символы одной строки идут подряд и не разделены пробелами.

Формат вывода
Выведите единственное число – максимальное количество баллов, которое
смогут набрать Гоша и Тимофей.
"""
if __name__ == "__main__":
    k = int(input())
    iField = []
    for i in range(4):
        iField.append(input())
    res = 0
    for i in range(9):
        # tmpRes = 0
        # for el in iField:
        #     tmpRes += el.count(str(i + 1))
        tmpRes = sum([el.count(str(i + 1)) for el in iField])
        if 0 < tmpRes <= k * 2:
            res += 1
    print(res)
