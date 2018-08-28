#!/usr/bin/env python

from sys import argv

def fibonacci(n):
    a, b = 0, 1
    for i in xrange(n):
        a, b = b, a + b
    return a

if __name__ == '__main__':
    n = int(argv[1])
    print 'fibonacci(' + argv[1] + ') =', fibonacci(n)
