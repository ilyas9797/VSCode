import os, sys
from lilliput import encrypt, decrypt
from generate_samples_lilliput import generate_samples_for_checking_mes_of_perf
from shutil import rmtree


def encrypt_decrypt_samples(rounds_start, rounds_end, samples_num):
    # create new dir samples/
    if os.path.exists("samples") and os.path.isdir("samples"):
        rmtree("samples")
    os.mkdir("samples")
 
    #creating samples in dir samples/
    generate_samples_for_checking_mes_of_perf(samples_num)

    pts_f = "samples/pts.txt"

    key_f = "samples/key.txt"

    with open(key_f, "r") as file:
        key = file.read()

    # encrypting
    cts_f = "samples/cts{0}.txt"

    for rounds_number in range(rounds_start, rounds_end + 1):

        with open(cts_f.format(rounds_number), "w") as file_cts:
            with open(pts_f, "r") as file_pts:
                for line in file_pts:
                    file_cts.write(encrypt(line[:-1], key, rounds_number) + '\n')

    # decrypting
    dts_f = "samples/dts{0}.txt"

    for rounds_number in range(rounds_start, rounds_end + 1):

        with open(dts_f.format(rounds_number), "w") as file_dts:
            with open(cts_f.format(rounds_number), "r") as file_cts:
                for line in file_cts:
                    file_dts.write(decrypt(line[:-1], key, rounds_number) + '\n')

def check_mes_of_perf(rounds_start, rounds_end, samples_num):
    # checking measure of perfection
    cts_f = "samples/cts{0}.txt"

    for rounds in range(rounds_start, rounds_end + 1):
        print()

        print('Rounds number = {0}:'.format(rounds))

        with open(cts_f.format(rounds), "r") as file:

            for bit_pos in range(64):

                print('Bit position = {0}:'.format(bit_pos))
                mark_vector_for_diff_bits = bytes([0 for i in range(8)])

                for i in range(samples_num):

                    tmp = file.readline()[:-1]
                    ct0 = bytes([int(tmp[i:i+2], 16) for i in range(0, 16, 2)])

                    tmp = file.readline()[:-1]
                    ct1 = bytes([int(tmp[i:i+2], 16) for i in range(0, 16, 2)])

                    prep_ct = bytes([i^j for i,j in zip(ct0, ct1)])
                    mark_vector_for_diff_bits = bytes([i|j for i,j in zip(prep_ct, mark_vector_for_diff_bits)])

                print(''.join('{0:08b}'.format(x) for x in mark_vector_for_diff_bits))
                if ''.join('{0:08b}'.format(x) for x in mark_vector_for_diff_bits).find('0') != -1:
                    break

            else:
                print('Measure of perfection = {0}'.format(rounds))
                break

    else:
        print('Maybe it need to check more rounds or to consider more samples for every bit...')

if __name__ == '__main__':

    rounds_start = 1
    rounds_end = 6
    samples_num = 15
    encrypt_decrypt_samples(rounds_start, rounds_end, samples_num)
    check_mes_of_perf(rounds_start, rounds_end, samples_num)


