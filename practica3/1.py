
import numpy as num
import scipy as sci
from numpy.polynomial import polynomial as pol


def euler(f,a,b,n ,y_0):
    h = (b-a)/n
    vals = []
    vals.append(y_0)
    print("u_0=", vals[0])
    for i in range (1, n):
        tj = a+i*h
        x = vals[i-1] + h*f(tj,vals[i-1])
        vals.append(x)
        print("u_",i,"=",x)


def f(t,x):
    return -x + t + 1

f0 = 1

euler(f,0,1,10,f0)
