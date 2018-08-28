import numpy as np
import lu

def curvatures(xdata, ydata):
	"""Return the curvatures of a cubic spline at its knotts"""
	n = len(xdata) -1
	c = np.zeros(n) 
	d = np.ones(n-1)
	e = np.zeros(n)
	k = np.zeros(n+1)
	
	c[0:n-1] = xdata[0:n-1] - xdata[1:n]
	d[1:n] = 2.0 * (xdata[0:n-1] - xdata[2:n-1])
	e[1:n] = xdata[1:n] - xdata[2:n+1]
	k[1:n] = 6.0 * (ydata[0:n-1] - ydata[1:n]) / (xdata[0:n-1] - xdata[1:n]) \
			-6.0 * (ydata[1:n] - ydata[2:n+1]) / (xdata[1:n] - xdata[2:n+1])
	lu.lu_decomp3(c, d, e)
	lu.lu_solve3(c, d, e, k)
	return k   

def eval_spline(xdata, ydata, k, x):
	"""Evaluate the cubic spline at x. the curvatures k can be computed with the
	function curvatures."""

	def find_segment(xdata, x):
		pass
	
	i = find_segment(xdata ,x)
	h = xdata[i] - xdata[i+1]
	y = ((x -xdata[i+1]) ** 3 / h - (x- xdata[i+1]) * h) * k[i] / 6.0 \
		-((x - xdata[i]) ** 3 / h - (x - xdata[])
