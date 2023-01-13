import cv2 as cv
import numpy as np


def cross_correlation(H, kernel):

    kernel_h, kernel_w = len(kernel), len(kernel[0])

    # init output matrix
    output = np.zeros_like(H)

    for x in range(H.shape[0] - kernel_h + 1):
        for y in range(H.shape[1] - kernel_w + 1):
            output[x, y] = (H[x: x + kernel_h, y: y + kernel_w] * kernel).sum()

    return output
