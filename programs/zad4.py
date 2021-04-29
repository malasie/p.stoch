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

LP=[1]
def populacja(p):
    for j in range(0,10):
        lpt=LP[len(LP-1)]
        for i in range(0, lpt):
            lpt=lpt+zmiana(p)
        LP.append(lpt)
    print(LP)

populacja(0.5)