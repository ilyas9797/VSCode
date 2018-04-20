#-*-coding:utf8;-*-
#qpy:3
#qpy:console
from math import floor
# from keyless_reading import Ferma_method

def gcdex(a, b, xy):
    '''
    xy: list
    '''
    if a == 0:
        xy[0] = 0
        xy[1] = 1
        return b
    d = gcdex(b % a, a, xy)
    y = xy[0]
    xy[0] = xy[1] - floor(b / a) * xy[0]
    xy[1] = y
    return d
    

def reverse_a_mod_n(a, n):
    xy = [0, 0]
    d = gcdex(a, n, xy)
    if d != 1:
        print("Error: gcd(a,n) != 1")
        return -1
    return (xy[0] % n + n) % n

# if __name__ == "__main__":
#     e = 42791935
#     n = 75726223
#     p, q = Ferma_method(n)
#     print(p, q)
#     d = reverse_a_mod_n(e, (p - 1) * (q - 1))
#     print(d)
#     print(pow(13104610, d, n))


