
import numpy as num
from decimal import *
import scipy as sci
from numpy.polynomial import polynomial as pol


def euler(f,a,b,n ,y_0):
    h=Decimal((b-a))/Decimal(n)
    vals = []
    vals.append(y_0)
    print ("Indice\t |  t  |  Aproximado(u) ")
    print("0\t |  0  |\t"+str(y_0))

    for i in range (0, n-1):
        tj =Decimal(a+(i)*h)
        x = vals[i] + h*f(tj,Decimal(vals[i]))
        vals.append(x)
        print(str(i+1)+"\t | "+str(tj)+" |"+"\t"+str(x))
        """print("u_",i+1,"=",x)"""


def f(t,x):
    return -x + t + 1

f0 = 1

euler(f,0,1,10,f0)
