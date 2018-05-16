from random import randint

with open('4.txt', 'w') as file:
    n = 100
    m = 1000
    file.write(str(n) + ' ' + str(m) + '\n')
    for i in range(m):
        a = i % (n - 2) + 1
        b = randint(a + 1, n)
        file.write(str(a) + ' ' + str(b) + '\n')