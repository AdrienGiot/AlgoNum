import numpy as np

def LUdecomp(a): #same than Gauss Elim
    """
    LU decomposition corresponds to the Gauss elimination phase where we
    store the multiplier in the lower triangular portion of A.

    @pre : a : <np.array | type=float64> The matrix A (n x n) with |A| !=0 and close 0 numbers (cf. Norms).

    @post : a : <np.array>  (n x n) LU combined matrix.
            b : <List> indices of the lines that where pivoted
    """
    def LUdecompRP(a):
    n = len(a)
    rp = []
    for k in range(0, n-1):

        pivot_idx = k + list(np.abs(a[k:n, k])).index(max(np.abs(a[k:n, k]))) # Find the max absolute value in a rows

        temp_a = a[k].copy()           #
        a[k] = a[pivot_idx]            # Swap the max abs value with the init pivot
        a[pivot_idx] = temp_a          #
        rp.append(pivot_idx)           # And store it in a List

        for i in range(k+1, n):
            if a[i,k] != 0.0:
                lam = a[i, k] / a[k, k]
                a[i, k+1:n] = a[i, k+1:n] - lam*a[k, k+1:n]
                a[i, k] = lam # Store the multiplier in the lower triangular
    return(a, rp)


def LUsolve(a, b, rp):
    """
    We must only compute LU once; it can then be used to compute Ax = LUx = b for any b.
    Solve LUx = b by first solving Ly = b using forward substitution,
    then Ux = y using backward substitution.

    @pre : a  : <np.array | type=float64> The matrix LU (n x n) from LUdecomp(A)
           b  : <np.array | type=float32> The matrix b (1 x n)
           rp : <List> indices of the lines that where pivoted in LUdecompRP()

    @post : return <np.array> : (1 x n) matrix
    """
    n = len(a)
    for k in range(len(rp)):
        temp_b = b[k].copy()
        b[k] = b[rp[k]]
        b[rp[k]] = temp_b

    #LY = B forward substitution (b is replaced with the solution of Y)
    for k in range(1, n):
        b[k] = b[k] - np.dot(a[k, 0:k], b[0:k])

    #UX = Y backward substitution (b=Y is remplaced with the solution of X)
    b[n-1] = b[n-1] / a[n-1, n-1]

    for k in range(n-2, -1, -1):
        b[k] = (b[k] - np.dot(a[k, k+1:n], b[k+1:n])) / a[k, k]
    return b


# --------------- EXAMPLE ---------------

# A = np.array([[3,-3,3], [-3,5,1], [3,1,5]], dtype=np.float64)

# LU = LUdecomp(A)
#
# b = np.array([9,-7,12], dtype=np.float64)
# print("b = ")
# print(b)
# print("x = ")
# print(LUsolve(LU, b))
