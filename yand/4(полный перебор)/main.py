from math import ceil

def comb(n, k):
    """Генерация сочетаний из `n` по `k` без повторений."""

    d = list(range(0, k))
    yield list(map(lambda x: x+1, d))

    while True:
        i = k - 1
        while i >= 0 and d[i] + k - i + 1 > n:
            i -= 1
        if i < 0:
            return

        d[i] += 1
        for j in range(i + 1, k):
            d[j] = d[j - 1] + 1

        yield list(map(lambda x: x+1, d))

def main():

    n, m = map(int, input().split())
    v = []

    # ввод ребер
    for i in range(m):
        v.append(sorted(map(int, input().split())))
    
    # перебор по различным сочетаниям вершин
    for num in range(1, n):
        for i in comb(n, num):
            norm_i = i
            # проверка 1-го подграфа с вершинами из `i` на полноту
            for j in range(len(i) - 1):
                for k in range(j + 1, len(i)):
                    try:
                        v.index([i[j], i[k]])
                    except:
                        # отсутствие ребра между `i[j]` и `i[k]` вершинами
                        break
                # если все ребра для `i[j]` вершины присутствуют, продолжаем проверку 1-го подграфа, переходя к вершине `i[j+1]`
                else:
                    continue
                # при отсутсвии какого-либо ребра для `i[j]` вершины переходим к проверке другого подграфа
                break
            # если нашли 1-й полный подграф, проверяем соответствующий ему 2-ой на полноту
            else:
                not_i = sorted(list(set([x + 1 for x in range(n)]) - set(norm_i)))
                for j in range(len(not_i) - 1):
                    for k in range(j + 1, len(not_i)):
                        try:
                            v.index([not_i[j], not_i[k]])
                        except:
                            break
                    else:
                        continue
                    break
                else:
                    print(num)
                    print(' '.join(str(x) for x in norm_i))
                    print(' '.join(str(x) for x in not_i))
                    return
    print("-1")

if __name__ == "__main__":
    main()