import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('messi1.jpg', 0)
h,w = img.shape

unique, counts = np.unique(img, return_counts=True)
#plot histogram

plt.bar(unique, counts, width=1)
plt.title('Histogram')
plt.show()

# calculate cdf
cdf = np.cumsum(counts)

#plot cdf
plt.plot(cdf)
plt.title('CDF')
plt.show()

calculate_he = np.zeros_like(unique)
calculate_he = np.round((cdf[:] - min(cdf))/ (h*w - min(cdf)) * 255)

equalized_v = dict(zip(unique, calculate_he))

balanced_img = np.zeros_like(img)
for i in range(h):
    for j in range(w):
        balanced_img[i,j] = equalized_v[img[i,j]]
        
cv.imshow("balanced_img", balanced_img)
cv.imshow("messi1_img", img)
#plot histogram
unique1, counts1 = np.unique(balanced_img, return_counts=True)
plt.bar(unique1, counts1, width=1)
plt.title('Histogram')
plt.show()


 


