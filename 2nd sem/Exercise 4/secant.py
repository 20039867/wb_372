def secant(f, a, b, tol=1e-9, n = 100):
	fmt = '{:2} {:>13.10f} {:>13.10f} {:>13.10f}'
	p1, p2 = float(a), float(b)
	i = 1
	print fmt.format(1,p1,p2,f(p2))
	
	while abs(p1-p2)>tol and i <=n:
		p1, p2 = p2, p2 - (f(p2)*(p2-p1))/(f(p2)-f(p1))
		i += 1
		print fmt.format(1,p1,p2, f(p2))
	
	return p2

def f(x):
	return x**3 + 4*x**2 - 10

if __name__ == '__main__':
	r1 = secant(f, 1, 2)
	print 'root = {:.10f}'.format(r1)
