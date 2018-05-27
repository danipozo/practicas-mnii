

import numpy
import itertools as it
from sympy import symbols, diff

def genf(r, f, t ,y):
    faux = f
    for i in range(1, r):
        f = diff(f, t) + diff(f, y)*faux(t,y)
        yield f(y, t)

def T(t,y,h,f,r):
    print(f(t,y))
    suma = f(t,y)
    for i,f_i in enumerate(genf(r, f, t ,y)):
        suma += (h**i)/(factorial(i))*f_i

def taylor(f,a,b,n,y_0,r):

    uj = y_0
    h = (b - a)/n
    tj = a
    for i in range (1, n+1):
        yield uj
        uj = uj + h*T(tj, uj, h, f, r)
        tj = tj + h


t, y = symbols( 't y', real = True)

f = -y+t+1

a = 0
b = 1
n = 10
y_0 = 1

for i in taylor(g, a, b, n, 1, 3):
    print(i)
