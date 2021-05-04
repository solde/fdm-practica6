import sympy as sym
import numpy as np
import math
import matplotlib.pyplot as plt

x = sym.Symbol('x')
n = sym.Symbol('n')

# Constants
h = 6.62607004 * 10**-34
m = 9.10938356 * 10**-31
a = 1 
k = 9.9 * 10**-21
w = 3.1 * 10**5

Y = np.empty(4, dtype=sym.core.mul.Mul)
d2Y = np.empty(4, dtype=sym.core.mul.Mul)

# Wave equations
Y[0] = (a/np.pi**1/2)**1/2*np.e**((-a**2*x**2)/2)
Y[1] = (a/np.pi**1/2)**1/2*2*a*np.e**((-a**2*x**2)/2)
Y[2] = (a/np.pi**1/2)**1/2*(4*a**2*x**2-2)*np.e**((-a**2*x**2)/2)
Y[3] = (a/np.pi**1/2)**1/2*(8*a**3*x**3-12*a*x)*np.e**((-a**2*x**2)/2)

d2Y[0] = sym.diff(sym.diff(Y[0], x) , x)
d2Y[1] = sym.diff(sym.diff(Y[1], x) , x)
d2Y[2] = sym.diff(sym.diff(Y[2], x) , x)
d2Y[3] = sym.diff(sym.diff(Y[3], x) , x)

# Gràfica de l'energia
print("Calcul de la gràfica de l'energia")

print("Entrar el nombre de n que es volen calcular: ")
iterations = int(input()) # number of energies that will be calculated

for i in range(0, iterations):
    n = float(input())

    En = (n+0.5)*(h/(2*np.pi))*w

# Provabilitat

P = np.empty([4, 20])

for j in range(-10, 10):
    for i in range(0, 4):
        P[i, j] = d2Y[i].subs(x, j)
        P[i, j] = P[i, j]**2
