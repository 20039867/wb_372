# -*- coding: utf-8 -*-

import numpy as np
import math
from cspline import eval_spline
from cspline import curvatures
from neville import neville
from poly_fit import poly_fit
from poly_fit import stdDev
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.optimize import bisect
from secant import secant

"""
(a) Use the natural cubic spline to determine y at x = 1.5. The data points are as follows:
    x | 1 2 3 4 5
    y | 0 1 0 1 0
"""

def a():
    xdata = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    ydata = np.array([0.0, 1.0, 0.0, 1.0, 0.0])
    k = curvatures(xdata, ydata)

    print "\n"
    print "A: y == " + str(eval_spline(xdata, ydata, k, 1.5)) + "\n  x == 1.5"
    print "\n"

    """Plot"""
    x1 = [1, 5]
    y1 = [eval_spline(xdata, ydata, k, 1.5), eval_spline(xdata, ydata, k, 1.5)]
    x11 = [1.5, 1.5]
    y11 = [0, 1]
    xapprox = np.linspace(1,5,100)
    yapprox = np.zeros(100)
    for i in range(len(xapprox)):
        yapprox[i] += eval_spline(xdata, ydata, k, xapprox[i])

    plt.title('A')
    plt.plot(x1, y1,"g-",x11, y11, "g-", xdata,ydata,"r.-",xapprox,yapprox,"b-")
    plt.show()


"""
(b) Find the zero of y(x) from the following data:
**********CHANGING THE X AND Y seems like a mistake**********
    x |1.8421 2.4694 2.4921 1.9047  0.8509  −0.4112  −1.5727
    y |0      0.5    1      1.5     2       2.5      3

    Where does y(x) == 0?
"""
def b():
    xdata = np.array([0.0,      0.5,    1.0,    1.5,    2,      2.5,    3.0])
    ydata = np.array([1.8421, 2.4694, 2.4921, 1.9047, 0.8509, -0.4112, -1.5727])
    a = poly_fit(xdata,ydata,2)

    def f(x):
        return a[0] + a[1]*x + a[2]*(x**2)

    point = bisect(f, 2, 2.5)
    print "B: Where x == " + str(point)
    """Plot"""
    x1  = [0,3 ]
    y1  = [0,0 ]
    x11 = [point, point]
    y11 = [-2, 3]

    plt.title('B')
    xapprox = np.linspace(0, 3.0, 100)
    yapprox = np.zeros(100)

    for i in range(len(xapprox)):
        yapprox[i] += a[0] + a[1]*xapprox[i] + a[2]*(xapprox[i]**2)

    plt.plot(x1, y1, "g-",x11,y11, "g-", xdata,ydata,"r.-", xapprox,yapprox, "b-")
    plt.show()

"""
(c) Use Neville’s method to compute y at x = π/4 from the following data points:
    x | 0.0       0.5      1.0       1.5      2.0
    y | −1.00   1.75     4.00    5.75     7.00
"""
def c():
    xdata = np.array([0.0, 0.5, 1.0, 1.5, 2.0])
    ydata = np.array([-1.0, 1.75, 4.0, 5.57, 7.0])
    print "C: " + str(neville(xdata, ydata, (math.pi/4)))
    print "\n"

"""
(d) Given the the following data, find y at x = π/4 and x = π/2. Use the method that you consider to
be most convenient.

    x | 0        0.5    1      1.5    2
    y | −0.7854  0.6529 1.7390 2.2071 1.9425
"""
def d():
    xdata = np.array([0.0, 0.5, 1.0, 1.5, 2.0])
    ydata = np.array([-0.7854, 0.6529, 1.7390, 2.2071, 1.9425])
    print "D1: X: " + str(math.pi/4) + "Y: "+ str(neville(xdata, ydata, (math.pi/4)))
    print "D2: X: " + str(math.pi/2) + "Y: " + str(neville(xdata, ydata, (math.pi/2)))
    print "\n"

    """Plot"""
    plt.title('D')

    xapprox = np.linspace(0,2,10)
    yapprox = np.zeros(10)

    for i in range(len(xapprox)):
        yapprox[i] += neville(xdata, ydata, xapprox[i])

    plt.plot(xdata,ydata,"r.-",xapprox,yapprox,"b-")
    plt.show()

