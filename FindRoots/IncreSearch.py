from numpy import sign
import numpy as np
import time
#tp
def rootsearchTP(f,a,b,dx):
    """
    The goal of this algorithm is to find the first root of the focus on the given interval.
    Note: in the examples, a while loop allows to get all the roots on the given inteval.

    @pre : Here length of xData  must be the same for yData
           f  : <function>  The function whose root we are looking for
           a  : <Float> The lower bound of the interval
           b  : <Float> The upper bound of the interval
           dx : <Float> The step between to test

    @post : return <(x1, x2)> The interval in which is the root
    """

    x1 = a
    f1 = f(x1)
    while(True):
        x2 = x1+dx
        f2 = f(x2)

        if(f1*f2<0):
            return (x1,x2)
        else:
            x1 = x2
            f1 = f2

        if(x2>b):
            return None

#Nico
def rootsearchNICO(f,a,b,dx):
    """
    This algorithm is a variant of the one proposed in tp. It seems to me to be simpler to retinue and to set up.
    Be careful, for some reason (maybe the numpy loop) this algo is slightly slower, it is possible to see the
    difference with the tests let's leave as an example.

    @pre : Here length of xData  must be the same for yData
           f  : <function>  The function whose root we are looking for
           a  : <Float> The lower bound of the interval
           b  : <Float> The upper bound of the interval
           dx : <Float> The step between to test

    @post : return <(x1, x2)> The interval in which is the root
    """
    fa = f(a)
    for i in np.arange(a, b, dx):
        if (fa * f(i) < 0):
            return (i-dx, i)
    return None


# --------------- EXAMPLE ---------------
#
# def f(x): return x**4+2*x**3-7*x**2+3
#
# #tp
# a = -400 # -4
# b = 200  #  2
# dx = 0.01
# start_time = time.time()
# while True:
#     rootbracket = rootsearchTP(f,a,b,dx)
#     if(rootbracket):
#         print(rootbracket)
#         a = rootbracket[1]
#     else:
#         break
# time_tp = time.time() - start_time
# print("--- %s seconds (TP)---" % (time.time() - start_time))
#
#
# #Nico
# a = -400 # -4
# b = 200  #  2
# dx = 0.01
# start_time = time.time()
# while True:
#     rootbracket = rootsearchNICO(f,a,b,dx)
#     if(rootbracket):
#         print(rootbracket)
#         a = rootbracket[1]
#     else:
#         break
# time_NICO = time.time() - start_time
# print("--- %s seconds (Nico)---" % (time.time() - start_time))
#
# print('TP {0} seconds faster'.format(time_NICO - time_tp) if time_NICO - time_tp >0 else 'NICO {0} seconds faster'.format(time_tp - time_NICO))
