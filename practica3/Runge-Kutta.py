# -*- coding: utf-8 -*-
"""
    Estos serán los valores iniciales de nuestro programa:
    f(x,y) representa a la función de nuestro P.V.I
    [a,b] es el intervalo donde queremos aproximar
    n+1 serán los puntos de en los que aproximaremos.
"""



import math
from sympy import symbols, diff, log


def RungeKutta(f,a,b,n ,y_0):
    h=float(b-a)/n
    vals = []
    vals.append(y_0)
    valor=y_0
    print ("Índice\t |  t  |  Aproximado(u) | Real(y) \t\t| Error")
    print ("0\t |  1  |"+str(y_0)+"\t|"+str(valor)+"  \t| "+str(valor-y_0))
    """
        NOTA: Ahora mismo los valores tj se machacan con cada interacción y los
        valores aproximados u se almacenan en el vector vals. Si se necesita cualquier modificación
        avisarla y lo cambio
    """
    for i in range (0, n):
        tj =a+(i+1)*h
        Ki = []
        Ki.append(f(tj,vals[i]))
        Ki.append(f(tj+h/2,vals[i]+(h/2)*Ki[0]))
        Ki.append(f(tj+h/2,vals[i]+(h/2)*Ki[1]))
        Ki.append(f(tj+h,vals[i]+h*Ki[2]))
        x = vals[i] + (h/6)*(Ki[0]+2*Ki[1]+2*Ki[2]+Ki[3])
        valor=func_y.subs(t,tj).evalf()
        vals.append(x)
        print (str(i+1)+"\t | "+str(tj)+" |"+str(x)+"\t|"+str(valor)+"  \t| "+str(valor-x))


def f(t,x):
    return math.pow(x,2)/(1+t);

t, y = symbols( 't y', real = True)
func_y= -1/log(t+1)

"""En t=1"""
y_0 = (-1/log(t+1)).subs(t,1).evalf()

RungeKutta(f,1,2,10,y_0)
