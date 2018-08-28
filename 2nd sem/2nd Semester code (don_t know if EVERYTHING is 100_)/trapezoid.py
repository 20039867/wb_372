def trapezoid(f, a, b, Iold, k):
	'''Compute the integral of f(x) from a to b with the recursive trapezoidal
	rule for 2**k panels, using the integral of f(x) from a to b computer for
	2**(k - 1) panels.

	Arguments:
		f -- the integrand ( a function)
		a -- the lower limit
		b -- the upper limit
		Iold -- the integral of f(x) from a to b computed by the trapezoidal rule
		with 2**(k - 1) panels
		k -- panel parameter'''

	if k == 1:
		Inew = (f(a) + f(b)) * (b - a) / 2.0
	else:
		n = 2**(k - 2)	# number of points
		h = (b - a) / n	# spacing of the new points
		x = a + h/2.0
		s = 0.0
		for i in xrange(n):
			s += f(x)
			x += h
		Inew = (Iold + h * s) / 2.0

	return Inew
