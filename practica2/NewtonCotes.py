from sympy import Symbol
from sympy import integrate
"""
    Estos seran los datos de entrada de nuestro programa.
        f(x) representa la funcion que queremos integrar
        [a,b] es el intervalo donde queremos obtener el valor de la integral
        n+1 son los nodos que utilizaremos.
"""
x=Symbol('x')
f = 1/(1+x**2)

a=-4
b=4
n=4

"""
    A partir de aqui, comienza el codigo de nuestro programa.
    Primero de todo, calcularemos el valor de h, los nodos que utilizaremos,
    asi como la base de Lagrange o pesos que utilizaremos para nuestro calculo
    de la integral.
"""

h=(b-a)/n

nodos=[]
for i in range(n+1):
    nodos.append(a+i*h)

pesos=[]
for i in range(n+1):
    aux=1
    for j in range(n+1):
        if(j != i):
            aux=aux*(x-nodos[j])/(nodos[i]-nodos[j])
            """print(aux)"""
    pesos.append(aux)

print(pesos[0])
print(integrate(pesos[0],(x,a,b)))

"""
    Una vez que tenemos calculados los pesos, en funcion de x, calcularemos el
    valor de una aproximacion de la integral.
"""
integral=0
for i in range(n+1):
    integral=integral+integrate(pesos[i],(x,a,b))*f.subs(x,nodos[i])

print(integral)
