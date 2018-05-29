# PROGRAMA 8
# -*- coding: utf-8 -*-

from math import fabs, exp
from scipy.interpolate import lagrange
from scipy.integrate import quad
from decimal import *

a = 0.0
b = 1.0
n = 10
k = 4

# Función f de dos variables
f = lambda t,y: (2-2*t*y)/(1+pow(t,2))

# Solución exacta
sol_exacta = False
y = lambda t: (2*t+1)/(pow(t,2)+1)
y_0 = 1

# Lista con las aproximaciones u_{0},..,u_{k-1}
# (en caso de no tener la solución exacta) 
inicial = []

h = (b - a) / n
t = [a + j * h for j in range(n + 1)]
u = [0 for i in range(n + 1)] # Lista "vacía" con n+1 posiciones

def integrate_interpolation_polynomial(j):
	x = []
	y = []
	for i in range(k):
		x.append(t[j-i])
		y.append(f(x[i], u[j-i]))

	poly = lagrange(x,y)
	return quad(poly, t[j], t[j+1])[0]
	
def adams_bashforth(j):
	if j < k:
		return u[j]
		
	u_j = adams_bashforth(j-1) + integrate_interpolation_polynomial(j-1)
	u[j] = u_j
	return u_j

def euler(f,a,b,n ,y_0):
    h=Decimal((b-a))/Decimal(n)
    inicial[0] =y_0  
    for i in range (0, n-1):
        tj =Decimal(a+(i+1)*h)
        x = inicial[i] + h*f(tj,Decimal(inicial[i]))
        inicial[i+1] = x




"""
Main
"""
euler(f,0,1,10,y_0)


if sol_exacta:
	for i in range(k):
		u[i] = y(t[i])
else:
	for i in range(k):
		u[i] = inicial[i]

adams_bashforth(n)
print("Las", n, "aproximaciones son: ")
for item in u:
    print(item)
if sol_exacta:
    print("Los errores son: ")
    for j in range(n + 1):
        print(fabs(u[j] - y(t[j])))
