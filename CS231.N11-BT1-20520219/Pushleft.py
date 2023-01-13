import cv2
import numpy as np

img1 = cv2.imread('messi1.jpg')
img2 = cv2.imread('messi2.jpg')

h1,w1,c1 = img1.shape
h2,w2,c2 = img2.shape

h=min(h1,h2)
w=min(w1,w1)

img1 = cv2.resize(img1,(w,h))
img2 = cv2.resize(img2,(w,h))
 
results=[]
Speed = 1
for D in range(0,w+1,Speed):
    result=img1.copy()
    result[:,0:w-D,:] = img1[:,D:w,:]
    result[:,w-D:w,:] = img2[:,0:D,:]
    cv2.imshow("PushLeft",result)
    if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()
            quit()

    