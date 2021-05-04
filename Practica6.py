from sympy import *
import numpy as np
import math

x = Symbol('x')

# Constants
h = 6.62607004 * 10**-34
m = 9.10938356 * 10**-31
a = 1 
k = 9.9 * 10**-21
w = 3.1 * 10**5

# Wave equations
Y0 = (a/np.pi**1/2)**1/2*np.e**((-a**2*x**2)/2)
Y1 = (a/np.pi**1/2)**1/2*2*a*np.e**((-a**2*x**2)/2)
Y2 = (a/np.pi**1/2)**1/2*(4*a**2*x**2-2)*np.e**((-a**2*x**2)/2)
Y3 = (a/np.pi**1/2)**1/2*(8*a**3*x**3-12*a*x)*np.e**((-a**2*x**2)/2)

print(diff(Y0, x))
print(diff(Y1, x))
print(diff(Y2, x))
print(diff(Y3, x))