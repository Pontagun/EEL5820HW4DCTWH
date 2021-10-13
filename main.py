import numpy as np;
import math;

import haartransform as haar
import walshtransform as walsh

def create_metric(size):
    return np.zeros((size, size))




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    transfMtrc = create_metric(4)  # input N = 2**n
    # wh = ini_wht(transfMtrc)

    haar.ini_haar(transfMtrc)
