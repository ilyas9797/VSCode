import os, sys, subprocess
from shutil import rmtree
from generate_samples_clefia import generate_samples_for_checking_mes_of_perf

def check_mes_of_perf(rounds_start, rounds_end, samples_num):
    # create new dir samples/
    if os.path.exists("samples") and os.path.isdir("samples"):
        rmtree("samples")
    os.mkdir("samples")

    # creating samples in dir samples/
    generate_samples_for_checking_mes_of_perf(samples_num)

    # encrypting and decrypting
    subprocess.check_call(["clefia_exec.exe", str(rounds_start), str(rounds_end)])

    # checking measure of perfection
    cts_f = "samples/cts{0}.txt"

    for rounds in range(rounds_start, rounds_end + 1):

        print('Rounds number = {0}:'.format(rounds))

        with open(cts_f.format(rounds), "rb") as file:

            for bit_pos in range(128):

                print('Bit position = {0}:'.format(bit_pos))
                mark_vector_for_diff_bits = bytes([0 for i in range(16)])

                for i in range(samples_num):

                    ct0 = file.read(16)
                    ct1 = file.read(16)

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
    check_mes_of_perf(1,10,25)
