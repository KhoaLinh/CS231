import cv2
import numpy as np
# đọc ảnh foreground
fg = cv2.imread('KLnen.jpg')
print('Kich thuoc theo tung kenh cua foreground: ', fg.shape)

# đọc ảnh effect
eff = cv2.imread('effect.png')
print('Kich thuoc theo tung kenh cua eff: ', eff.shape)

# đọc ảnh mask
mask = cv2.imread('KLnen-removebg.png', cv2.IMREAD_UNCHANGED)
print('Kich thuoc theo tung kenh cua mask: ', mask.shape)

result = fg.copy()
alpha = 0.6
result[mask[:,:,3] != 0] = fg[mask[:,:,3] != 0] * alpha \
    + eff[mask[:,:,3] != 0] * (1 - alpha)

cv2.imshow('Result', result)
cv2.waitKey(0)
