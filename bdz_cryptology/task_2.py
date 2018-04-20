from operator import itemgetter


C = 'EMGLOSUDCGDNCUSWYSFHNSFCYKDPUMLWGYICOXYSIPJCKQPKUGKMGOLICGINCGACKSNISACYKZSCKXECJCKSHYSXCGOIDPKZCNKSHICGIWYGKKGKGOLDSILKGOIUSIGLEDSPWZUGFZCCNDGYYSFUSZCNXEOJNCGYEOWEUPXEZGACGNFGLKNSACIGOIYCKXCJUCIUZCFZCCNDGYYSFEUEKUZCSOCFZCCNCIACZEJNCSHFZEJZEGMXCYHCJUMGKUCY'

def letters_frequences(C):
    alph = [chr(i) for i in range(65, 91)]
    freq = {}
    for s in alph:
        freq[s] = C.count(s)
    return sorted(freq.items(), key=itemgetter(1), reverse=True)


def calc_ci(C):
    '''
    Вычисляет индекс совпадений текста C, если return ~ 0,065 значит шифр простой замены
    '''
    ci = 0
    for i in letters_frequences(C):
        ci += i[1] ** 2
    return ci / (len(C) ** 2)


def main():
    freq = letters_frequences(C)
    print(calc_ci(C))
    shift = ord(freq[0][0]) - ord('E')
    print(''.join(chr((ord(x) - 65 - shift) % 26 + 65 ) for x in C))
    print(C.lower())


if __name__ == '__main__':
    main()
