from scipy import interpolate as interp
import numpy as np
from math import pi
x = np.array([0,0.5,1,1.5,2])
y = np.array([-1.0,1.75,4.,5.75,7.])

def eval_poly(a, xs, x):
    n = len(xs) - 1
    p = a[n]
    for k in range(1, n+1):
        p = a[n-k] + (x - xs[n-k])*p
    return p

def coefficients(xs,ys):
    m = len(xs)
    xs = np.copy(xs)
    a = ys.copy()
    for k in range(1, m):
        a[k:m] = (a[k:m] - a[k-1])/(xs[k:m] - xs[k-1])
    return a

if __name__ == "__main__":
    a = coefficients(x,y)
    print(eval_poly(a, x, pi/4))

