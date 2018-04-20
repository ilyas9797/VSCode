from FI_table import FI_table
from multiprocessing import Pool
from time import time

vectors = []
for i in range(0, 65536):
    s = '{0:016b}'.format(i)
    vectors.append(([int(s[0]),int(s[1]),int(s[2]),int(s[3]),int(s[4]),int(s[5]),int(s[6]),int(s[7]),int(s[8]),int(s[9]),int(s[10]),int(s[11]),int(s[12]),int(s[13]),int(s[14]),int(s[15])],i))

def scalar(x,u):
    return x[0]*u[0]^x[1]*u[1]^x[2]*u[2]^x[3]*u[3]^x[4]*u[4]^x[5]*u[5]^x[6]*u[6]^x[7]*u[7]^x[8]*u[8]^x[9]*u[9]^x[10]*u[10]^x[11]*u[11]^x[12]*u[12]^x[13]*u[13]^x[14]*u[14]^x[15]*u[15]

def W_uolsh(a):
    W = [0 for i in range(16)]
    for x in vectors:
        c = '{0:016b}'.format(FI_table[0][x[1]])
        for i in range(16):
            W[i] += (-1) ** (int(c[i]) ^ scalar(x[0], a[0]))
    return W

def W_furie(a):
    W = [0 for i in range(16)]
    for x in vectors:
        c = '{0:016b}'.format(FI_table[0][x[1]])
        for i in range(16):
            W[i] += ((-1) ** scalar(a[0], x[0])) * int(c[i])
    return W

def compute_W_uolsh():
    pool = Pool()

    results = pool.map(W_uolsh, vectors[::1000])

    pool.close()
    pool.join()

    with open("FI_W_uolsh.txt", "w") as file:
        #file.write('''"a": n\n''')
        #dump({str(a): n for a, n in zip(range(len(results)), results)}, file, indent=4)
        for i in range(len(results)):
            file.write("a = " + str(i*1000)+":\n")
            file.write("y0 y1 y2 y3 y4 y5 y6 y7 y8 y9 y10 y11 y12 y13 y14 y15\n")
            file.write(str(results[i])+"\n")


def compute_W_furie():
    pool = Pool()

    results = pool.map(W_furie, vectors[::1000])

    pool.close()
    pool.join()

    with open("FI_W_furie.txt", "w") as file:
        #file.write('''"a": n\n''')
        #dump({str(a): n for a, n in zip(range(len(results)), results)}, file, indent=4)
        for i in range(len(results)):
            file.write("a = " + str(i*1000)+":\n")
            file.write("y0 y1 y2 y3 y4 y5 y6 y7 y8 y9 y10 y11 y12 y13 y14 y15\n")
            file.write(str(results[i])+"\n")

if __name__ == '__main__':
    start = time()
    compute_W_uolsh()

    compute_W_furie()

    print(time() - start)

    


