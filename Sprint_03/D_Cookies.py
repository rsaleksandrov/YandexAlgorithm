"""
К Васе в гости пришли одноклассники. Его мама решила угостить ребят печеньем.
Но не всё так просто. Печенья могут быть разного размера. А у каждого ребёнка
есть фактор жадности —– минимальный размер печенья, которое он возьмёт.
Нужно выяснить, сколько ребят останутся довольными в лучшем случае, когда они
действуют оптимально.

Каждый ребёнок может взять не больше одного печенья.

Формат ввода
В первой строке записано n —– количество детей.
Во второй —– n чисел, разделённых пробелом, каждое из которых –— фактор
жадности ребёнка. Это натуральные числа, не превосходящие 1000.
В следующей строке записано число m –— количество печенек.
Далее —– m натуральных чисел, разделённых пробелом —– размеры печенек.
Размеры печенек не превосходят 1000.

Оба числа n и m не превосходят 10000.

Формат вывода
Нужно вывести одно число –— количество детей, которые останутся довольными
"""


def searchCookieId(pData, pValue, pLeftBound, pRightBound, isUsed):
    if pLeftBound >= pRightBound:
        id = min(pLeftBound, pRightBound)
        if id < len(pData) and pData[id] >= pValue:
            while id < len(pData):
                if not isUsed[id] and pData[id] >= pValue:
                    isUsed[id] = True
                    return id
                id += 1
            return -1
        else:
            return -1
    mid = (pLeftBound + pRightBound) // 2
    if pData[mid] >= pValue:  # Ищем самое первое вхождение pValue
        return searchCookieId(pData, pValue, pLeftBound, mid, isUsed)
    else:
        return searchCookieId(pData, pValue, mid + 1, pRightBound, isUsed)


def searchCookieId_v2(pData, pValue, pLeftBound, pRightBound):
    if pLeftBound >= pRightBound:
        id = min(pLeftBound, pRightBound)
        if id < len(pData) and pData[id] >= pValue:
            return id
        else:
            return -1
    mid = (pLeftBound + pRightBound) // 2
    if pData[mid] > pValue:
        return searchCookieId_v2(pData, pValue, pLeftBound, mid)
    elif pData[mid] < pValue:
        return searchCookieId_v2(pData, pValue, mid + 1, pRightBound)
    else:
        return mid


n = int(input())
iFactor = list(map(int, input().split()))
m = int(input())
iCookies = list(map(int, input().split()))
iFactor.sort()
iCookies.sort()
# isCookiesUse = [False] * m
idCook = idFactor = 0
childCount = 0
while idCook < len(iCookies) and idFactor < len(iFactor):
    if iFactor[idFactor] <= iCookies[idCook]:
        childCount += 1
        idFactor += 1
    idCook += 1

# for el in iFactor:
#     if searchCookieId(iCookies, el, 0, m, isCookiesUse) == -1:
#         break
#     childCount += 1
#     i += 1
print(childCount)
