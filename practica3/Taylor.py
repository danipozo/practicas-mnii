# -*- coding: utf-8 -*-
import numpy
import itertools as it
from math import factorial
from sympy import symbols, diff, log
def genf(r, f, t ,y, t_s, y_s):
    faux = f
    for i in range(1, r):
        faux = diff(faux, t_s) + diff(faux, y_s)*f
        yield faux.subs(t_s,t).subs(y_s,y).evalf()

def T(t,y,h,f,r, t_s, y_s):

    suma = f.subs(t_s,t).subs(y_s,y).evalf()
    for i,f_i in enumerate(genf(r, f, t ,y, t_s, y_s)):
        suma += ((h**(i+1))/(factorial(i+2)))*f_i

    return suma

def taylor(f,a,b,n,y_0,r, t_s, y_s):
    uj = y_0
    h = float(b - a)/float(n)
    tj = float(a)
    print ("Índice\t |  t  |  Aproximado(u) \t| Real(y) \t\t| Error")
    for i in range (1, n+2):
        yield uj
        valor=func_y.subs(t,tj).evalf()
        print (str(i)+"\t  "+str(tj)+" \t"+str(uj)+"\t"+str(valor)+"  \t "+str(valor-uj))
        uj = uj + h*T(tj, uj, h, f, r, t_s, y_s)
        tj = tj + h


t, y = symbols( 't y', real = True)

f = y**2/(1+t)

func_y= -1/log(t+1)

a = 1
b = 2
n = 10
y_0 = (-1/log(t+1)).subs(t,1).evalf()

print(f)
for i in taylor(f, a, b, n, y_0, 2, t, y):
    i
