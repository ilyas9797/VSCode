def main():
    k, m, d = map(int, input().split())
    d0 = d
    i = 1
    s = m + k * int(bool((5 - (d - 1) % 7) * (6 - (d - 1) % 7))) - i
    while s >= 0:
        d += 1
        i += 1
        s += k * int(bool((5 - (d - 1) % 7) * (6 - (d - 1) % 7))) - i
    print(d - d0)

if __name__ == '__main__':
    main()