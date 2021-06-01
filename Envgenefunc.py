import numpy as np
import scipy.stats
from dppy.finite_dpps import FiniteDPP

# Simulation window parameters
xMin = -0.5
xMax =   0.5
yMin =  -0.5
yMax =  0.5
xDelta = xMax - xMin;
yDelta = yMax - yMin;  # rectangle dimensions
areaTotal = xDelta * yDelta;


def PPP(lambda0):
    # numbPoints = scipy.stats.poisson(lambda0 * areaTotal).rvs()
    numbPoints = lambda0
    xx = xDelta * scipy.stats.uniform.rvs(0, 1, ((numbPoints, 1))) + xMin  # x coordinates of Poisson points
    yy = yDelta * scipy.stats.uniform.rvs(0, 1, ((numbPoints, 1))) + yMin  # y coordinates of Poisson points
    return xx,yy


def dpp(N,r,k):
        rng = np.random.RandomState()

        # Random feature vectors
        Phi = rng.randn(r, N)
        DPP = FiniteDPP('likelihood', **{'L': Phi.T.dot(Phi)})

        for _ in range(N):
            DPP.sample_exact_k_dpp(size=k, random_state=rng)
        result = DPP.list_of_samples
        for i in range(len(result)):
            result[i][0] = (result[i][0]/50)-0.5
            result[i][1] = (result[i][1]/50)-0.5
        return result