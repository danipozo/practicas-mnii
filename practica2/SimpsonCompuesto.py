from sympy import Symbol
from sympy import integrate
from decimal import *
"""
    Estos seran los datos de entrada de nuestro programa.
        f(x) representa la funcion que queremos integrar
        [a,b] es el intervalo donde queremos obtener el valor de la integral
        m son los intervalos que utilizaremos.
"""
x=Symbol('x')
f = 1/(1+x**2)

a=-4
b=4
m=10

"""
    A partir de aqui, comienza el codigo de nuestro programa.
    Primero de todo, calcularemos el valor de h y los nodos que utilizaremos.
"""
n=2*m

h=Decimal((b-a))/Decimal(n)

nodos=[]
for i in range(n+1):
    nodos.append(a+i*h)
    """print(nodos[i])"""

"""
    A continuacion, calcularemos el valor de la integral.
"""
suma1=0
suma2=0
for i in range(1,m+1):
    suma1=suma1+4*f.subs(x,nodos[2*i-1])
    if(i>=2):
        suma2=suma2+2*f.subs(x,nodos[2*i-2])
"""print("\n")
print(f.subs(x,nodos[0]))
print(suma1)
print(suma2)
print(f.subs(x,nodos[n]))

print("\n")
print(h)
print(h/3)
print(f.subs(x,nodos[0])+suma1+suma2+f.subs(x,nodos[n]))"""
integral=(h/3)*(f.subs(x,nodos[0])+suma1+suma2+f.subs(x,nodos[n]))

print(integral)
