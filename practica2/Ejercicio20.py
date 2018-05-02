#Librerias
import numpy as num
import scipy as sci
from numpy.polynomial import polynomial as pol
import math
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



def f1(x):
    return (3*x)/(x**2-4)

def f2(x):
    return (math.cos(x)*math.exp(3*x))
a1=1
b1=1.8
a2=0
b2=math.pi/4
n=10

resultado1 = integrate.quad(f1, a1, b1)
resultado2 = integrate.quad(f2, a2, b2)

print (" Resultado exactos:  Apartado c: ", resultado1[0], "Apartado d: ", resultado2[0])

res1 = romberg(f1,a1,b1,n)
res2 = romberg(f2, a2, b2, n)
print("Los valores de la aproximacion por el metodo de Romberg son: Apartado c: ", res1, "Apartado d: ", res2)
