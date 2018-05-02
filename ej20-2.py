# -*- coding: utf-8 -*-

import scipy as sp
import numpy as np
from numpy.polynomial import polynomial as P
import math
import scipy.integrate as integrate
import scipy.special as special

def rk0( f, a, b, n ):
     if(n==1):
          resultado = (f(b) + f(a))*(b-a)/2
     else:
     	  # Calculamos la separación entre nodos
          h = (b-a)/n
          # Calculamos los nodos para interpolar
          x=[ a+h*i for i in range(n+1)]
          fx = 0
          for i in range(n-1):
          	fx = fx + f(x[i+1])
          resultado = ( h *( ( f(x[0]) + f(x[n]) )/2 + fx ) ) 
     return resultado

def intPuntoMedio(f,a,b):
    return f((a+b)/2)*(b-a)

def rk( Rk, Rk1, j ):
     return Rk + (1/(4**j-1))*(Rk - Rk1)

#Rk = R_{k,j-1} RK1 = R_{k-1,j-1}
def metodoRomberg(f, a, b, k):
		resultados=[]
		resultados.append( rk0( f, a, b, 1 ) )
		for i in range(k):
			resultados.append( rk0( f, a, b, 2**(i+1) ) )
		for i in range(k):
			for j in range(k-i):
		    		resultados[j]=rk( resultados[j+1], resultados[j], i+1 )
		return resultados[0]

#Apartado c)
f = lambda x: 3*x/(x**2 - 4)
a=1
b=1.8
n = 0
diferencia = 1
integral = integrate.quad(f,a,b)
trapecio = rk0(f,a,b,1)
simpson = rk0(f,a,b,2)
medio = intPuntoMedio(f,a,b)

print("Función x^3*e^(-x)\n")

while diferencia >= 10**(-6):
    Rk = metodoRomberg(f, a, b, n)
    Rk1 = metodoRomberg(f, a, b, n+1)
    print("R{0},{0} =".format(n), Rk )
    print("R{0},{0} =".format(n+1), Rk1 )
    diferencia = abs(Rk-Rk1)
    print("|R{0},{0}-R{1},{1}| =".format(n, n+1), diferencia)
    print("\n")
    cont = n+1
print("Su integral real es:",integral)
print("Su valor por el trapecio es:", trapecio)
print("Su valor por simpson es:", simpson)
print("Su valor por el punto medio es:", medio)



# Apartado d)
f = lambda x: math.cos(x)*math.exp(3*x)
a=0
b=math.pi
n = 0
diferencia = 1
integral = integrate.quad(f,a,b)
trapecio = rk0(f,a,b,1)
simpson = rk0(f,a,b,2)
medio = intPuntoMedio(f,a,b)


print("Función x^3*e^(-x)\n")
while diferencia >= 10**(-6):
    Rk = metodoRomberg(f, a, b, n)
    Rk1 = metodoRomberg(f, a, b, n+1)
    print("R{0},{0} =".format(n), Rk )
    print("R{0},{0} =".format(n+1), Rk1 )
    diferencia = abs(Rk-Rk1)
    print("|R{0},{0}-R{1},{1}| =".format(n, n+1), diferencia)
    print("\n")
    cont = n+1
print("Su integral real es:",integral)
print("Su valor por el trapecio es:", trapecio)
print("Su valor por simpson es:", simpson)
print("Su valor por el punto medio es:",medio)
