# -*- coding: utf-8 -*-
"""
    Estos serán los valores iniciales de nuestro programa:
    f(x,y) representa a la función de nuestro P.V.I
    [a,b] es el intervalo donde queremos aproximar
    n+1 serán los puntos de en los que aproximaremos.
"""


import numpy as num
from decimal import *
import scipy as sci
from numpy.polynomial import polynomial as pol


def RungeKutta(f,a,b,n ,y_0):
    h=Decimal((b-a))/Decimal(n)
    vals = []
    vals.append(y_0)
    print("u_0=", vals[0])
    for i in range (0, n-1):
        tj =Decimal(a+(i+1)*h)
        Ki = []
        Ki.append(f(tj,vals[i]))
        Ki.append(f(tj+h/2,vals[i]+(h/2)*Ki[0]))
        Ki.append(f(tj+h/2,vals[i]+(h/2)*Ki[1]))
        Ki.append(f(tj+h,vals[i]+h*Ki[2]))
        x = vals[i] + (h/6)*(Ki[0]+2*Ki[1]+2*Ki[2]+Ki[3])
        vals.append(x)
        print("u_",i+1,"=",x)


def f(t,x):
    return -x + t + 1

f0 = 1

RungeKutta(f,0,1,10,f0)
