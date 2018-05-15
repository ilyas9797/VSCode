import os, sys
from lilliput import encrypt, decrypt
from generate_samples_lilliput import generate_samples_for_checking_linear_props
from shutil import rmtree

def encrypt_decrypt_samples(rounds_start, rounds_end, samples_num):
    # create new dir samples/
    if os.path.exists("samples") and os.path.isdir("samples"):
        rmtree("samples")
    os.mkdir("samples")
 
    #creating samples in dir samples/
    generate_samples_for_checking_linear_props(samples_num)

    pts_f = "samples/pts.txt"

    key_f = "samples/key.txt"

    with open(key_f, "r") as file:
        key = file.read()

    # encrypting
    cts_f = "samples/cts{0}.txt"

    for rounds_number in range(rounds_start, rounds_end + 1):
        print('{0} encryption'.format(rounds_number))

        with open(cts_f.format(rounds_number), "w") as file_cts:
            with open(pts_f, "r") as file_pts:
                for line in file_pts:
                    file_cts.write(encrypt(line[:-1], key, rounds_number) + '\n')

    # decrypting
    dts_f = "samples/dts{0}.txt"

    for rounds_number in range(rounds_start, rounds_end + 1):
        print('{0} decryption'.format(rounds_number))

        with open(dts_f.format(rounds_number), "w") as file_dts:
            with open(cts_f.format(rounds_number), "r") as file_cts:
                for line in file_cts:
                    file_dts.write(decrypt(line[:-1], key, rounds_number) + '\n')

def check_linear_props(rounds_start, rounds_end, samples_num):
    cts_f = "samples/cts{0}.txt"

    for rounds_number in range(rounds_start, rounds_end + 1):
        
        print(rounds_number)

        with open(cts_f.format(rounds_number), "r") as file:

            mark_vector = bytes([0 for i in range(16)])

            for i in range(samples_num):

                ct_a = file.readline()[:-1]
                ct_b = file.readline()[:-1]
                ct_ac = file.readline()[:-1]
                ct_bc = file.readline()[:-1]

                prep_a = [int(i,16) ^ int(j,16) for i,j in zip(ct_a,ct_ac)]
                prep_b = [int(i,16) ^ int(j,16) for i,j in zip(ct_b,ct_bc)]

                xored_ab = [i^j for i,j in zip(prep_a,prep_b)]

                mark_vector = [i|j for i,j in zip(xored_ab,mark_vector)]
            
            bin_mark_vector = ''.join('{0:04b}'.format(x) for x in mark_vector)
            print(bin_mark_vector)

            if bin_mark_vector.find('0') == -1:
                print("Transformation is non-linear after {0} round(s)".format(rounds_number))
                return 0

    else:
        print("Transformation seems linear till.\nMaybe need more rounds or another samples")
    return 1  

def check_stab_of_linear_props(rounds_start, rounds_end, samples_num):
    for rounds in range(rounds_start, rounds_end + 1):
        if check_linear_props(rounds, rounds, samples_num) != 0:
            print("Transformation is linear at {0}-th round".format(rounds))
            return 1
    return 0     

if __name__ == '__main__':

    rounds_start = 1
    rounds_end = 50
    samples_num = 15
    encrypt_decrypt_samples(rounds_start, rounds_end, samples_num)
    check_linear_props(rounds_start, rounds_end, samples_num)
    #check_stab_of_linear_props(rounds_start, rounds_end, samples_num)


