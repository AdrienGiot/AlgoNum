import numpy as np


def bracket(f, x1, h, c = 1.618033989):
    f1 = f(x1)
    x2 = x1 + h;
    f2 = f(x2)
    # Determine downhill direction and change sign of h if needed
    if f2 > f1:
        h = -h
        x2 = x1 + h;
        f2 = f(x2)
        # Check if minimum between x1 - h and x1 + h
        if f2 > f1:
            return x2, x1 - h
    # Search loop
    for i in range(100):
        h = c * h
        x3 = x2 + h;
        f3 = f(x3)
        if f3 > f2:
            return x1, x3
        x1 = x2;
        x2 = x3
        f1 = f2;
        f2 = f3
    print("Bracket did not find a minimum")

def f(x):
    lam = 1.0 # Constraint multiplier
    c = min(0.0, x) # Constraint function
    return 1.6*x**3 + 3.0*x**2 - 2.0*x + lam*c**2
xStart = 1.0
h = 0.01
x1,x2 = bracket(f,xStart,h)

print("x1 =",x1)
print("x2=",x2)
