#!/usr/bin/env python

from sys import argv

def factorial(n):
    f = 1
    for i in xrange(1, n + 1):
        f = f * i
    return f

if __name__ == '__main__':
    n = int(argv[1])
    print 'factorial(' + argv[1] + ') =', factorial(n)
