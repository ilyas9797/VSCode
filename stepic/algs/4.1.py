from operator import itemgetter


def get_covering_set(n, segments):
    points = []
    segments.sort(key=itemgetter(1))
    for i in segments:
        if points:
            if i[0] <= points[-1]:
                continue
        points.append(i[1])
    return points


def main1():
    n = int(input())
    segments = []
    for i in range(n):
        segments.append(list(map(int, input().split())))
    points = get_covering_set(n, segments)
    print(len(points))
    print(' '.join(str(x) for x in points))


def get_max_price(w, items):
    price = 0
    items.sort(key=lambda x: x[0]/x[1], reverse=True)
    for i in items:
        w -= i[1]
        price += i[0]
        if w <= 0:
            price -= -w * (i[0]/i[1])
            break
    return price


def main2():
    n, w = map(int, input().split())
    items = []
    for i in range(n):
        items.append(list(map(int, input().split())))
    print('{0:.3f}'.format(get_max_price(w, items)))


def get_sum_decomposition(n):
    decomposition = []
    i = 1
    while n > 0:
        if (n - i) == 0 or (n - i) > i:
            decomposition.append(i)
            n -= i
        i += 1
    return decomposition


def main3():
    n = int(input())
    decomp = get_sum_decomposition(n)
    print(len(decomp))
    print(' '.join(str(x) for x in decomp))

if __name__ == "__main__":
    main3()
