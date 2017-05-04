# -*- coding: utf-8 -*-
"""
Created on Mon May  1 15:37:10 2017

@author: Christoffer Arnlund & Oskar Friberg
"""

from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as op

x=np.arange(0, 3.5,0.5)
y=[70,70,55,22,13,10,10]
cs = CubicSpline(x, y,bc_type='clamped')
thermocline=op.fsolve(cs, 1, args=2)

print("The thermocline depth is:",thermocline.item(0),"m.")

xs = np.arange(0,4, 0.01)

def fluxFunc(x):
     
        return -1*cs(x,1)

flux=fluxFunc(thermocline)
print("The flux at",thermocline.item(0),"m is ",flux.item(0))
plt.figure()
plt.plot(x, y, 'o', label='data')

plt.plot(xs, cs(xs), label="C (℃/m)")

plt.plot(xs, cs(xs, 1), label="C'")

plt.plot(xs, cs(xs, 2), label="C''")

plt.legend()
plt.figure()
plt.plot(xs,-1*cs(xs,1), label=r"J $ \left( \frac{cal}{m^2s}\right)$")
plt.legend()

#plt.plot(x, f(x), label="S'")
plt.show()

tempat17=cs(1.7)
depthat50= cs.solve(50)

print("Depth at 50 degrees is ",depthat50.item(0), "m")
print("Temperature at 1.7 m is ",tempat17.item(0))
