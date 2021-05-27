import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.stats as stats

MP=[[0,0.6,0.4,0,0],[0.4,0,0.6,0,0],[0,0.4,0,0,0,0.6,0.5,0,3,0.1,0.1,0]]

def przejście(P):
    sP=[P[0]]
    for i in range(1, len(P)):
        sP.append(sP[-1]+P[i])
    a=np.random.rand()
    for i in range(0, len(P)):
        if a<sP[i]:
            return i+1
L=[]
X=[1]
for i in range(10000):
    while X[-1]<5:
        X.append(przejście(MP[X[-1]-1]))
    L.append(len(X)-1)
print(np.mean(L))