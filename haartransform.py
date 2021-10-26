import math

def ini_haar(tm):
    N = tm.shape[0]
    n = int(math.log2(N))
    x = [item / N for item in range(0, N)]
    r_max = n
    rm_pair = []

    for r in range(r_max):
        for m in range((2 ** r)):
            rm_pair.append(str(r) + "," + str(m + 1))

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

            if firs_lim <= x_val < seco_lim:
                m_val = v
            elif seco_lim <= x_val < thir_lim:
                m_val = -v

            met_row_tmp.append(float("{0:.4f}".format(m_val)))

        tm[inx+1] = met_row_tmp

    return tm/math.sqrt(tm.shape[0])