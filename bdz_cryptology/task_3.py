from task_2 import calc_ci, letters_frequences

C = 'KCCPKBGUFDPHQTYAVINRRTMVGRKDNBVFDETDGILTXRGUDDKOTFMBPVGEGLTGCKQRACQCWDNAWCRXIZAKFTLEWRPTYCQKYVXCHKFTPONCQQRHJVAJUWETMCMSPKQDYHJVDAHCTRLSVSKCGCZQQDZXGSFRLSWCWSJTBHAFSIASPRJAHKJRJUMVGKMITZHFPDISPZLVLGWTFPLKKEBDPGCEBSHCTJRWXBAFSPEZQNRWXCVYCGAONWDDKACKAWBBIKFTIOVKCGGHJVLNHIFFSQESVYCLACNVRWBBIREPBBVFEXOSCDYGZWPFDTKFQIYCWHJVLNHIQIBTKHJVNPIST'
# c = C.lower()

def main():
    for i in range(1, 7):
        print('key length = ' + str(i))
        for j in range(i):
            print(calc_ci(C[j::i]))
    # вероятнее всего, что длинна ключа 3
    k_l = 3
    texts = []
    for i in range(k_l):
        text = C[i::k_l]
        freq = letters_frequences(text)
        print(freq)
        shift = ord(freq[0][0]) - ord('E')
        texts.append(''.join(chr((ord(x) - 65 - shift) % 26 + 65 ) for x in text))
    P = ''.join(''.join(y for y in x) for x in list(zip(*texts)))
    print(P)
    print(calc_ci(P))
    

if __name__ == '__main__':
    main()
