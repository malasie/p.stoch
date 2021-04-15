import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.stats as stats

def krok(p):
    a=np.random.rand() #a in range [0,1)
    if a<p:
        return 1
    else:
        return -1

def spacer2(P0, N, p, a,b):
    poz=np.zeros([N+1,1])
    poz[0]=P0
    for i in range(1,N+1):
        poz[i]=poz[i-1]+krok(p)
        if poz[i]==a:
            return poz[0:i]
        if poz[i]==b:
            return poz[0:i+1]
    return poz

fig=plt.figure(figsize=(8,4), dpi=200)
plt.plot(spacer2(0,1000,0.5,-10,10), 'b.')
plt.plot(spacer2(0,1000,0.5,-10,10), 'r.')
plt.plot(spacer2(0,1000,0.5,-10,10), 'g.')
plt.plot(spacer2(0,1000,0.5,-10,10), 'c.')
plt.plot(spacer2(0,1000,0.5,-10,10), 'm.')
plt.show()