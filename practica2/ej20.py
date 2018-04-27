
import math
import numpy as num
import scipy as sci
from numpy.polynomial import polynomial as pol
import scipy.integrate as integrate
import scipy.special as special


def rkj(f,a,b,k,j):
    if(j == 0):
        h = (b-a)/(2**k)
        parcial = 0
        for i in range (2**k - 1):
            parcial = parcial + f(a+i*h)

        res = (h/2)*(f(a) + 2*parcial +f(b))

    else:
        res = rkj(f,a,b,k,j-1) + (1/(4**j-1))*(rkj(f,a,b,k,j-1) - rkj(f,a,b,k-1,j-1))

    return res;



#k = n
def romberg(f,a,b,n):
    aprox = rkj(f,a,b,n,n)
    return aprox



f1 = lambda x: (x**2)*num.log(x)
af1 = 1
bf1 = 1.5
n1 =1
f2 = lambda x: (x**3)*math.exp(-x)
af2 = 0
bf2 = 1
n2 = 1
f3 = lambda x: (3*x)/((x**2)-4)
af3 = 1
bf3 = 1.8
n3 = 1
f4 = lambda x : num.cos(x)*num.exp(3*x)
af4 = 0
bf4 = math.pi/4
n4 = 1


def calcular(f,a,b,n):
    it1 = romberg(f,a,b,n-1)
    it2 = romberg(f,a,b,n)

    while (abs(it1 - it2) > 10**(-6)):
        it1 = romberg(f,a,b,n-1)
        it2 = romberg(f,a,b,n)
        print("\n Iteracion : |R(", n-1,") - R(",n,")|" , abs(it1 - it2) )
        n = n+1
'''
print("Función 1: x^2 * log(x)")
calcular(f1,af1,bf1,n1)
v1 = integrate.quad(f1,af1,bf1)
print("El valor de real era:", v1)

print("Función 2: x^3 * e^(-x)")
calcular(f2,af2,bf2,n2)
v2 = integrate.quad(f2,af2,bf2)
print("El valor de real era:", v2)
''' 
print("Función 3: (3x/(x^2 -4))")
calcular(f3,af3,bf3,n3)
v3 = integrate.quad(f3,af3,bf3)
print("El valor de real era:", v3)

print("Función 4: cos(x) * e^(3x)")
calcular(f4,af4,bf4,n4)
v4 = integrate.quad(f4,af4,bf4)
print("El valor de real era:", v4)

