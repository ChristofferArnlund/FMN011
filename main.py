# -*- coding: utf-8 -*-
"""
Created on Mon May  1 15:37:10 2017

@author: Christoffer Arnlund & Oskar Friberg
"""

from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import numpy

x=numpy.arange(0, 3.5, 0.5)
y=[70,70,55,22,13,10,10]
cs = CubicSpline(x, y,bc_type='clamped')
plt.figure()
plt.plot(x, y, 'o', label='data')
plt.plot(x, cs(x), label="S")
#plt.plot(x, cs(x, 1), label="S'")
print(x)