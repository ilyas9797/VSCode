from task_2 import calc_ci, letters_frequences
from operator import itemgetter

C = 'BNVSNSIHQCEELSSKKYERIFJKXUMBGYKAMQLJTYAVFBKVTDVBPWRJYYLAOKYMPQSCGDLFSRLLPROYGESEBUUALRWXMMASAZLGLEDFJBZAVVPXWICGJXASCBYEHOSNMULKCEAHTQOKMFLEBKFXLRRFDTZXCIWBJSICBGAWDVYDHAVFJXZIBKCGJIWEAHTTOEWTUHKRQVVRGZBXYIREMMASCSPBNLHJMBLRFFJELHWEYLWISTFVVYFJCMHYUYRUFSFMGESIGRLWALSWMNUHSIMYYITCCQPZSICEHBCCMZFEGVJYOCDEMMPGHVAAUMELCMOEHVLTIPSUYILVGFLMVWDVYDBTHFRAYISYSGKVSUUHYHGGCKTMBLRX'


def freq_bigrams(C):
    freq = {}
    for i in range(len(C) // 2):
        if freq.get(C[i * 2: i * 2 + 2]):
            freq[C[i * 2: i * 2 + 2]] += 1
        else:
            freq[C[i * 2: i * 2 + 2]] = 1
    return sorted(freq.items(), key=itemgetter(1), reverse=True)


def main():
    for i in range(1, 10):
        print('key length = ' + str(i))
        for j in range(i):
            print(calc_ci(C[j::i]))
    # print(len(C))
    # print(freq_bigrams(C))
    # print(C.lower())
    # print(letters_frequences(C))

    # for k_l in range(3, 10):
    #     print(k_l)
    #     texts = []
    #     for i in range(k_l):
    #         text = C[i::k_l]
    #         freq = letters_frequences(text)
    #         # print(freq)
    #         shift = ord(freq[0][0]) - ord('E')
    #         texts.append(''.join(chr((ord(x) - 65 - shift) % 26 + 65 ) for x in text))
    #     P = ''.join(''.join(y for y in x) for x in list(zip(*texts)))
    #     print(P)
    #     print(calc_ci(P))
    # вероятнее всего длянна ключа 6

    k_l = 6
    texts = []
    for i in range(k_l):
        print(i)
        text = C[i::k_l]
        freq = letters_frequences(text)
        print(freq)
        print()
        if i == 3:
            shift = ord(freq[1][0]) - ord('E')
        else:
            shift = ord(freq[0][0]) - ord('E')
        texts.append(''.join(chr((ord(x) - 65 - shift) % 26 + 65 ) for x in text))
    P = ''.join(''.join(y for y in x) for x in list(zip(*texts)))
    print(P)
    print(calc_ci(P))



if __name__ == '__main__':
    main()
