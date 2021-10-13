import numpy as np;
import math;


def create_metric(size):
    return np.zeros((size, size))


def get_binary(decical, bits):
    return (bin(decical).replace("0b", "")).zfill(bits)


def ini_wht(tm):
    n = int(math.log2(tm.shape[0]))
    print("There are " + str(n) + " bits")

    for ridx in range(tm.shape[1]):  # row
        row_bin = get_binary(ridx, n)
        row_bin = row_bin[::-1]
        for cidx in range(tm.shape[0]):  # col
            col_bin = get_binary(cidx, n)
            B = 1
            for i in range(n):  # bit represent
                B = B * (-1) ** (int(col_bin[i]) * int(row_bin[i]))

            tm[cidx, ridx] = B

    return tm;


def ini_haar(tm):
    N = tm.shape[0]  # For example, N = 8
    n = int(math.log2(N))  # n = 3
    x = [item / N for item in range(0, N)]
    r_max = n
    rm_pair = []

    for r in range(r_max):
        for m in range((2 ** r)):
            rm_pair.append(str(r) + "," + str(m + 1))
            # print(str(r) + " " + str(m))

    tm[0] = 1

    for inx, val in enumerate(rm_pair):

        met_row_tmp = []

        r = int(val.split(",")[0])
        m = int(val.split(",")[1])
        v = 2 ** (r / 2)

        firs_lim = (m - 1) / 2 ** r
        seco_lim = (m - 1 / 2) / 2 ** r
        thir_lim = (m / 2 ** r)


        for i, x_val in enumerate(x):
            m_val = 0

            if firs_lim <= x_val and x_val < seco_lim:
                m_val = v
            elif seco_lim <= x_val and x_val < thir_lim:
                m_val = -v

            met_row_tmp.append(float("{0:.2f}".format(m_val)))

        # tm[inx+1] = met_row_tmp
        tm[inx+1] = met_row_tmp

    print(tm)

def ini_dct(tm):
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    transfMtrc = create_metric(4)  # input N = 2**n
    # wh = ini_wht(transfMtrc)

    ini_haar(transfMtrc)
