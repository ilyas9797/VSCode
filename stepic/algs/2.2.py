def Pisano_period_fib_mod(n, m):
    f=[]
    f.append(0)
    f.append(1)
    for i in range(2,n+1):
        f[i%2] = (f[0]+f[1])%m
        if [f[(i+1)%2], f[i%2]] == [0, 1]:
            return i + 1 - 2

def fib_mod(n, m):
    f=[]
    f.append(0)
    f.append(1)
    for i in range(2,n+1):
        f[i%2] = (f[0]+f[1])%m
    return f[n%2]

def main():
    n, m = map(int, input().split())
    p = Pisano_period_fib_mod(m ** 2 + 1, m)
    print(fib_mod(n % p, m))


if __name__ == "__main__":
    main()