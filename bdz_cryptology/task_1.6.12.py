'''
Двойной перестановочный шифр, размер матрицы 10x11
'''
from task_2 import calc_ci
from biagram_frequencies import get_biagrams_freq
from itertools import permutations
from operator import itemgetter


C = 'TNOSSKAIMAGAEITMHETHTSRHXXIHEUXDXNUEIDSATDTDDSARAHHENTTTDSOUIOEARTFHDAOMWYWFERTNEONFDYAHSEIMEDGRWTATISURUARTHJ'


def make_perms_by_biagramms(row):
    b_f = get_biagrams_freq()
    for s in row:
        perm = ''
        letters = list(row)
        perm += s
        letters.remove(s)
        
        while letters:
            tmp_dict = {}
            for l in letters:
                tmp_dict[perm[-1] + l] = b_f[perm[-1] + l]
            k, v = list(sorted(tmp_dict.items(), key=itemgetter(1), reverse=True))[0]
            perm += k[-1]
            letters.remove(k[-1])
            
        print(perm)


def main():

    rows = [C[i * 11: i * 11 + 11] for i in range(10)]
    for r in rows:
        print(r)
        print()
        make_perms_by_biagramms(r)
        print()
        print('=====================')
        print()
    print()



    # columns = [C[i: i + 9 * 11 + 1: 11] for i in range(11)]
    # for i in columns:
    #     print(i)
    # print()




if __name__ == '__main__':
    main()
