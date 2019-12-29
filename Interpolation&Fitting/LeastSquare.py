import numpy as np
import math

"""
Here we use the method of choleski seen previously because the matrix we use is symmetrical
"""
def choleski(a):
    n = len(a)
    for k in range(n):
        try:
            a[k,k] = math.sqrt(a[k,k] - np.dot(a[k,0:k],a[k,0:k]))
        except ValueError:
            raise Exception('Matrix is not positive definite')
        for i in range(k+1,n):
            a[i,k] = (a[i,k] - np.dot(a[i,0:k],a[k,0:k]))/a[k,k]
    for k in range(1,n): a[0:k,k] = 0.0 #erase upper triangle
    return a

def choleskiSol(L,b):
    n = len(b)
  # Solution of [L]{y} = {b}
    for k in range(n):
        b[k] = (b[k] - np.dot(L[k,0:k],b[0:k]))/L[k,k]
  # Solution of [L_transpose]{x} = {y}
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(L[k+1:n,k],b[k+1:n]))/L[k,k]
    return b


def polyFit(xData, yData, m):
    """
    Least-Square (Curve fitting) function is used to aproximate the f(x) value with on a polynom of degree m

    @pre : Here length of xData  must be the same for yData
           xData  : <np.array | type=float64>  The known x-points
           yData  : <np.array | type=float64>  The points y associated with a x
           m      : <int> The polynom's degree

    @post : return <np.array | type=float64> The coeficiens of the polynomials that approximate the function 
    """
    a = np.zeros((m+1, m+1))
    b = np.zeros(m+1)
    s = np.zeros(2*m+1)
    for i in range(len(xData)):
        temp = yData[i]
        for j in range(m+1):
            b[j] += temp
            temp *= xData[i]
        temp = 1.0
        for j in range(2*m+1):
            s[j] += temp
            temp *= xData[i]
    for i in range(m+1):
        for j in range(m+1):
            a[i, j] = s[i+j]
    return choleskiSol(choleski(a), b)

# --------------- EXAMPLE ---------------

xData = np.array([1., 2.5, 3.5, 4., 1.1, 1.8, 2.2, 3.7])
yData = np.array([6.008, 15.722, 27.130, 33.772, 5.257, 9.549, 11.098, 28.828])

print("Degree 1:")
coefs = polyFit(xData, yData, 1)
print(coefs)
print("Std dev:")

print("Degree 2:")
coefs = polyFit(xData, yData, 2)
print(coefs)

print("Degree 3:")
coefs = polyFit(xData, yData, 3)
print(coefs)
