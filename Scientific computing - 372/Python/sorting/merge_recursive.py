#!/usr/bin/env python

from random import shuffle
from sys import argv

N = 0

def sort(L, debug=False):
    """Sort the list L into ascending order according to the natural order of
    the list elements."""

    if len(L) <= 1:
        return

    if debug: print L

    middle = len(L) / 2
    left = L[:middle]
    right = L[middle:]
    sort(left, debug)
    sort(right, debug)
    
    if debug:
        print 'left  =', left
        print 'right =', right
    
    L[:] = merge(left, right)


def merge(L1, L2):
    """Return a merged list for the sorted lists L1 and L2."""

    global N

    LS = []
    i1 = i2 = 0
    while i1 < len(L1) and i2 < len(L2):
        N = N + 1
        if L1[i1] <= L2[i2]:
            LS.append(L1[i1])
            i1 = i1 + 1
        else: # L1[i2] > L2[i2]
            LS.append(L2[i2])
            i2 = i2 + 1

    LS.extend(L1[i1:])
    LS.extend(L2[i2:])

    return LS

def test_sort(debug, *args):
    global N
    for L in args:
        print 'L =', L
        N = 0
        sort(L, debug)
        print 'L =', L
        print N, 'iterations'
        print

if __name__ == '__main__':
    L1 = range(1, int(argv[1]) + 1)
    L2 = L1[:]
    shuffle(L2)
    L3 = L1[:]
    L3.reverse()

    test_sort(eval(argv[2]), L1, L2, L3)

