import numpy as np
import math

def Lagrange(xData,yData, x):
    """
    Lagrange interpolation function is used to aproximate the f(x) value

    @pre : Here length of xData  must be the same for yData
           xData  : <list>  The known x-points
           yData  : <list>  The points y associated with a x
           x      : <Float> The point at which we are looking for the image

    @post : return <Float> The Pn (x) value
    """
    # Apply the equation
    res = 0
    for i in range(len(xData)):
        prod = 1
        for j in range(len(yData)):
            if(i!=j):
                prod *= (x-xData[j])/(xData[i]-xData[j])
        res += prod*yData[i]
    return res


# --------------- EXAMPLE ---------------

# xData = [ -1.2, 0.3, 1.1]
# yData = [ -5.76, -5.61, -3.69]
# x = 0
#
# print(Lagrange(xData, yData, x))
