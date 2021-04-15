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

def spacer(P0, N, p):
    poz=np.zeros([N+1,1])
    poz[0]=P0
    for i in range(1,N+1):
        poz[i]=poz[i-1]+krok(p)
    return poz


#fig=plt.figure(figsize=(8,4), dpi=200)
#plt.plot(spacer(0,1000,0.5), 'b.')
#plt.plot(spacer(0,1000,0.5), 'r.')
#plt.plot(spacer(0,1000,0.5), 'g.')
#plt.show()

NN=1000
Pk1=np.zeros([NN,1])
for i in range(1,NN):
    a=spacer(0,1000,0.5)
    Pk1[i]=a[-1]

plt.subplot(2,1,1)
plt.title('N=1000')
#plt.axis([-350,350,0,300])
plt.hist(Pk1,20)

plt.show()