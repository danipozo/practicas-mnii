import numpy as num
import scipy as sci
from numpy.polynomial import polynomial as pol

def pMedio(f,a,b,n ,y_0,y_1):
    h = (b-a)/n
    vals = []
    vals.append(y_0)
    print("u_0=", vals[0])
    vals.append(euler1(f,a,b,y_0))
    print("u_1=", vals[1])
    for i in range (2, n):
        tj = a+i*h
        x = vals[i-2] + x2*h*f(tj,vals[i-1])
        vals.append(x)
        print("u_",i,"=",x)


def euler1(f,a,b,y_0):
    h = (b-a)/n
    tj = a+h
    x = y_0 + h*f(tj,y_0)
    return x

def f(t,x):
    return -x + t + 1

f0 = 1


euler(f,0,1,10,f0)


