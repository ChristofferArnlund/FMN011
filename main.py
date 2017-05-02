# -*- coding: utf-8 -*-
"""
Created on Mon May  1 15:37:10 2017

@author: Christoffer Arnlund & Oskar Friberg
"""

from scipy.interpolate import CubicSpline
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as op

x=np.arange(0, 301, 50)
y=[70,70,55,22,13,10,10]
cs = CubicSpline(x, y,bc_type='clamped')

xs = np.arange(-50, 450, 0.1)

f = interp1d(x, y)
#f2 = interp1d(x, y, kind='cubic')

plt.figure()
plt.plot(x, y, 'o', label='data')
plt.plot(xs, cs(xs), label="S'")
plt.figure()
plt.plot(xs,-0.001*cs(xs,1), label="J")
plt.figure()
plt.plot(xs, cs(xs, 1), label="S'")
plt.figure()
plt.plot(xs, cs(xs, 2), label="S''")
#plt.plot(xs, cs(xs, 3), label="S'''")
#plt.ylim(-100, 100)


#plt.plot(x, f(x), label="S'")
plt.show()
res= cs.solve(50)
print(res)
print(cs)
print(x)