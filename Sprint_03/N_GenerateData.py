import random

n = int(input())
f = open('N_input.txt', 'w')
f.write(str(n) + '\n')
for i in range(n):
    p1 = random.randint(0, 10**7)
    p2 = random.randint(0, 10**7)
    while p1 == p2:
        p1 = random.randint(0, 10**7)
        p2 = random.randint(0, 10**7)
    f.write(str(min(p1, p2)) + ' ' + str(max(p1, p2)) + '\n')
f.close()
print('OK')
