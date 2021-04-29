import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.stats as stats

def zmiana(p):
    a=np.random.rand()
    if a<p:
        return 1
    else:
        return 0


def populacja(p):
    LP=[1]
    lpt=0
    while lpt<1000:
        lpt=LP[len(LP)-1]
        lp0=lpt
        for i in range(0, lp0):
            lpt=lpt+zmiana(p)
        LP.append(lpt)
    return LP

Sl=[]
P=[]
for j in range(0,10):
    pu=(j+1)/10
    P.append(pu)
    L=[]
    for i in range(0,100):
        L.append(len(populacja(pu)))
    Sl.append(np.mean(L))

plt.plot(P,Sl,'bx')
plt.show()