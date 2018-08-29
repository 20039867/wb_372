'''A module for LU decomposition of matrices'''

def lu_decomp3(c,d,e):
	n = len(d)
	for k in xrange(1,n):
		lam = c[k-1] / d[k-1]
		d[k] = d[k] - lam * e[k-1]
		c[k-1] = lam
	return c, d, e

def lu_solve3(c,d,e,b):
	n = len(d)
	for k in xrange(1,n):
		b[k] = b[k] - c[k-1] * b[k-1]
	b[n-1] = b[n-1] / d[n-1]
	for k in xrange(n-2,-1,-1):
		b[k] = (b[k] - e[k] * b[k+1]) / d[k]
	return b
