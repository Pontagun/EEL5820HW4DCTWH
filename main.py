import numpy as np;
import math;

def create_metric(size):
    return np.zeros((size, size))

def get_binary(decical, bits):
    return (bin(decical).replace("0b", "")).zfill(bits)

def ini_wht(tm):

    n = int(math.log2(tm.shape[0]))
    print("There are " + str(n) + " bits")

    for ridx in range(tm.shape[1]): # row
        row_bin = get_binary(ridx, n)
        row_bin = row_bin[::-1]
        for cidx in range(tm.shape[0]): # col
            col_bin = get_binary(cidx, n)
            B = 1
            for i in range(n): # bit represent
                B = B * (-1)**(int(col_bin[i])*int(row_bin[i]))

            tm[cidx, ridx] = B

    return tm;


def ini_harr(tm):
    pass


def ini_dct(tm):
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    transfMtrc = create_metric(8) # input N = 2**n
    wh = ini_wht(transfMtrc)

