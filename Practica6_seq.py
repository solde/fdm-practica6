import sympy as sym
import numpy as np
import math
import matplotlib.pyplot as plt

sym.init_printing(use_unicode=True)

x = sym.Symbol('x', nonzero=True, real=True )
n = sym.Symbol('n', nonzero=True)

# Constants
h = 6.62607004 * 10**-34
m = 9.10938356 * 10**-31
a = 1 
k = 9.9 * 10**-21
w = math.sqrt(k/m)
q = 1.602177 * 10**-19

Y = np.empty(4, dtype=sym.core.mul.Mul)

# Wave equations
Y[0] = sym.simplify((a/(np.pi)**1/2)**1/2*np.e**((-a**2*x**2)/2))
Y[1] = sym.simplify(((a/(2*((np.pi)**1/2)))**1/2)*2*x*a*np.e**((-a**2*x**2)/2))
Y[2] = sym.simplify((a/(8*((np.pi)**1/2)))**1/2*((4*a**2*x**2)-2)*np.e**((-a**2*x**2)/2))
Y[3] = sym.simplify((a/(48*((np.pi)**1/2)))**1/2*(8*a**3*x**3-12*a*x)*np.e**((-a**2*x**2)/2))

# Gràfica de l'energia
print("Calcul de la gràfica de l'energia")

Ej = []
Eev = []
n = []
aux = input("Entre el valor de n pel que vulguis calcular l'energia (escriu stop per acabar): ")

while aux != "stop":
    n.append(float(aux))

    Ej.append((n[-1]+0.5)*(h/(2*np.pi))*w)
    Eev.append(Ej[-1]/q)
    
    print("Per la n " + str(n[-1]) + " la seva energia és " + str(Ej[-1]) + "J o " + str(Eev[-1]) + "eV.")

    aux = input("Entre el valor de n pel que vulguis calcular l'energia (escriu stop per acabar): ")

plt.plot(n, Eev, 'o')
plt.title("Energia")
plt.xlabel("n")
plt.ylabel("Energia (eV)")
plt.draw()
plt.savefig("Energia.png")
plt.clf()

# Gràfica de la funció d'ona

min = -1
max = 1
interval = 0.01
plotRange = np.arange(min, max, interval)

P = np.empty([4, plotRange.shape[0]])

print("Calculant l'ona")

it = 0
for j in plotRange:
    for i in range(0, 4):
        P[i, it] = Y[i].subs(x, j)
    it += 1

print("Generant les gràfiques de la funció d'ona")

for j in range(0, 4):
    plt.plot(plotRange, P[j])
    plt.title("Funció d'ona Ψ" + str(j))
    plt.xlabel("Posició (m)")
    plt.ylabel("Valor de l'Energia (J)")
    plt.draw()
    plt.savefig("OnaN"+str(j)+".png")
    plt.clf()

# Densitat de probabilitat

min = -1
max = 1
interval = 0.01
plotRange = np.arange(min, max, interval)

P = np.empty([4, plotRange.shape[0]])

print("Calculant la probabilitat")

it = 0
for j in plotRange:
    for i in range(0, 4):
        P[i, it] = (Y[i].subs(x, j))**2
    it += 1

print("Generant les grafiques")

for j in range(0, 4):
    plt.plot(plotRange, P[j])
    plt.title("Probabilitat de la Ψ" + str(j))
    plt.xlabel("Posició (m)")
    plt.ylabel("Probabilitat (%)")
    plt.draw()
    plt.savefig("DPOnaN"+str(j)+".png")
    plt.clf()

# Probabilitat

aux = input("Entra la n(1-4) (excriu stop per acabar): ")

while aux != "stop":

    nwave = int(aux)-1
    a = float(input("Posició x0: "))
    b = float(input("Posició x1: "))

    Y2 = sym.parse_expr(str( sym.simplify( Y[nwave] ) )+"*"+str( sym.simplify( ( Y[nwave] ) ) ))
    Y2 = sym.simplify(Y2)
    #Y1 = (a/((np.pi)**(1/2)))**(1/2)*(np.e)**((-a**(2)*x**(2))/2)
    
    #Y2 = sym.Pow(Y[nwave], 2)
    iY2 = sym.integrate(Y[nwave], (x, a ,b))
    iY2 = sym.simplify(iY2)
    iY2d = iY2.doit()
    iY2v = iY2d.evalf()
    print("La probabilitat de trobar la particula en X0 = " + str(a) + " i el punt X1 " + str(b) + " amb n = " + str(nwave+1) + " és " + str(iY2v*100) + "%.")
    aux = input("Entra la n(1-4): ")
