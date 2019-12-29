import numpy as np

def Neville(xData,yData,x):
    """
    Newton interpolation function is used to aproximate the f(x) value with on a polynom

    @pre : Here length of xData  must be the same for yData
           xData  : <np.array | type=float64>  The known x-points
           yData  : <np.array | type=float64>  The points y associated with a x
           x      : <Float> The point at which we are looking for the image

    @post : return <Float> The Pn (x) value
    """

    m = len(xData)   # number of data points
    y = yData.copy()
    for k in range(1,m): #implements the recurrence formula of Neuville
        y[0:m-k] = ((x - xData[k:m])*y[0:m-k] +      \
                    (xData[0:m-k] - x)*y[1:m-k+1])/  \
                    (xData[0:m-k] - xData[k:m])
        print(y[0:m-k])
    return y[0]


# --------------- EXAMPLE ---------------

# xData = np.array([-1.2, 0.3, 1.1], dtype=np.float64)
# yData = np.array([-5.76, -5.61, -3.69], dtype=np.float64)
#
# print(Neville(xData, yData, 0.0))
#
# xData = np.array([1, 2, 3, 4, 5], dtype=np.float64)
# yData = np.array([4, 4, 4, 2, 4], dtype=np.float64)
#
# print(Neville(xData, yData, 3.9))
