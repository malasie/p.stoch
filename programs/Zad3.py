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

def bariera(po):
    a=np.random.rand()
    if a<po:
        return 1
    else: return 0

def spacer3(P0, N, p, a,b, po):
    poz=np.zeros([N+1,1])
    poz[0]=P0
    for i in range(1,N+1):
        if poz[i-1]==a:
            poz[i]=poz[i-1]+bariera(po)
        else:
            poz[i]=poz[i-1]+krok(p)
        if poz[i]==b:
            return poz[0:i+1]
    return poz

fig=plt.figure(figsize=(8,4), dpi=200)
plt.plot(spacer3(0,1000,0.5,-10,10,0.5), 'b.')
plt.plot(spacer3(0,1000,0.5,-10,10,0.5), 'r.')
plt.plot(spacer3(0,1000,0.5,-10,10,0.5), 'g.')
plt.plot(spacer3(0,1000,0.5,-10,10,0.5), 'c.')
plt.plot(spacer3(0,1000,0.5,-10,10,0.5), 'm.')
plt.show()

DL=[]
B=0
for i in range(0,1000):
    W=spacer3(0,1000,0.5,-10,10,0.5)
    DL.append(len(W))
    if W[len(W)-1]==10:
        B=B+1

plt.hist(DL)
plt.show()
print(B/1000)
