# -*- coding: utf-8 -*-
"""
    Estos serán los valores iniciales de nuestro programa:
    f(x,y) representa a la función de nuestro P.V.I
    [a,b] es el intervalo donde queremos aproximar
    n+1 serán los puntos de en los que aproximaremos.
"""



import math



def RungeKutta(f,a,b,n ,y_0):
    h=float(b-a)/n
    vals = []
    vals.append(y_0)
    valor=y(1)
    print ("Índice\t |  t  |  Aproximado(u) | Real(y) \t\t| Error")
    print ("0\t |  1  |"+str(y_0)+"\t|"+str(valor)+"  \t| "+str(valor-y_0))
    """
        NOTA: Ahora mismo los valores tj se machacan con cada interacción y los
        valores aproximados u se almacenan en el vector vals. Si se necesita cualquier modificación
        avisarla y lo cambio
    """
    for i in range (0, n-1):
        tj =a+(i+1)*h
        Ki = []
        Ki.append(f(tj,vals[i]))
        Ki.append(f(tj+h/2,vals[i]+(h/2)*Ki[0]))
        Ki.append(f(tj+h/2,vals[i]+(h/2)*Ki[1]))
        Ki.append(f(tj+h,vals[i]+h*Ki[2]))
        x = vals[i] + (h/6)*(Ki[0]+2*Ki[1]+2*Ki[2]+Ki[3])
        valor=y(tj)
        vals.append(x)
        print (str(i+1)+"\t | "+str(tj)+" |"+str(x)+"\t|"+str(valor)+"  \t| "+str(valor-x))


def f(t,x):
    return math.pow(x,2)/(1+t);

def y(t):
    return -1/math.log(t+1)

"""En t=1"""
f0 = -1/(math.log(2))

RungeKutta(f,1,2,10,f0)
