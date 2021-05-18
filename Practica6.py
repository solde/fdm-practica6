import sympy as sym
import numpy as np
import math
import matplotlib.pyplot as plt
import threading

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
Y[0] = (a/(np.pi)**1/2)**1/2*np.e**((-a**2*x**2)/2)
Y[1] = ((a/(2*((np.pi)**1/2)))**1/2)*2*x*a*np.e**((-a**2*x**2)/2)
Y[2] = (a/(8*((np.pi)**1/2)))**1/2*((4*a**2*x**2)-2)*np.e**((-a**2*x**2)/2)
Y[3] = (a/(48*((np.pi)**1/2)))**1/2*(8*a**3*x**3-12*a*x)*np.e**((-a**2*x**2)/2)

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

# Probabilitat
def prob(int i):
    print("Calcul de la probabilitat")

    min = -1
    max = 1
    interval = 0.001
    plotRange = np.arange(min, max, interval)

    P = np.empty([4, int((max-min)/interval)])

    it = 0
    for j in plotRange:
        aux = d2Y[i].subs(x, it)
        P[i, it] = aux**2
        it += 1

    print("Generant els .csv")


    count = min
    f = open("Ona"+str(j+1)+".csv", "w")
    for j in P[i]:
        f.write(str(count) + ", " + str(j) + "\n")
        count += interval
    f.close()

    print("Generant els plots")

    plt.plot(plotRange, P[i])
    plt.title("Probabilitat de la Ψ" + str(j+1))
    plt.xlabel("Posició (m)")
    plt.ylabel("Probabilitat (%)")
    plt.draw()
    plt.savefig("Grafic"+str(i+1)+".png")

for i in range(0,4):
    thr = threading.Thread(target=prob, args=(i))
    thr.start()
    