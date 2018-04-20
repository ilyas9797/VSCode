from operator import itemgetter


def symbols_freq_sorted_reverse(string):
    letters = {}
    for s in string:
        if letters.get(s):
            letters[s] += 1
        else:
            letters[s] = 1
    return sorted(letters.items(), key=itemgetter(1), reverse=True)


def go_in_tree(tree, coding, code):
    if type(tree[0]) == str:
        if code:
            coding[tree[0]] = code
        else:
            coding[tree[0]] = '0'
        return coding
    else:
        coding = {**coding, **go_in_tree(tree[0][1], coding, code + '0')} 
        coding = {**coding, **go_in_tree(tree[0][0], coding, code + '1')}  
        return coding


def Haffman_enc(letters):
    while len(letters) > 1:
        i = letters.pop()
        j = letters.pop()
        letters.append(([j, i], i[1] + j[1]))
        letters.sort(key=itemgetter(1), reverse=True)
    coding = {}
    coding = go_in_tree(letters[0], coding, '')
    return coding


def mainEnc():
    string = input()
    letters = symbols_freq_sorted_reverse(string)
    n = len(letters)
    coding = Haffman_enc(letters)
    coded_string = ''.join(coding[x] for x in string)
    print(n, len(coded_string))
    for k,v in coding.items():
        print(k + ': ' + v)
    print(coded_string)


def Haffman_dec(codding, coded_string):
    string = ''
    tmp = ''
    while coded_string:
        tmp += coded_string[0]
        coded_string = coded_string[1:]
        if codding.get(tmp):
            string += codding[tmp]
            tmp = ''
    return string


def mainDec():
    k, l = map(int, input().split())
    coding = {}
    for i in range(k):
        letter, code = input().split(': ')
        coding[code] = letter
    coded_string = input()
    print(Haffman_dec(coding, coded_string))


if __name__ == "__main__":
    # mainEnc()
    mainDec()
