#Librerias
import numpy as num
import scipy as sci
from numpy.polynomial import polynomial as pol

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



f = lambda x: num.log(x)
a=1
b=2
n=10

res = romberg(f,a,b,n)
print("\n El valor de la aproximacion por el metodo de Romberg es:", res)
