#-*-coding:utf8;-*-
#qpy:3
#qpy:console
from math import floor, sqrt


def Ferma_method(n):
    x0 = floor(sqrt(n)) + 1
    for i in range(n):
        x = x0 + i
        y = sqrt(x**2 - n)
        if int(y) - y == 0:
            if (x - y)*(x + y) == n and x - y != 1 and x + y != 1:
                return list(map(int, [(x - y), (x + y)]))
        
if __name__ == "__main__":
    n = 10000049000057
    print(Ferma_method(n))