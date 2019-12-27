import numpy as np

def gaussEliminPP(a, b):
    """
    Gauss elimination: By successive transformations, A is expressed as an upper
    triangular matrix. We then find the values of the unknowns by backward substitution.

    @pre : a : <np.array | type=float32> The matrix A (n x n) with |A| !=0 and close 0 numbers (cf. Norms)
           b : <np.array | type=float32> The matrix b (1 x n)

    @post : return <np.array> (1 x n) matrix
    """
    n = len(b)
    # Elimination Phase
    for k in range(0, n-1): #iterate on rows

        pivot_idx = k + list(np.abs(a[k:n, k])).index(max(np.abs(a[k:n, k])))  # Find the max absolute value in a rows

        temp_a = a[k].copy()              #
        temp_b = b[k].copy()              #
        a[k] = a[pivot_idx]               # Swap the max abs value with the init pivot
        b[k] = b[pivot_idx]               # /!\ to make on both matrixes
        a[pivot_idx] = temp_a             #
        b[pivot_idx] = temp_b             #

        for i in range(k+1, n): #for eatch cells under the pivot
            if a[i,k] != 0.0:   # if equal to zero, nothing to do
                lam = a[i, k] / a[k, k] #
                a[i, k+1:n] = a[i, k+1:n] - lam*a[k, k+1:n] #  Li -> Li - lam * Lk
                b[i] = b[i] - lam*b[k]
        #a[k+1:,k] = 0 #optional, set element bellow pivot to 0

    # Back substitution
    for k in range(n-1, -1, -1):
        b[k] = (b[k] - np.dot(a[k, k+1:n], b[k+1:n])) / a[k, k]
    return b



# --------------- EXAMPLE ---------------

# A = np.array([[0,-2,2], [-2,0,-20], [10,-2,4]], dtype=np.float32)
# print(A)
#
# b = np.array([1,1,1], dtype=np.float32)
# print(b)
#
# print(gaussEliminPP(A,b))