"""
(e) The table shows the drag coefficient cD of a sphere as a function of the Reynolds number Re. Use
the natural cubic spline to find cD at Re = 5, 50, 500, and 5000. Hint: Use the log-log scale.
    Re | 0.2    2      20      200     2000    20000
    cD | 103    13.9   2.72    0.800   0.401   0.433
"""
def e():
    xdata = np.array([0.2, 2.0, 20.0, 200.0, 2000.0, 20000.0])
    ydata = np.array([103.0, 13.9, 2.72, 0.800, 0.401, 0.433])
    a = poly_fit(xdata,ydata,2)

    def f(x):
        return a[0] + a[1]*x + a[2]*(x**2)


    print "E1: " + str(neville(xdata, ydata, f(5)))
    print "E2: " + str(neville(xdata, ydata, f(50)))
    print "E3: " + str(neville(xdata, ydata, f(500)))
    print "E4: " + str(neville(xdata, ydata, f(5000)))
    print "INCORRECT\n"

    """Plot"""
    yapprox = np.zeros(100)
    ysapprox =  np.zeros(100)
    plt.title('E')
    xapprox = np.linspace(0.2,20000,100)
    for i in range(len(xapprox)):
        yapprox[i] = f(xapprox[i])

    plt.plot(xdata,ydata,"r.-",xapprox,yapprox,"b-")
    plt.show()

"""
(a) Fit a straight line to the following data, and compute the standard deviation.
    x | 0.0 1.0 2.0 2.5 3.0
    y | 2.9 3.7 4.1 4.4 5.0
"""
def a2():
    xdata = np.array([0.0, 1.0, 2.0, 2.5, 3.0])
    ydata = np.array([2.9, 3.7, 4.1, 4.4, 5.0])
    a = poly_fit(xdata,ydata,1)

    print "A2: " + str(stdDev(a, xdata, ydata))

    """Plot"""
    plt.title('A2')
    xapprox = np.linspace(0,3,10)
    yapprox = np.zeros(10)

    for i in range(len(xapprox)):
        yapprox[i] += a[0] + a[1] * xapprox[i]

    plt.plot(xdata,ydata,"ro",xapprox,yapprox,"b-")
    plt.show()

"""
(b) The relative density ρ of air was measured at various altitudes h (in km). The results are:
    h | 0   1.525   3.050   4.575   6.10    7.625   9.150
    ρ | 1   0.8617  0.7385  0.6292  0.5328  0.4481  0.3741
    Use a quadratic least-squares fit to determine the relative air density at h = 10.5 km.
"""
def b2():
    xdata = np.array([0.0, 1.525, 3.050, 4.575, 6.10, 7.625, 9.150])
    ydata = np.array([1.0, 0.8617, 0.7385, 0.6292, 0.5328, 0.4481, 0.3741])
    a = poly_fit(xdata,ydata,2)

    print "B2: " + str(a[0] + a[1] * 10.5 + a[2]*(10.5**2))

    """Plot"""
    plt.title('B2')
    xapprox = np.linspace(0,10,10)
    yapprox = np.zeros(10)

    for i in range(len(xapprox)):
        yapprox[i] += a[0] + a[1] * xapprox[i] + a[2]*(xapprox[i]**2)

    plt.plot(xdata,ydata,"ro",xapprox,yapprox,"b-")
    plt.show()

"""
(c) Fit a straight line and quadratic to the follow data.
 x | 1.0    2.5     3.5     4.0     1.1     1.8     2.2     3.7
 y | 6.008  15.722  27.130  33.772  5.257   9.549   11.098  28.828
"""
def c2():
    xdata = np.array([1.0, 2.5, 3.5, 4.0, 1.1, 1.8, 2.2, 3.7])
    ydata = np.array([6.008, 15.722, 27.130, 33.772, 5.257, 9.549, 11.098, 28.828])
    a = poly_fit(xdata,ydata,2)

    ar = np.polyfit(xdata,ydata, 1)
    print ar[1]
    print ar[0]
    def f(x):
        return ar[1] + ar[0]*x #ar[1] = a   ar[0]=b so a + bx

    """Plot"""
    plt.title('C2')

    xapprox = np.linspace(0,5,10)
    yapprox = np.zeros(10)
    yyapprox = np.zeros(10)
    for i in range(len(xapprox)):
        yapprox[i] = a[0] + a[1] * xapprox[i] + a[2]*(xapprox[i]**2)
        yyapprox[i] = f(xapprox[i])
    plt.plot(xdata,ydata,"ro",xapprox,yapprox,"b-", xapprox, yyapprox, "y-")
    plt.show()

def d2():
    pass

if __name__ == "__main__":
    a()
    b()
    c()
    d()
    e()
    a2()
    b2()
    c2()
    d2()
