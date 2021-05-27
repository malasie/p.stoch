import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.stats as stats
import math

def zmiana(p1):
    a=np.random.rand()
    if a<p1:
        return 1
    else:
        return 0


def populacja(p1,pk):
    LP=[1]
    lpt=0
    while lpt<600:
        lpt=LP[len(LP)-1]
        b=np.random.rand()
        if b<pk:
            lpt=math.floor(lpt/2)
        lp0=lpt
        for i in range(0,lp0):
            lpt=lpt+zmiana(p1)
        LP.append(lpt)
        if lpt==0:
            break
    return LP




def f(p1,pk):
    Prz=[]
    Wyg=[]
    for i in range(10000):
        LP=populacja(p1,pk)
        if LP[-1]==0:
            Wyg.append(len(LP))
        else: Prz.append(len(LP))
    print('średni czas do uzyskania 600 osobników: ' +  str(np.mean(Prz)))
    print('prawdopodobieństwo wyginięcia koloni przed osiągnięciem 600 osobników: '+ str((len(Wyg))/(len(Wyg)+len(Prz))))
    print('średni czas istnienia kolonii przed wyginięciem: ' +  str(np.mean(Wyg)))


f(0.65,0.15)


