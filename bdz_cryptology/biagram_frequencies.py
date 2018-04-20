biagrams_freq1 = '''A B C D E F G H I J K L M
A 4 20 28 52 2 11 28 4 32 4 6 62 23
B 13 0 0 0 55 0 0 0 8 2 0 22 0
C 32 0 7 1 69 0 0 33 17 0 10 9 1
D 40 16 9 5 65 18 3 9 56 0 1 4 15
E 84 20 55 125 51 40 19 16 50 1 4 55 54
F 19 3 5 1 19 21 1 3 30 2 0 11 1
G 20 4 3 2 35 1 3 15 18 0 0 5 1
H 101 1 3 0 270 5 1 6 57 0 0 0 3
I 40 7 51 23 25 9 11 3 0 0 2 38 25
J 3 0 0 0 5 0 0 0 1 0 0 0 0
K 1 0 0 0 11 0 0 0 13 0 0 0 0
L 44 2 5 12 62 7 5 2 42 1 1 53 2
M 52 14 1 0 64 0 0 3 37 0 0 0 7'''

biagrams_freq2 = '''N O P Q R S T U V W X Y Z
A 167 2 14 0 83 76 127 7 25 8 1 9 1
B 0 11 0 0 15 4 2 13 0 0 0 15 0
C 0 50 3 0 10 0 28 11 0 0 0 3 0
D 6 16 4 0 21 18 53 19 5 15 0 3 0
E 146 35 37 6 191 149 65 9 26 31 12 5 0
F 0 51 0 0 26 8 47 6 3 3 0 2 0
G 4 21 1 1 20 9 21 9 0 5 0 1 0
H 2 44 1 0 3 10 18 6 0 5 0 3 0
I 202 56 12 1 46 79 117 1 22 0 4 0 3
J 0 4 0 0 0 0 0 3 0 0 0 0 0
K 2 2 0 0 0 6 2 1 0 2 0 1 0
L 2 25 1 1 2 16 23 9 0 1 0 33 0
M 1 17 18 1 2 12 3 8 0 1 0 2 0'''

biagrams_freq3 = '''A B C D E F G H I J K L M
N 42 10 47 122 63 19 106 12 30 1 6 6 9
O 7 12 14 17 5 95 3 5 14 0 0 19 41
P 19 1 0 0 37 0 0 4 8 0 0 15 1
Q 0 0 0 0 0 0 0 0 0 0 0 0 0
R 83 8 16 23 169 4 8 8 77 1 10 5 26
S 65 9 17 9 73 13 1 47 75 3 0 7 11
T 57 22 7 1 76 5 2 330 126 1 0 14 10
U 11 5 9 6 9 1 6 0 9 0 1 19 5
V 7 0 0 0 72 0 0 0 28 0 0 0 0
W 36 1 1 0 38 0 0 33 36 0 0 4 1
X 1 0 2 0 0 1 0 0 3 0 0 0 0
Y 14 5 4 2 7 12 2 6 10 0 0 3 7
Z 1 0 0 0 4 0 0 0 0 0 0 0 0'''

biagrams_freq4 = '''N O P Q R S T U V W X Y Z
N 7 54 7 1 7 44 124 6 1 15 0 12 0
O 134 13 23 0 91 23 42 55 16 28 0 4 1
P 0 27 9 0 33 14 7 6 0 0 0 0 0
Q 0 0 0 0 0 0 0 17 0 0 0 0 0
R 16 60 4 0 24 37 55 6 11 4 0 28 0
S 12 56 17 6 9 48 116 35 1 28 0 4 0
T 6 79 7 0 49 50 56 21 2 27 0 24 0
U 31 1 15 0 47 39 31 0 3 0 0 0 0
V 0 5 0 0 0 0 0 0 0 0 0 3 0
W 8 15 0 0 0 4 2 0 0 1 0 0 0
X 0 1 5 0 0 0 3 0 0 1 0 0 0
Y 5 17 3 0 4 16 30 0 0 5 0 0 0
Z 0 0 0 0 0 0 0 0 0 0 0 0 0'''


def create_list_from_str(biagrams_freq):
    b_f = []
    for i in biagrams_freq.splitlines():
        b_f.append(i.split())
    return b_f


def append_freq_to_dict(bgrm_frq, *args):
    for b_f in args:
        for i in range(1, 14):
            for j in range(1, 14):
                bgrm_frq[b_f[i][0] + b_f[0][j - 1]] = int(b_f[i][j])


def get_biagrams_freq():
    bgrm_frq = {}

    b_f1 = create_list_from_str(biagrams_freq1)
    b_f2 = create_list_from_str(biagrams_freq2)
    b_f3 = create_list_from_str(biagrams_freq3)
    b_f4 = create_list_from_str(biagrams_freq4)

    append_freq_to_dict(bgrm_frq, b_f1, b_f2, b_f3, b_f4)

    return bgrm_frq
    
# print(get_biagrams_freq()['TN'])