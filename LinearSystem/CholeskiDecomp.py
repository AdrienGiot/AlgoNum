import numpy as np
import math

def choleskiDecomp(a):
    """
    Note that Choleski decomposition requires the matrix A to be
    symmetric and positive definite.

    @pre : a : <np.array | type=float64> The matrix A (n x n) that must be symmetric positive definite.

    @post : return <np.array> (n x n) lower triangular matrix.
    """
    n = len(a)
    for k in range(n):
        try:
            a[k, k] = math.sqrt(a[k, k] - np.dot(a[k, 0:k], a[k, 0:k])) # Compute diagonal value
        except ValueError:
            raise Exception("Matrix is not positive definite")
        for i in range(k+1, n):
            a[i, k] = (a[i, k] - np.dot(a[i, 0:k], a[k, 0:k])) / a[k, k] # Compute off-diagonal values
    for k in range(1, n):
        a[0:k, k] = 0.0 # Erase upper triangle
    return a


"""
Solve Ax = L tr(L) x = b by first solving Ly = b using forward substitution,
then tr(L) x = y using backward substitution.

@pre : L : <np.array | type=float64> Lower triangular matrice from choleskiDecomp()
       b : <np.array | type=float64> The matrix b (1 x n)

@post : b : <np.array | type=float64> The matrix b (1 x n)
"""
def choleskiSolve(L, b):
    n = len(L)
    for k in range(n):
        b[k] = (b[k] - np.dot(L[k, 0:k], b[0:k])) / L[k, k]
    for k in range(n-1, -1, -1):
        b[k] = (b[k] - np.dot(L[k+1:n, k], b[k+1:n])) / L[k, k]
    return b



# --------------- EXAMPLE ---------------

# A = np.array([[2,-1,0], [-1,2,-1], [0,-1,2]], dtype=np.float64)
# print("A = ")
# print(A)
# L = choleskiDecomp(A)
# print("L = ")
# print(L)
#
# b = np.array([3,-1,4], dtype=np.float64)
# print("b = ")
# print(b)
# print("x = ")
# print(choleskiSolve(L, b))
