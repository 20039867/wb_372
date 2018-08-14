import scipy.optimize

def newton(f, fprime, p, tol=1e-9, n=100):
	fmt = '{:2} {:>13.10f} {:>13.10f}'
	i = 1
	while abs(0-f(p)) > tol and i <= n:
		p = p - f(p)/fprime(p)
		print fmt.format(1,p,f(p))
		i += 1
	return p

def f(x):
	return float(x**3 + 4*x**2 - 10)

def fprime(x):
	return float(3*x**2 + 8*x)

if __name__ == '__main__':
	r1 = newton(f, fprime, 1)
	r2 = scipy.optimize.newton(f, 1,fprime=fprime, tol=1e-9)
	print(r1)
	print(r2)
