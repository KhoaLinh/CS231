import numpy as np
from numpy.random import default_rng   # for random number generation
import random
from matplotlib import pyplot as plt   # for plotting

rng = default_rng()   # create a random number generator
try:
    rng_integers = rng.integers
except AttributeError:
    rng_integers = rng.randint
a = rng_integers(0, 100, size=70)   # generate 70 random integers between 0 and 100

arr = np.zeros((70,2))

for i in range(70):
    arr[i][0] = a[i]
    arr[i][1] = 2 * a[i] + -2.3
    
y = default_rng(42).random((30,2)) *5

x =  np.concatenate((arr, y))

while True:
    a = random.choice(x)
    b = random.choice(x)
    
    m = (b[1] - a[1]) / (b[0] - a[0])
    c = a[1] - m * a[0]
    
    count = 0
    
    for i in x:
        if i[1] < m * i[0] + c:
            count += 1
    if count >= 70:
        break
    
plt.plot(x, m * x + c, color='yellow')
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.show()

