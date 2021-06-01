import numpy as np
import random


def update_funcdp(ai, bi,  Ci, ae, be, Ce,si,se,func):
    ri = ai/bi
    re = ae/be
    for i in range(len(si)):
        r = ri[i].tolist()
        si[i].func=[]
        for j in range(len(func)):
            if popability(r[j]) and len(si[i].func)<Ci:
                si[i].func.append(func[j])
    for i in range(len(se)):
        r = re[i].tolist()
        se[i].func = []
        for j in range(len(func)):
            if popability(r[j]) and len(se[i].func) < Ce:
                se[i].func.append(func[j])
    return si,se


def get_reward(ai,bi,ae,be,si,se,func,R):
    for i in range(len(si)):
        popu = si[i].history
        for j in range(len(func)):
            r = popu.count([func[j]]) / (len(popu) + 0.01)
            ai[i][j] = ai[i][j]+r
            bi[i][j] = bi[i][j]+R-r
    for i in range(len(se)):
        popu = se[i].history
        for j in range(len(func)):
            r = popu.count([func[j]]) / (len(popu) + 0.01)
            ae[i][j] = ae[i][j] + r
            be[i][j] = be[i][j] + R - r
    return ai,bi,ae,be


def popability(r):
    a = random.random()
    if a < r:
        return True
    else:
        return False