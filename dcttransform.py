import numpy as np
import math

def init_dct(input_img, rows, cols):
    output_img = np.zeros((rows, cols), complex)
    for u in range(0, rows):  # Moving along rows
        for v in range(0, cols):  # Moving along cols
            for x in range(0, rows):  # Evaluation loop
                for y in range(0, cols):  # Evaluation loop
                    cosx = math.cos(((2 * x + 1) * u * math.pi) / (2 * rows))
                    cosy = math.cos(((2 * y + 1) * v * math.pi) / (2 * rows))
                    output_img[u][v] += input_img[x][y] * cosx * cosy

            if u == v == 0:
                output_img[u][v] = output_img[u][v] / rows
            else:
                output_img[u][v] = (output_img[u][v] * 2) / rows
    return output_img
