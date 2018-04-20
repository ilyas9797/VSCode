import random, os
from shutil import rmtree

def create_samples_dir():
    # create new dir samples/
    if os.path.exists("samples") and os.path.isdir("samples"):
        rmtree("samples")
    os.mkdir("samples")

def generate_samples_for_checking_linear_props(samples_num):
    '''
    Генерирует файл (samples/pts.txt) с открытыми текстами, длины которых равны 16 байтам (128 битам)
    и файл с ключем (samples/key.txt) длинны 32 байта (256 бита).
    В файле sample_num*4 открытых текстов, т.к. для одной проверки требуется 4 открытых текста,
    обозначим их a, b, a+c, b+c (где a, b и c 16-байтные строки)
    '''

    key_f = "samples/key.txt"

    key = b'\xff\xee\xdd\xcc\xbb\xaa\x99\x88\x77\x66\x55\x44\x33\x22\x11\x00\xf0\xe0\xd0\xc0\xb0\xa0\x90\x80\x70\x60\x50\x40\x30\x20\x10\x00'

    with open(key_f, "wb") as file:
        file.write(key)


    pts_f = "samples/pts.txt"

    #pt = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'

    with open(pts_f, "wb") as file:
        #file.write(pt)
        
        for i in range(samples_num):
            pt_a = bytes([random.randint(0,255) for i in range(16)])
            pt_b = bytes([random.randint(0,255) for i in range(16)])
            pt_c = bytes([random.randint(0,255) for i in range(16)])

            pt_ac = bytes([i^j for i,j in zip(pt_a,pt_c)])
            pt_bc = bytes([i^j for i,j in zip(pt_b,pt_c)])


            file.write(pt_a)
            #print(pt_a)
            file.write(pt_b)
            file.write(pt_ac)
            file.write(pt_bc)

def generate_samples_for_checking_mes_of_perf(samples_num):
    '''
    Генерирует файл (samples/pts.txt) с открытыми текстами, длины которых равны 16 байтам (128 битам)
    и файл с ключем (samples/key.txt) длинны 32 байта (256 бита).
    В файле 128*sample_num*2 открытых текстов, т.к. для проверки каждой из 128 координат требуется samples_num пар векторов соседних (внутри своей пары) по данной координате.
    '''
    key_f = "samples/key.txt"

    key = b'\xff\xee\xdd\xcc\xbb\xaa\x99\x88\x77\x66\x55\x44\x33\x22\x11\x00\xf0\xe0\xd0\xc0\xb0\xa0\x90\x80\x70\x60\x50\x40\x30\x20\x10\x00'

    with open(key_f, "wb") as file:
        file.write(key)


    pts_f = "samples/pts.txt"

    with open(pts_f, "wb") as file:

        for bit_pos in range(128):

            for i in range(samples_num):

                pts = [random.randint(0,255) for i in range(16)]
                byte_with_curr_bit = list('{0:08b}'.format(pts[bit_pos//8]))

                byte_with_curr_bit[bit_pos%8] = '0'
                pts[bit_pos//8] = int(''.join(x for x in byte_with_curr_bit), 2)
                file.write(bytes(pts))

                byte_with_curr_bit[bit_pos%8] = '1'
                pts[bit_pos//8] = int(''.join(x for x in byte_with_curr_bit), 2)
                
                file.write(bytes(pts))

