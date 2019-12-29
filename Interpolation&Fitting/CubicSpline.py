import numpy as np

def cubicspline_curvatures(xData,yData):
    """
    Newton interpolation function is used to aproximate the f(x) value with on a polynom

    @pre : Here length of xData  must be the same for yData
           xData  : <np.array | type=float64>  The known x-points
           yData  : <np.array | type=float64>  The points y associated with a x
           x      : <Float> The point at which we are looking for the image

    @post : return <Float> The Pn (x) value
    """
    def LUdecomp3(c,d,e):
        n = len(d)
        for k in range(1,n):
            lam = c[k-1]/d[k-1]
            d[k] = d[k] - lam*e[k-1]
            c[k-1] = lam
        return c,d,e

    def LUsolve3(c,d,e,b):
        n = len(d)
        for k in range(1,n):
            b[k] = b[k] - c[k-1]*b[k-1]
        b[n-1] = b[n-1]/d[n-1]
        for k in range(n-2,-1,-1):
            b[k] = (b[k] - e[k]*b[k+1])/d[k]
        return b

    n = len(xData) - 1
    c = np.zeros(n)
    d = np.ones(n+1)
    e = np.zeros(n)
    k = np.zeros(n+1)
    c[0:n-1] = xData[0:n-1] - xData[1:n]
    print(c)
    d[1:n] = 2.0*(xData[0:n-1] - xData[2:n+1])
    print(d)
    e[1:n] = xData[1:n] - xData[2:n+1]
    print(e)
    k[1:n] =6.0*(yData[0:n-1] - yData[1:n]) \
                 /(xData[0:n-1] - xData[1:n]) \
             -6.0*(yData[1:n] - yData[2:n+1])   \
                 /(xData[1:n] - xData[2:n+1])
    LUdecomp3(c,d,e)
    LUsolve3(c,d,e,k)
    return k

def cubicspline_evalSpline(xData,yData,k,x):

    def findSegment(xData,x):
        iLeft = 0
        iRight = len(xData)- 1
        while 1:
            if (iRight-iLeft) <= 1: return iLeft
            i = int( (iLeft + iRight)/2 )
            if x < xData[i]: iRight = i
            else: iLeft = i

    i = findSegment(xData,x)

    h = xData[i] - xData[i+1]
    y = ((x - xData[i+1])**3/h - (x - xData[i+1])*h)*k[i]/6.0 \
      - ((x - xData[i])**3/h - (x - xData[i])*h)*k[i+1]/6.0   \
      + (yData[i]*(x - xData[i+1])                            \
       - yData[i+1]*(x - xData[i]))/h
    return y

# # --------------- EXAMPLE ---------------
#
xData = np.array([1, 2, 3, 4, 5], dtype=np.float64)
yData = np.array([4, 4, 4, 2, 4], dtype=np.float64)

k = cubicspline_curvatures(xData, yData)
print(cubicspline_evalSpline(xData, yData, k, 3.9))
#
# xData = np.array([-1.2, 0.3, 1.1], dtype=np.float64)
# yData = np.array([-5.76, -5.61, -3.69], dtype=np.float64)
#
# k = cubicspline_curvatures(xData, yData)
# print(cubicspline_evalSpline(xData, yData, k, 0))
