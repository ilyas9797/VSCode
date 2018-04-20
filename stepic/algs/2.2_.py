from numpy import dot, array

def matr_pow(n):
    a = array([[0, 1], [1, 1]])
    res = array([[1, 0], [0, 1]])
    while n:
        if n & 1:
            res = dot(res, a)
        a = dot(a, a)
        print(n)
        n >>= 1
    return res

def fib_mod(n, m):
    f=[]
    f.append(0)
    f.append(1)
    for i in range(2,n+1):
        f[i%2] = (f[0]+f[1])%m
    return f[n%2]


def main():
    # n, m = map(int, input().split())
    # print(fib_mod(n, m))
    print(binpow_mod(2))


if __name__ == "__main__":
    main()