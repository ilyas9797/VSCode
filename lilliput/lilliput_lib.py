# Work with only 64-bit inner X and 80-bit Key (both are 16-based strings)

#sbox = [4, 8, 7, 1, 9, 3, 2, 14, 0, 11, 6, 15, 10, 5, 13, 12]
#perm=[13, 9, 14, 8, 10, 11, 12, 15, 4, 5, 3, 1, 2, 6, 0, 7]; # Encryption permutation
#perm_d=[14, 11, 12, 10, 8, 9, 13, 15, 3, 1, 4, 5, 6, 0, 2, 7]; # Decryption permutation

#Create state

def create_state_hex(X):
    state = list(reversed([int(i, 16) for i in X]))
    return state
    
def create_state_bin(X):
    return list(reversed([int(X[4*i:4*i+4], 2) for i in range(len(X)//4)]))
    
   
# Round function

def nonlinear_layer(X,K, sbox):
    for i in range(8):
        X[8+i] = X[8+i]^sbox[X[7-i]^K[i]]
    return X

def linear_layer(X):
    for i in range(1, 7):
        X[15] = X[15]^X[i]
        X[15-i] = X[15-i]^X[7]
    X[15] = X[15]^X[7]
    return X

def permutation(X, perm):
    state = [0 for i in range(16)]
    for i in range(16):
        state[perm[i]] = X[i]
    return state

# Keyschedule

def exctract_round_key(K, i, sbox):
    tmp = '{0:04b}'.format(K[18]) +\
    '{0:04b}'.format(K[16]) +\
    '{0:04b}'.format(K[13]) +\
    '{0:04b}'.format(K[10]) +\
    '{0:04b}'.format(K[9]) +\
    '{0:04b}'.format(K[6]) +\
    '{0:04b}'.format(K[3]) +\
    '{0:04b}'.format(K[1])

    #print(tmp)
    
    RK = ''
    
    for j in range(8):
        s = int(tmp[j] + tmp[8+j] + tmp[16+j] + tmp[24+j], 2)
        RK_tmp = sbox[s]
        RK += '{0:04b}'.format(RK_tmp)
    
    # ???
    #print(RK)
    RK = '{0:05b}'.format(int(RK[:5], 2) ^ i) + RK[5:]
    #print(RK)
    #print(create_state_bin(RK))
    return create_state_bin(RK)

def rotl(bin, d):
    return bin[d:] + bin[:d]
    
def rotr(bin, d):
    return bin[len(bin) - d:] + bin[:len(bin) - d]
    
def shiftl(bin, d):
    return bin[d:] + ''.join(['0' for i in range(d)])
    
def shiftr(bin, d):
    return ''.join(['0' for i in range(d)]) + bin[:len(bin) - d]
    
def roundFnLFSM(K, d):
    if d>0:
        for i in range(0, 16, 5):
            #print('K = ' + str(K))
            K[i:i+5] = K[i+1:i+5] + K[i:i+1]
    
    state = [0 for i in range(20)]
    # L0
    state[0] = K[0] ^ int(rotr('{0:04b}'.format(K[4]), 1), 2)
    state[1] = K[1] ^ int(shiftr('{0:04b}'.format(K[2]), 3), 2)
    state[2] = K[2]
    state[3] = K[3]
    state[4] = K[4]
    # L1
    state[5] = K[5]
    state[6] = K[6] ^ int(shiftl('{0:04b}'.format(K[7]), 3), 2)
    state[7] = K[7]
    state[8] = K[8]
    state[9] = K[9] ^ int(rotl('{0:04b}'.format(K[8]), 1), 2)
    # L2
    state[10] = K[10]
    state[11] = K[11] ^ int(rotr('{0:04b}'.format(K[12]), 1), 2)
    state[12] = K[12]
    state[13] = K[13] ^ int(shiftr('{0:04b}'.format(K[12]), 3), 2)
    state[14] = K[14]
    # L3
    state[15] = K[15]
    state[16] = K[16] ^ int(shiftl('{0:04b}'.format(K[15]), 3), 2) ^ int(rotl('{0:04b}'.format(K[17]), 1), 2)
    state[17] = K[17]
    state[18] = K[18]
    state[19] = K[19]
    ## permutation
    if d<=0:
        for i in range(0, 16, 5):
            #if i == 0: print('state = ' + str(state))
            state[i:i+5] = state[i+4:i+5] + state[i:i+4]
    return state
