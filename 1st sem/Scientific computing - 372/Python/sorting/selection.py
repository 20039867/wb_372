#!/usr/bin/env python

from random import shuffle
from sys import argv

N = 0

def sort(L, debug=False):
    """Sort the list L into ascending order according to the natural order of
    the list elements."""

    if debug: print L
    for i in xrange(len(L)):
        m = findmin(L, i)
        L[i], L[m] = L[m], L[i]
        if debug: print L

def findmin(L, i):
    """Return the index of the minimum element in the list slice L[i:]."""
    
    global N
    m = i
    for j in xrange(i + 1, len(L)):
        N = N + 1
        if L[j] < L[m]:
            m = j
    return m

def test_sort(debug, *args):
    global N
    for L in args:
        N = 0
        print 'L =', L
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

