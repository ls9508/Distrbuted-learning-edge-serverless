import numpy as np
from scipy.special import zeta
import random

def disance(vec1, vec2):
    dist = np.sqrt(np.sum((np.array(vec1) - np.array(vec2)) ** 2))
    return dist




def zipf(n,a,f):
# n number of variable
# a distribution parameter
# f name of variable
    p = []
    for i in range(n):
        pi = pow(i + 1, -a) / zeta(a)
        p.append(pi)
    # p = p / sum(p)
    r = []
    for i in range (n):
        num = round(p[i]*100)
        for _ in range(num):
            r.append(f[i])
    fc = random.sample(r,1)
    return fc