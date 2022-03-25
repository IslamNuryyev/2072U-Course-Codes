import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x = np.linspace(0, 10, 11) # x values of points for which we will plot the interpolant
y = np.cos(-x**2/9.0)

f = interp1d(x, y)

xx = np.linspace(0, 10, 100)
yy = f(xx) #interpolation

plt.plot(x, y, 'o', xx, yy, '-r')
plt.show()




