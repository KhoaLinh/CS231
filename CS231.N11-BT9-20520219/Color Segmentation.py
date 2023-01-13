import cv2 
import numpy as np
from matplotlib import pyplot as plt

img = plt.imread('People.png')
ground = plt.imread('bien.jpg') 

h,w,c = img.shape
ground = cv2.resize(ground,(w,h))

background = img [:600, :750,:]

min_val = np.min(background, axis=(0,1))
max_val = np.max(background, axis=(0,1))
mask = cv2.inRange(img, min_val, max_val)

res = cv2.bitwise_and(img, img, mask=mask)
f = img - res
plt.imshow(f)

