

import numpy
import itertools as it
from math import factorial
from sympy import symbols, diff

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
    h = (b - a)/n
    tj = a
    for i in range (1, n+2):
        yield uj
        uj = uj + h*T(tj, uj, h, f, r, t_s, y_s)
        tj = tj + h


t, y = symbols( 't y', real = True)

f = -y+t+1

a = 0
b = 1
n = 10
y_0 = 1

print(f)
for i in taylor(f, a, b, n, 1, 2, t, y):
    print("Aproximación ", i)
