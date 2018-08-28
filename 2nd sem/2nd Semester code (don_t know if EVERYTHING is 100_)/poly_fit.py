from numpy import zeros
from numpy.linalg import solve
from math import sqrt

def poly_fit(xdata, ydata, m):
	'''Compute and return the coefficients of the polynomial \
	p(x) = c[0] + c[1]x + c[2]x**2 + ... + c[m]x**m \
	that fits the specified data in the least-squares sense.'''
	
	A = zeros((m+1, m+1))
	b = zeros(m+1)
	s = zeros(2*m + 1)
	for i in xrange(len(xdata)):
		temp = ydata[i]
		for j in xrange(m+1):
			b[j] = b[j] + temp
			temp = temp * xdata[i]
		temp = 1.0
		for j in xrange(2*m + 1):
			s[j] = s[j] + temp
			temp = temp * xdata[i]
	
	for i in xrange(m + 1):
		for j in xrange(m + 1):
			A[i,j] = s[i+j]

	return solve(A, b)

def eval_poly(c, x):
	m = len(c) - 1
	p = c[m]
	for j in xrange(m):
		p = p*x + c[m-j-1]
	return p

def std_dev(c, xdata, ydata):
	'''Computer the standard deviation between p(c) and the	data.'''
	
	n = len(xdata) - 1
	m = len(c) - 1
	sigma = 0.0
	for i in xrange(n+1):
		p = eval_poly(c, xdata[i])
		sigma += (ydata[i] - p) ** 2
	sigma = sqrt(sigma / (n-m))
	return sigma
