"""
ID 67832885

Работу программы можно разделить на два этапа:
    - формирование хэш таблицы частоты появления слова в документе
      (функция makehashtable)
    - расчет релевантности запроса (функция calcrelevant)

Этап "Формирование хэш таблицы частоты появления слова в документе"
    Информация о частоте появления слова в документе хранится в словаре,
    в котором ключем является слово, а значением словарь соответствия 
    номера предложения (ключ) и сколько раз слово встретилось в 
    документе (значение).
    Заполнение словаря проходит по алегоритму:
        - получаем список слов документа.
        - для каждого слова проверяем, есть ли оно в словаре или нет.
        - если нет, то для этого слова в словаре создается запись, 
          ключем которой является слово, а значением пустой словарь.
        - если слово в словаре есть, то получаем ссылку на словарь, 
          соответствующий этому слову.
        - в полученном словаре проверяем наличие в нем записи с 
          номером документа.
        - если записи нет, она создается со значением "1" и ключем 
          "номер документа".
        - если запись есть, значение увеличивается на 1.

Этап "Расчет релевантности запроса"
    Для каждого запроса получаем список его слов.
    Создаем вспомогательные структуры (обнуляются для каждого запроса):
        - словарь учета слов, для которых расчитана релевантность. Если 
          слово уже встречалось, релевантность для него не расчитывается 
          и оно пропускается.
        - массив для хранения релевантности запроса. Каждый элемент массива
          содержит сумму частоты вхождения слов запроса в документ и номер 
          документа с обратным знаком (для корректной сортировки).
    Для каждого слова запроса проверяем, расчитывали для него релевантность
    или нет. Если расчитывали, то переходим к следующему слову. Если нет, то
    из хэш таблицы, сформированной на первом этапе получаем частоту вхождения
    слова запроса в документы. Переносим эти данные во массив для хранения 
    релевантности запроса.
    После обработки всех слов запроса сортируем массив для хранения 
    релевантности запроса и выводим 5 последних элементов в обратном порядке.
    Если при выводе встретился элемент с нулевой релевантностью, то вывод
    прекращаем.
    
Вычислительная сложность:
Вычислительную сложность первого этапа можно оценить как O(n*k) поскольку
имеется только один цикл. k - количество слов в документе.
Оценка вычислительной сложности второго этапа:
    - в лучшем случае - O(m * nlog(n)). Предполагается что в запросы состоят из 
      небольшого (много меньше m) числа слов и эти слова редко встречаются в
      документах
    - в худшем случае - O(m * k * n * nlog(n)), где m - число запросов,
      k - число уникальных слов в запросе (>=m), n - число документов

Пространственная сложность:
Пространственная сложность первой части алгоритма оценивается как O(n*k)
Пространственная сложность второй части алгоритма - O(n) - выделяется
дополнительная память для храниения релевантности запросов в разрезе документов

"""


def makehashtable(pht, pwords, docnum):
    for word in pwords:
        if word not in pht.keys():
            pht[word] = {}
        docht = pht[word]
        if docnum not in docht.keys():
            docht[docnum] = 1
        else:
            docht[docnum] += 1


def calcrelevant(pht, pwords, pdoccount, pdrnum):
    reldocs = [[0, 0]] * pdoccount
    wht = {}
    for word in pwords:
        if word not in wht.keys():
            wht[word] = 1
            if word in pht.keys():
                worddocrels = pht[word]
                for wdr in worddocrels:
                    reldocs[wdr] = [reldocs[wdr][0] + worddocrels[wdr],
                                    -wdr]
    reldocs.sort()
    start = pdoccount - 1
    stop = (pdoccount - pdrnum - 1) if pdoccount >= pdrnum else -1
    res = []
    for j in range(start, stop, -1):
        if reldocs[j][0] == 0:
            break
        else:
            res.append(abs(reldocs[j][1]) + 1)
    return res


def main_v2():
    n = int(input())
    ht = {}
    # Читаем предложения текста и расчитываем релевантность слов
    for i in range(n):
        words = input().split()
        makehashtable(ht, words, i)

    # Работаем с запросами
    m = int(input())
    for i in range(m):
        docwords = input().split()
        res = calcrelevant(ht, docwords, n, 5)
        print(*res)


if __name__ == '__main__':
    main_v2()