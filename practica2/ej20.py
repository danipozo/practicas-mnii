import ejercicio5
import math

f1 = lambda x: (x**2)*num.log(x)
af1 = 1
bf1 = 1.5
n1 =1
f2 = lambda x: (x**3)*.exp(-x)
af2 = 0
bf2 = 1
n2 = 1
f3 = lambda x: (3*x)/((x**2)-4)
af3 = 1
bf3 = 1.8
n3 = 1
f4 = lambda x : num.cos(x)*num.exp(3*x)
af4 = 0
bf4 = math.pi/4
n4 = 1


def calcular(f,a,b,n):
    while (abs(romberg(f,a,b,n-1) - romberg(f,a,b,n)) < 10**(-6)):
    frase = "\n" + "Iteracion " + str(n) + ":" + "|R(n-1) - R(n)|" + str(abs(romberg(f,a,b,n-1) - romberg(f,a,b,n)))
    print(frase)
    n = n+1

print("Función 1: x^2 * log(x)")
calcular(f1,af1,bf1,n1)
v1 = integrate.quad(f1,af1,bf1)
print("El valor de real era:", v1)

print("Función 2: x^3 * e^(-x)")
calcular(f2,af2,bf2,n2)
v2 = integrate.quad(f2,af2,bf2)
print("El valor de real era:", v2)

print("Función 3: (3x/(x^2 -4))")
calcular(f3,af3,bf3,n3)
v3 = integrate.quad(f3,af3,bf3)
print("El valor de real era:", v3)

print("Función 4: cos(x) * e^(3x)")
calcular(f4,af4,bf4,n4)
v4 = integrate.quad(f4,af4,bf4)
print("El valor de real era:", v4)

