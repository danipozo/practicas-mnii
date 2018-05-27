import numpy as num
import scipy as sci
from decimal import *
from numpy.polynomial import polynomial as pol

def pMedio(f,a,b,n,y_0):
    h=Decimal((b-a))/Decimal(n)
    vals = []
    vals.append(y_0)
    print ("Indice\t |  t  |  Aproximado(u) ")
    print ("0\t |  0  |\t"+str(y_0))
    vals.append(euler1(f,a,b,n,y_0))
    print ("1\t | "+ str(h) + " |\t"+str(vals[1]))
    for i in range (2, n):
        tj = a+(i*h)
        x = vals[i-2] + Decimal(2*h*f(tj,vals[i-1]))
        vals.append(x)
        print(str(i)+"\t | "+str(tj)+" |\t"+str(x))



def euler1(f,a,b,n,y_0):
    h=Decimal((b-a))/Decimal(n)
    tj = Decimal(a+h)
    x = y_0 + h*f(tj,y_0)
    return x

def y(t,x):
	return -x*t + math.pow(t,2)/2 + t

def f(t,x):
    return -x + t + 1

f0 = 1

pMedio(f,0,1,10,f0)
