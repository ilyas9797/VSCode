####
##  LILLIPUT
####

from lilliput_lib import create_state_hex,exctract_round_key,roundFnLFSM,nonlinear_layer,linear_layer,permutation
                         
####
##  Constante
####
sbox = [4, 8, 7, 1, 9, 3, 2, 14, 0, 11, 6, 15, 10, 5, 13, 12]
perm=[13, 9, 14, 8, 10, 11, 12, 15, 4, 5, 3, 1, 2, 6, 0, 7] # Encryption permutation
perm_d=[14, 11, 12, 10, 8, 9, 13, 15, 3, 1, 4, 5, 6, 0, 2, 7] # Decryption permutation


####
## Example of test vectors
####
#MSG = '0123456789abcdef'
#Master_KEY = '0123456789abcdef0123'
#MSG='0000000000000000'
#Master_KEY='00000000000000000000'


def encrypt(MSG, Master_KEY, rounds):
    '''
    lilliput encryption
    '''
    state_M = create_state_hex(MSG)
    state_K = create_state_hex(Master_KEY)

    #for i in range(29):
    for i in range(rounds-1):
        #if i == rounds:
        #    break
        RK = exctract_round_key(state_K, i, sbox)
        state_K = roundFnLFSM(state_K, 0)
        state_M = nonlinear_layer(state_M, RK, sbox)
        state_M = linear_layer(state_M)
        state_M = permutation(state_M, perm)
    #else:
    #RK = exctract_round_key(state_K, 29, sbox)
    RK = exctract_round_key(state_K, rounds-1, sbox)
    state_M = linear_layer(nonlinear_layer(state_M, RK, sbox))
    C = ''.join(hex(i)[2:] for i in reversed(state_M))
    return C

def decrypt(crypted_MSG, Master_KEY, rounds):
    state_M = create_state_hex(crypted_MSG)
    state_K = create_state_hex(Master_KEY)

    for i in range(rounds-1):
        state_K = roundFnLFSM(state_K, 0)
    
    for i in range(rounds-1, 0, -1):
        RK = exctract_round_key(state_K, i, sbox)
        #if i == 29: print(RK)
        state_K = roundFnLFSM(state_K, 1)
        state_M = nonlinear_layer(state_M, RK, sbox)
        state_M = linear_layer(state_M)
        state_M = permutation(state_M, perm_d)
    #if rounds == 29:
    RK = exctract_round_key(state_K, 0, sbox)
    state_M = linear_layer(nonlinear_layer(state_M, RK, sbox))
    M = ''.join(hex(i)[2:] for i in reversed(state_M))
    return M
