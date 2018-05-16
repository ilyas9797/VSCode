from operator import itemgetter
import sys

Max_Cliques = []
n = 0
m = 0
matrix = []


def all_N(u):
    global matrix, n
    neighbors = set()
    for i in range(n):
        if matrix[u - 1][i] == 1:
            neighbors.add(i + 1)
    return neighbors


def choose_max_u(P, X):
    global matrix
    # m_sum = 0
    # m = 0
    return max([(i, matrix[i - 1]) for i in set.union(P, X)], key=itemgetter(1))[0]
    # for i in set.union(P, X):
    #     tmp_sum = sum(matrix[i - 1])
    #     if tmp_sum > m_sum:
    #         m_sum = tmp_sum
    #         m = i
    # return m


def dfs(R, P, X):
    global Max_Cliques
    if len(P) == 0 and len(X) == 0:
        ##############################
        Max_Cliques.append(R)
        # print(R)
        # if len(Max_Cliques[-1]) == n - 1:
        #     print(n - 1)
        #     print(' '.join(str(x) for x in Max_Cliques[-1]))
        #     print(' '.join(str(x) for x in set.difference({j + 1 for j in range(n)}, Max_Cliques[-1])))
        #     sys.exit()
        # elif len(Max_Cliques[-1]) < n - 1:
        #     if set.difference({j + 1 for j in range(n)}, Max_Cliques[-1]) in Max_Cliques:
        #         print(len(Max_Cliques[-1]))
        #         print(' '.join(str(x) for x in Max_Cliques[-1]))
        #         print(' '.join(str(x) for x in set.difference({j + 1 for j in range(n)}, Max_Cliques[-1])))
        #         sys.exit()
        #################################
        return
    u = choose_max_u(P, X)
    N_u = all_N(u)
    P_without_N_u = set.difference(P, N_u)
    while len(P_without_N_u) != 0:
        v = P_without_N_u.pop()
        N_v = all_N(v)
        dfs(set.union(R, {v}), set.intersection(P, N_v), set.intersection(X, N_v))
        P.discard(v)
        X.add(v)
        P_without_N_u = set.difference(P, N_u)


def main():
    global n, m, matrix, Max_Cliques
    # n, m = map(int, input().split())
    with open('4.txt', 'r') as file:
        n, m = map(int, file.readline().split())
        matrix = [[0 for j in range(n)] for i in range(n)]
        for k in range(m):
            i, j = map(int, file.readline().split())
            matrix[i - 1][j - 1] = 1
            matrix[j - 1][i - 1] = 1

    dfs(set(), {i + 1 for i in range(n)}, set())

    for i in Max_Cliques:
        if len(i) == n - 1:
            print(n - 1)
            print(' '.join(str(x) for x in i))
            print(' '.join(str(x) for x in set.difference({j + 1 for j in range(n)}, i)))
            break
        elif len(i) < n - 1:
            if set.difference({j + 1 for j in range(n)}, i) in Max_Cliques:
                print(len(i))
                print(' '.join(str(x) for x in i))
                print(' '.join(str(x) for x in set.difference({j + 1 for j in range(n)}, i)))
                break
    else:
        print(-1)

if __name__ == '__main__':
    main()