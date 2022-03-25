import numpy as np
from PIL import ImageFilter

gaussianbandwidths = [0.5, 1, 1.5, 2, 2.5, 3, 3.5]


def GaussianBlurRandom(img):
    gaussianidx = np.random.randint(0, len(gaussianbandwidths))
    gaussianbandwidth = gaussianbandwidths[gaussianidx]
    return GaussianBlur(img, gaussianbandwidth)


def GaussianBlur(img, bandwidth):
    print(ImageFilter.GaussianBlur(bandwidth))
    img = img.filter(ImageFilter.GaussianBlur(bandwidth))
    return img
