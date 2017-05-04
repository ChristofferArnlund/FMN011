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

x=np.arange(0, 3.5,0.5)
y=[70,70,55,22,13,10,10]
cs = CubicSpline(x, y,bc_type='clamped')
thermocline=op.fsolve(cs, 1, args=2)
print("thermocline:",thermocline)
xs = np.arange(0,4, 0.01)

f = interp1d(x, y)
#f2 = interp1d(x, y, kind='cubic')

def fluxFunc(x):
     
        return -1*cs(x,1)

flux=fluxFunc(thermocline)
print("Task 2 flux: ",flux.item(0))
plt.figure()
plt.plot(x, y, 'o', label='data')
plt.plot(xs, cs(xs), label="C (℃/m)")
#plt.figure()
plt.plot(xs, cs(xs, 1), label="C'")
#plt.figure()
plt.plot(xs, cs(xs, 2), label="C''")
plt.legend()
plt.figure()
plt.plot(xs,-1*cs(xs,1), label="J")
plt.legend()

#plt.plot(x, f(x), label="S'")
plt.show()

tempat17=cs(1.7)
depthat50= cs.solve(50)
print("depthat50",depthat50)
print("temp at 1.7m ",tempat17)
#print(cs)
#print(x)