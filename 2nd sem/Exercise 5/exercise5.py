# -*- coding: utf-8 -*-
from trapezoid import trapezoid
from scipy.integrate import quad
import math
import numpy as np


def a():
    pass
def b():
    pass
def c():
    pass

"""
2. For parts (a) to (c), also solve the integrals by using Scientific Python. In particular, consider how to
to use scipy.integrate.quad.
(a) Determine
                |       dx        |
    INTGERATE   |_________________|
    1 -> infi   |     1 + x^4     |

    with the trapezoidal rule using five panels and compare the result with the “exact” integral 0.24375.
    Hint: Use the transformation x = 1/t.

"""


def a2():
    def f(x):
        return 1/(1 + x**4)

    print quad(f, 1, np.inf)


def b2():
    pass

def c2():
    pass

def d2():
    pass

def e2():
    pass

if __name__ == "__main__":
    a()
    b()
    c()
    a2()
    b2()
    c2()
    d2()
    e2()
