#!/usr/bin/env python

from sys import argv

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == '__main__':
    n = int(argv[1])
    print 'factorial(' + argv[1] + ') =', factorial(n)
