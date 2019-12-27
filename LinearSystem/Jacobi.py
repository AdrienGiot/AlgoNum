import numpy as np
import math

"""
Note: This algorithm does not come from the course, but has been realized from the notions
given by slides, it is possible to optimize the memory space, but also some point of
syntax related to a limited knowledge of Numpy
"""
def jacobi(a,b,xInit = False, err = 1e-10, withMax = True):
    """
    Jacobi development, very useful for matrices where the values of the terms of the diagonal are greater than the
    sum in absolute values of the other terms of the line.

    /!\ Be careful, it is possible that this algorithm diverges instead of converging.

    @pre : a       : <np.array | type=float> The matrix A (n x n) with |A| !=0 and close 0 numbers (cf. Norms)
           b       : <np.array | type=float> The matrix b (1 x n)
           xInit   : <np.array | type=float> The matrice (1 x n) of initials values to converge
           err     : <float> The limite of precision
           withMax : <boolean> -> if True, use "max | Xi - Yi |" for err calcul
                               -> if True, use "sum (Xi - Yi)^2" for err calcul

    @post : return <np.array> (1 x n) matrix
    """

    xInit = xInit if xInit != False else np.zeros((len(a),1)) #If no xInit arg, use a zeros matrix

    R = a.copy()
    D = np.zeros((len(a), len(a)))

    for i in range(len(R)):
        D[i,i] = R[i,i]**-1   # Create the diagonal matrix D^-1
        R[i,i] = 0            # replace the diagonal's values by 0

    limit = math.inf
    prevX = xInit.copy()

    while(err <= limit ):     # While the error is too big
        prevX = xInit.copy()
        xInit = np.dot(D, b - np.dot(R,xInit))   # In the cheat sheet

        if withMax: # If use       max | Xi - Yi |
            max = -1
            for i in range(len(xInit)):
                if abs(xInit[i] - prevX[i]) > max:
                    limit = abs(xInit[i] - prevX[i])

        else:       # If use :     sum (Xi - Yi)^2
            # limit = 0
            # for i in range(len(xInit)):
            #     limit += (xInit[i] - prevX[i])**2
            limit = sum((xInit-prevX)**2)

    return xInit


# --------------- EXAMPLE ---------------


# A = np.array([[100,-2,2], [-2,100,-20], [1,-2,100]], dtype=np.float64)
# b = np.array([[1],[1],[1]], dtype=np.float64)
# print(jacobi(A,b))
