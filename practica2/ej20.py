import ejercicio5

f1 = lambda x: (x**2)*num.log(x)
af1 =
bf1 =
n1 =1
f2 = lambda x: (x**3)*.exp(-x)
af2 =
bf2 =
n2 = 1
f3 = lambda x: (3*x)/((x**2)-4)
af3 =
bf3 =
n3 = 1
f4 = lambda x : num.cos(x)*num.exp(3*x)
af4 =
bf4 =
n4 = 1


def calcular(f,a,b,n):
    while (abs(romberg(f,a,b,n-1) - romberg(f1,af1,bf1,n)) < 10**6):
    frase = "\n" + "Iteracion " + str(n) + ":" + "|R(n-1) - R(n)|" + str(abs(romberg(f1,af1,bf1,n1-1) - romberg(f1,af1,bf1,n1)))
    print(frase)
    n = n+1

print("Función 1: x^2 * log(x)")
calcular(f1,af1,bf1,n1)

print("Función 2: x^3 * e^(-x)")
calcular(f2,af2,bf2,n2)

print("Función 3: (3x/(x^2 -4))")
calcular(f3,af3,bf3,n3)

print("Función 4: cos(x) * e^(3x)")
calcular(f4,af4,bf4,n4)

