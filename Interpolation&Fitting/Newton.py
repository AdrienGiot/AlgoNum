import numpy as np

def Newton(xData,yData,x):
    """
    Newton interpolation function is used to aproximate the f(x) value with on a polynom

    @pre : Here length of xData  must be the same for yData
           xData  : <np.array | type=float64>  The known x-points
           yData  : <np.array | type=float64>  The points y associated with a x
           x      : <Float> The point at which we are looking for the image

    @post : return <Float> The Pn (x) value
    """

    m = len(xData)  # Number of data points
    a = yData.copy()
    print(a)
    for k in range(1,m): #Expression of a0,...,an
        a[k:m] = (a[k:m] - a[k-1])/(xData[k:m] - xData[k-1])

    n = len(xData) - 1  # Degree of polynomial
    p = a[n]
    for k in range(1,n+1): #implements the recurrence formula of the newton polynomial
        p = a[n-k] + (x -xData[n-k])*p
    return p


# --------------- EXAMPLE ---------------

# xData = np.array([-1.2, 0.3, 1.1], dtype=np.float64)
# yData = np.array([-5.76, -5.61, -3.69], dtype=np.float64)
#
# print(Newton(xData, yData, 0.0))
#
# xData = np.array([1, 2, 3, 4, 5], dtype=np.float64)
# yData = np.array([4, 4, 4, 2, 4], dtype=np.float64)
#
# print(Newton(xData, yData, 3.9))
