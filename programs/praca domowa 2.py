
import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.stats as stats

def krok(p,q):
    a=np.random.rand() #a in range [0,1)
    if a<p:
        return 1
    elif a<p+q:
        return -1
    else:
        return 0

def spacer(W0, N, p, q):
    pozycja=np.zeros([N+1,1])
    pozycja[0]=W0
    for i in range(1,N+1):
        pozycja[i]=pozycja[i-1]+krok(p,q)
    return pozycja


#plt.plot(spacer(25,1000,0.35,0.25), 'r.')
#plt.plot(spacer(25,1000,0.35,0.25), 'b.')
#plt.plot(spacer(25,1000,0.35,0.25), 'g.')
#plt.show()


n=1000
Wn=np.zeros([n,1])
for i in range(1,n):
    a=spacer(25,1000,0.35,0.25)
    Wn[i]=a[-1]


plt.subplot(2,1,1)
plt.title('N=1000')
plt.hist(Wn,20)

plt.show()

print(sum(Wn)/n)
print(25+1000*(0.35-0.25))
