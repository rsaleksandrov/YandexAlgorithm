"""
Представьте, что вы работаете пограничником и постоянно проверяете документы
людей по записи из базы. При этом допустима ситуация, когда имя человека в
базе отличается от имени в паспорте на одну замену, одно удаление или одну
вставку символа. Если один вариант имени может быть получен из другого
удалением одного символа, то человека пропустят через границу. А вот если есть
какое-либо второе изменение, то человек грустно поедет домой или в посольство.
Например, если первый вариант —– это «Лена», а второй — «Лера», то девушку
пропустят. Также человека пропустят, если в базе записано «Коля», а в
паспорте — «оля». Однако вариант, когда в базе числится «Иннокентий», а в
паспорте написано «ннакентий», уже не сработает. Не пропустят также человека,
у которого в паспорте записан «Иинннокентий», а вот «Инннокентий» спокойно
пересечёт границу. Напишите программу, которая сравнивает имя в базе с именем
в паспорте и решает, пропускать человека или нет. В случае равенства двух
строк — путешественника, естественно, пропускают.

Формат ввода
В первой строке дано имя из паспорта. Во второй строке —- имя из базы.
Обе строки состоят из строчных букв английского алфавита. Размер каждой строки
не превосходит 100 000 символов.

Формат вывода Выведите «OK», если человека пропустят, или «FAIL» в противном
случае.
"""
s1 = input()
s2 = input()

if abs(len(s1) - len(s2)) > 1:
    print('FAIL')
else:
    id1 = 0
    id2 = 0
    isCorrect = 0
    while id1 < len(s1) and id2 < len(s2):
        if s1[id1] == s2[id2]:
            id1 += 1
            id2 += 1
        else:
            isCorrect += 1
            if isCorrect > 1:
                print('FAIL')
                break
            else:
                if len(s1) == len(s2):
                    id1 += 1
                    id2 += 1
                elif len(s1) < len(s2):
                    id2 += 1
                else:
                    id1 += 1
    else:
        print('OK')
