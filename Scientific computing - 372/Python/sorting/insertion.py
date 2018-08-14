#!/usr/bin/env python

from random import shuffle
from sys import argv

N = 0

def sort(L, debug=False):
    """Sort the list L into ascending order according to the natural order of
    the list elements."""

    if debug: print L
    for i in xrange(1, len(L)):
        insert(L, i)
        if debug: print L

def insert(L, i):
    """Insert the element at index i into its proper place in L[:i]."""

    global N
    j = i
    while j > 0 and L[j-1] > L[j]:
        N = N + 1
        L[j], L[j-1] = L[j-1], L[j]
        j = j - 1

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

