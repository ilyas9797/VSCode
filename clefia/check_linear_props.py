from subprocess import check_call, check_output
from generate_samples_clefia import generate_samples_for_checking_linear_props, create_samples_dir

def check_linear_props(rounds_start, rounds_end, samples_num):
    # checking linear properties
    cts_f = "samples/cts{0}.txt"

    for rounds in range(rounds_start, rounds_end + 1):
        
        print(rounds)
        
        with open(cts_f.format(rounds), "rb") as file:

            mark_vector = bytes([0 for i in range(16)])
        
            for i in range(samples_num):
                ct_a = file.read(16)
                ct_b = file.read(16)
                ct_ac = file.read(16)
                ct_bc = file.read(16)

                prep_a = bytes([i^j for i,j in zip(ct_a, ct_ac)])
                prep_b = bytes([i^j for i,j in zip(ct_b, ct_bc)])
            
                xored_ab = bytes([i^j for i,j in zip(prep_a, prep_b)])

                mark_vector = bytes([i|j for i,j in zip(mark_vector, xored_ab)])

            bin_mark_vector = ''.join('{0:08b}'.format(x) for x in mark_vector)
            print(bin_mark_vector)

            if bin_mark_vector.find('0') == -1:
                print("Transformation is non-linear after {0} round(s)".format(rounds))
                return 0   
    else:
        print("Transformation is linear till. Maybe it need to check more rounds or to consider more samples for every round...")
    
    return 1

def check_stab_of_linear_props(rounds_start, rounds_end, samples_num):
    for rounds in range(rounds_start, rounds_end + 1):
        if check_linear_props(rounds, rounds, samples_num) != 0:
            print("Transformation is linear at {0}-th round".format(rounds))
            return 1
    return 0
        

if __name__ == '__main__':
    rounds_start = 1
    rounds_end = 100
    samples_num = 15

    # create directory samples/
    create_samples_dir()

    # creating samples in dir samples/
    generate_samples_for_checking_linear_props(samples_num)

    # encrypting and decrypting
    check_call(["clefia_exec.exe", str(rounds_start), str(rounds_end)])

    # check linear properties
    check_linear_props(rounds_start, rounds_end, samples_num)

    # check stability of linear properties
    #check_stab_of_linear_props(rounds_start, rounds_end, samples_num)

