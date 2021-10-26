import time

import numpy
import numpy as np
import math
import cv2
from PIL import Image

import haartransform as haar
import walshtransform as walsh
import dcttransform as dc


def create_metric(size):
    return np.zeros((size, size))


def pixel_normalization(unorm_image):
    pxmin = unorm_image.min()
    pxmax = unorm_image.max()

    for i in range(unorm_image.shape[0]):
        for j in range(unorm_image.shape[1]):
            unorm_image[i, j] = math.floor(((unorm_image[i, j] - pxmin) / (pxmax - pxmin)) * 255)

    norm_image = unorm_image
    return norm_image

def pixel_onenormalization(unorm_image):
    print(type(unorm_image))
    pxmin = unorm_image.min()
    pxmax = unorm_image.max()

    for i in range(unorm_image.shape[0]):
        for j in range(unorm_image.shape[1]):
            unorm_image[i, j] = float(round((unorm_image[i, j] - pxmin) / (pxmax - pxmin), 4))

    norm_image = unorm_image
    return norm_image


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    path1 = r'Dataset/b/b128.jpg'
    img1 = cv2.imread(path1, 0)
    img1 = img1.astype(float)
    transfMtrc = create_metric(img1.shape[0])  # input N = 2**n
    start_time = time.time()
    Hr = haar.ini_haar(transfMtrc)
    Hrt = np.transpose(Hr)
    img = Hr.dot(img1).dot(Hrt)
    print("--- %s seconds ---" % (time.time() - start_time))

    im = Image.fromarray(img)
    if im.mode != 'RGB':
        im = im.convert('RGB')
    im.save("b128haar.jpg")

    path1 =  r'Dataset/b/b128.jpg'
    img1 = cv2.imread(path1, 0)
    img1 = img1.astype(float)
    transfMtrc = create_metric(img1.shape[0])  # input N = 2**n

    start_time = time.time()
    W = walsh.ini_wht(transfMtrc)
    img = W.dot(img1).dot(W)
    print("--- %s seconds ---" % (time.time() - start_time))

    im = Image.fromarray(img)
    if im.mode != 'RGB':
        im = im.convert('RGB')
    im.save("b128Walsh.jpg")

    path1 =  r'Dataset/b/b128.jpg'
    # path1 = r'm64.jpg'
    img1 = cv2.imread(path1, 0)
    img1 = img1.astype(float)

    start_time = time.time()
    dct = dc.init_dct(img1, img1.shape[0], img1.shape[1])
    print("--- %s seconds ---" % (time.time() - start_time))

    img = abs(dct)

    im = Image.fromarray(img)
    if im.mode != 'RGB':
        im = im.convert('RGB')
    im.save("b128dct.jpg")

