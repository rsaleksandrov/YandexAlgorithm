"""
Помогите Васе понять, будет ли фраза палиндромом.
Учитываются только буквы и цифры, заглавные и строчные буквы
считаются одинаковыми.
Решение должно работать за O(N), где N — длина строки на входе.

Формат ввода
В единственной строке записана фраза или слово.
Буквы могут быть только латинские. Длина текста не превосходит 20000 символов.
Фраза может состоять из строчных и прописных латинских букв, цифр,
знаков препинания.

Формат вывода
Выведите «True», если фраза является палиндромом, и «False», если не является.
"""
iStr = input()
isStop = False
if len(iStr) <= 1:
    print("True")
else:
    lb = 0
    rb = len(iStr) - 1
    while lb < rb:
        lch = iStr[lb].upper()
        while not lch.isalnum() and lb < rb:
            lb += 1
            lch = iStr[lb].upper()
        rch = iStr[rb].upper()
        while not rch.isalnum() and lb < rb:
            rb -= 1
            rch = iStr[rb].upper()
        if lb < rb:
            if lch != rch:
                isStop = True
                break
        else:
            if lb != rb:
                isStop = True
            break
        lb += 1
        rb -= 1
    if isStop:
        print("False")
    else:
        print("True")
