import math

def f(x):
    return 2**x*math.sin(x)

def A0(f, c, h):
    return (f(c+h)-f(c))/h

def A1(f, c, h):
    return 2*A0(f, c, h/2)-A0(f, c, h)

def A2(f, c, h):
    return (4*A1(f, c, h/2)-A1(f, c, h))/3

print("f'(1.05) con h = 0.4: {}".format(A2(f, 1.05, 0.4)))
