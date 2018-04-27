# -*- coding: utf-8 -*-

"""
Programa 4: Fórmula de Simpson compuesta
"""

"""
Datos de entrada
"""

# Función cuya integral queremos aproximar
import scipy as sp
import numpy as np
from numpy.polynomial import polynomial as P


import math
import scipy.integrate as integrate
import scipy.special as special
def f(x):
	return (math.exp(3*x)*math.sin(3*x))/(x**4+1)

a = 0
b = 2
n = 20

""" 
Implementación
"""

# Fórmula de Simpson compuesta
def SimpsonCompuesto(f, a, b, n):
	m = 2 * n
	h = (b - a) / m

	nodos = []
	for i in range(m+1):
		nodos.append(a + i * h)

	sum1 = 0
	for i in range(1,n+1):
		sum1 += 4 * f(nodos[2 * i - 1])

	sum2 = 0
	for i in range(2,n+1):
		sum2 += 2 * f(nodos[2 * i - 2])

	return (h / 3) * (f(nodos[0]) + sum1 + sum2 + f(nodos[m]))

"""
Programa principal
"""

i = 0
result = integrate.quad(f, 0, 2)
print("Valor de la integral", result[0])

print("Método de Simpson Compuesto:")
# Ejemplo de ejecución
for i in range(1, n+1):
        print("n =", i, "Error obtenido: ", SimpsonCompuesto(f, a, b, i)-result[0])


def intTrapecio( f, a, b, n ):
     h = (b-a)/n
     x=[ a+h*i for i in range(n+1)]

     if(n<1):
          resultado=0
     elif(n==1):
          resultado = (f(b) + f(a))*(b-a)/2
     else:
          resultado = ( h *( ( f(x[0]) + f(x[n]) )/2 + sum([f(x[i+1]) for i in range(n-1)]) ) )

     return resultado


a=0
b=2

print("Método del trapecio compuesto")
for i in range(439, 441):
        resultado = intTrapecio( f, a, b, i )
        print("\nEl valor aproximado es:",resultado, "la diferencia con el valor exacto es: ", resultado-result[0], "con n = ", i)

