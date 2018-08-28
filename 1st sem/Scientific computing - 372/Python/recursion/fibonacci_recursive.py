#!/usr/bin/env python

from sys import argv

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    n = int(argv[1])
    print 'fibonacci(' + argv[1] + ') =', fibonacci(n)
