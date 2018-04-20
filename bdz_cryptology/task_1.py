from operator import itemgetter
from reverse_by_modulo import reverse_a_mod_n, gcdex

C = 'KQEREJEBCPPCJCRKIEACUZBKRVPKRBCIBQCARBJCVFCUPKRIOFKPACUZQEPBKRXPEIIEABDKPBCPFCDCCAFIEABDKPBCPFEQPKAZBKRHAIBKAPCCIBURCCDKDCCJCIDFUIXPAFFERBICZDFKABICBBENEFCUPJCVKABPCYDCCDPKBCOCPERKIVKSCPICBRKIJPKABI'


def calc_a_b(x1, y1, x2, y2, n):
    r_x2_x1 = reverse_a_mod_n(((x2 - x1) % n + n) % n, n)
    if r_x2_x1 == -1:
        print('Error 1')
        return None, None
    y2_y1 = ((y2 - y1) % n + n) % n
    a = r_x2_x1 * y2_y1 % n
    if gcdex(a, n, [0, 0]) != 1:
        print('Error 2')
        return None, None
    b = (y1 - a * x1) % n
    return a, b


def main():
    pass
    alph = [chr(i) for i in range(65, 91)]
    freq = {}
    for s in alph:
        freq[s] = C.count(s)
    # print(sorted(freq.items(), key=itemgetter(1), reverse=True))
    # print(alph.index('K'))
    a, b = calc_a_b(alph.index('C'), alph.index('E'), alph.index('B'), alph.index('T'), 26)
    print(a, b)
    print(''.join(x for x in [chr(((ord(x) - 65)*a + b) % 26 + 65) for x in C]))

if __name__ == '__main__':
    main()
