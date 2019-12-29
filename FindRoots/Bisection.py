from numpy import sign
import numpy as np
import math

def bisection(f,x1,x2,tol=1.0e-9, printN=False):
    """
    This algorithm makes it possible to find a function's root in a dichotomous way.

    @pre : Here length of xData  must be the same for yData
           f   : <function>  The function whose root we are looking for
           x1  : <Float> The lower bound of the interval
           x2  : <Float> The upper bound of the interval
           tol : <Float> The precision / accepted error

    @post : return <Float> The middle of the interval in which is the root
    """
    I = 0
    f1 = f(x1)
    f2 = f(x2)
    while(np.abs(x2-x1)>tol):
        I+=1
        x3 = 0.5 * (x1+x2)
        f3 = f(x3)
        if(f1*f3<0):
            x2 = x3
            f2 = f3
        else:
            x1 = x3
            f1 = f3
    if(printN):print("number of iterations", I)
    return 0.5 * (x1+x2)


# --------------- EXAMPLE ---------------

#
# def f(x): return x**4+2*x**3-7*x**2+3
# print(bisection(f, 0.79, 0.80, 1e-8, printN=True))
# print(bisection(f, 0.79, 0.80, printN=True))
# print(bisection(f, 1.61, 1.62, 1e-8, printN=True))
