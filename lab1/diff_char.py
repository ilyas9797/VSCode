from multiprocessing import Pool
from json import dump
import time

from S7_S9_FI import S7_table, S9_table
from FI_table import FI_table

def diff_char_table_S7(a):
    '''
    return -> словарь с разностными значениями преобразования S7 для всвозможных пар (a,b)
    {
        (a1,b0) -> количество векторов x удовлетворяющих условию разностной характеристики для заданной пары (a,b),
        ...
        (a127,b127) -> количество векторов x...
    }
    '''
    table = [0 for i in range(128)]

    #for a in a_range:
    #for b in range(128):

    for x in range(128):

        b = S7_table[x] ^ S7_table[x^a]
        table[b] += 1
    
    return max(table)

def diff_char_table_S9(a):
    '''
    return -> словарь с разностными значениями преобразования S9 для всвозможных пар (a,b)
    {
        (a1,b0) -> количество векторов x удовлетворяющих условию разностной характеристики для заданной пары (a,b),
        ...
        (511,511) -> количество векторов x...
    }
    '''
    table = [0 for i in range(512)]

    #for a in a_range:
    #for b in range(512):

    for x in range(512):

        b = S9_table[x] ^ S9_table[x^a]
        table[b] += 1
    
    return max(table)

def diff_char_table_FI(a):
    '''
    return -> словарь с разностными значениями преобразования FI для всвозможных пар (a,b)
    {
        (a1,b0) -> количество векторов x удовлетворяющих условию разностной характеристики для заданной пары (a,b),
        ...
        (a65535,b65535) -> количество векторов x...
    }
    '''
    table = [[0 for i in range(65536)] for i in range(len(FI_table))]

    #for a in a_range:
    #for b in range(65536):
    for i in range(len(FI_table)):

        for x in range(65536):

            b = FI_table[i][x] ^ FI_table[i][x^a]
            table[i][b] += 1
    
    return [max(table[i]) for i in range(len(table))]

def compute_diff_charr_table_S7():
    '''
    Вывод таблицы с разностной характеристикой преобразования S7 в файл S7_diff_char_table.txt
    '''
    pool = Pool()

    a_range = [i for i in range(1, 128)]
    results = pool.map(diff_char_table_S7, a_range)

    pool.close()
    pool.join()

    with open("S7_diff_char_table.txt", "w") as file:
        file.write("MAX = " + str(max(results)) + "\n" + '''    "a": n\n''')
        dump({str(a): m for a, m in zip(range(1, len(results)+1), results)}, file, indent=4)

def compute_diff_charr_table_S9():
    '''
    Вывод таблицы с разностной характеристикой преобразования S9 в файл S9_diff_char_table.txt
    '''
    pool = Pool()

    a_range = [i for i in range(1, 512)]
    results = pool.map(diff_char_table_S9, a_range)

    pool.close()
    pool.join()

    with open("S9_diff_char_table.txt", "w") as file:
        file.write("MAX = " + str(max(results)) + "\n" + '''    "a": n\n''')
        dump({str(a): m for a, m in zip(range(1, len(results)+1), results)}, file, indent=4)

def compute_diff_charr_table_FI():
    '''
    Вывод таблицы с разностной характеристикой преобразования FI в файл FI_diff_char_table.txt
    '''
    pool = Pool()

    a_range = [i for i in range(1, 65536, 1000)]
    results = pool.map(diff_char_table_FI, a_range)

    pool.close()
    pool.join()

    with open("FI_diff_char_table.txt", "w") as file:
        subkey = 0
        for i in range(len(results)):
            file.write("MAX = " + str(max(results[i])) + " subkey = "+str(subkey)+"\n")# + '''    "a": n\n''')
            #dump({str(a): m for a, m in zip(range(1, len(results[i])+1), results[i])}, file, indent=4)
            file.write('\n')
            subkey += 127



if __name__ == '__main__':
    start = time.time()

    #compute_diff_charr_table_S7()

    #compute_diff_charr_table_S9()

    compute_diff_charr_table_FI()
    
    print(time.time() - start)
