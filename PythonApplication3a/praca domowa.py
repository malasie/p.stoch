#ZAD 2

import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.stats as stats
import math

def f(x):
    y=(5*x**2-50*x+105)/(x**2)
    return y

#podpunkt a
def calka(x):
    return 5*x-50*math.log(x)-105/x
print(abs(calka(6)-calka(3)))

x1=3
x2=6
#f(3) # =0
#f(6) # = -0.41(6)

#pochodna: (50x-210)/x**3 = 0 -> 50x-210=0
y1=f(210/50)
y2=0


#podpunkt b
N=1000
pole=[]

for j in range(0,N):
    X=np.random.uniform(x1,x2,N)
    Y=np.random.uniform(y1,y2,N)
    p=0
    z=0
    for i in range(0,N):
        if Y[i]>=f(X[i]):
            p=p+1
        else: z=z+1
    pole.append((p/(p+z))*(x2-x1)*(y2-y1))

#print(pole)

#podpunkt c
plt.hist(pole,bins=20)
plt.show()
normalny=stats.norm(np.mean(pole),np.std(pole))
print(stats.kstest(pole,normalny.cdf)) # pvalue>0.1 ->rozkład normalny

# podpunkt d
print(stats.ttest_1samp(pole,abs(calka(6)-calka(3)))) # wartości zgodne