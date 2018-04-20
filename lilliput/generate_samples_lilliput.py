import random

def generate_samples_for_checking_linear_props(samples_num):

    key_f = "samples/key.txt"

    key = '0123456789abcdef0123'

    with open(key_f, "w") as file:
        file.write(key)


    pts_f = "samples/pts.txt"

    #pt = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'

    with open(pts_f, "w") as file:
        #file.write(pt)
        
        for i in range(samples_num):
            pt_a = ''.join(x for x in ['{0:02x}'.format(random.randint(0,255)) for i in range(8)])
            pt_b = ''.join(x for x in ['{0:02x}'.format(random.randint(0,255)) for i in range(8)])
            pt_c = ''.join(x for x in ['{0:02x}'.format(random.randint(0,255)) for i in range(8)])

            pt_ac = ''.join(x for x in ['{0:01x}'.format(int(i,16) ^ int(j,16)) for i,j in zip(pt_a,pt_c)])
            pt_bc = ''.join(x for x in ['{0:01x}'.format(int(i,16) ^ int(j,16)) for i,j in zip(pt_b,pt_c)])


            file.write(pt_a + '\n')
            file.write(pt_b + '\n')
            file.write(pt_ac + '\n')
            file.write(pt_bc + '\n')


def generate_samples_for_checking_mes_of_perf(samples_num):
    '''
    Генерирует файл (samples/pts.txt) с открытыми текстами, длины которых равны 8 байтам (64 битам)
    и файл с ключем (samples/key.txt) длинны 10 байтов (80 битов).
    В файле 64*sample_num*2 открытых текстов, т.к. для проверки каждой из 64 координат требуется samples_num пар векторов соседних (внутри своей пары) по данной координате.
    '''
    key_f = "samples/key.txt"

    key = '0123456789abcdef0123'

    with open(key_f, "w") as file:
        file.write(key)


    pts_f = "samples/pts.txt"

    with open(pts_f, "w") as file:

        for bit_pos in range(64):
            #print('Bit position = {0}'.format(bit_pos))

            for i in range(samples_num):

                pts = [random.randint(0,255) for i in range(8)]
                byte_with_curr_bit = list('{0:08b}'.format(pts[bit_pos//8]))

                byte_with_curr_bit[bit_pos%8] = '0'
                pts[bit_pos//8] = int(''.join(x for x in byte_with_curr_bit), 2)
                file.write(''.join('{0:02x}'.format(x) for x in pts) + '\n')

                byte_with_curr_bit[bit_pos%8] = '1'
                pts[bit_pos//8] = int(''.join(x for x in byte_with_curr_bit), 2)
                file.write(''.join('{0:02x}'.format(x) for x in pts) + '\n')


