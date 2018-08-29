import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy import stats

def draw():
	xdata = np.array([0.0,1.0,2.0,2.5,3.0])
	ydata = np.array([2.9,3.7,4.1,4.4,5.0])

	f1 = interp1d(xdata,ydata)
	f2 = interp1d(xdata,ydata,kind='cubic')
	slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

	xplot = np.linspace(0., 3., 40)

	fig, ax = plt.subplots()
	ax.plot(xdata,ydata,"ro",xplot, f1(xplot), "b-", \
		xplot, f2(xplot),"g-", xplot, slope * xplot + intercept, "b-")
	ax.set_aspect("equal")
	ax.grid(True,which="both")
	ax.axhline(y=0,color="k")
	ax.axvline(x=0,color="k")
	ax.set_xlim((-1,6))
	ax.set_ylim((-1,6))

	plt.show()


if __name__ == "__main__":
	draw()
