import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.stats as stats
import math


def funkcja(l,x):
    if x>0:
        return l*np.exp(-l*x)
    else: return 0

la=0.1
TS=[]
for j in range(1,500):
    x0=np.random.rand()
    X=[x0]
    for i in range (1,3000):
        xp=X[-1]+np.random.normal()
        A=np.min([1,funkcja(la,xp)/funkcja(la,X[-1])])
        a=np.random.rand()
        if a<=A:
            X.append(xp)
        else: X.append(X[-1])
    TS.append(np.mean(X))
    print(j)

plt.hist(TS,30)
plt.show()
print(np.mean(TS))
print(np.std(TS))

normalny=stats.norm(np.mean(TS), np.std(TS))


print(stats.ttest_lsamp(TS,l/la))