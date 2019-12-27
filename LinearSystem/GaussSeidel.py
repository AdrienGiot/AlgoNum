import numpy as np

def gaussSeidel(A, b, epsilon=1e-10):
    """
    Gauss Seidel seems to be inspired of Jacobi development. He can be faster or slower
    than Jacobi depending of A.

    /!\ Be careful, it is possible that this algorithm diverges instead of converging.

    @pre : A   : <np.array | type=float> The matrix A (n x n) with |A| !=0 and close 0 numbers (cf. Norms)
           b   : <np.array | type=float> The matrix b (1 x n)
           epsilon : <float> The limite of precision

    @post : return <np.array> (1 x n) matrix
    """

    n = A.shape[0]
    x = np.zeros(n)
    diff = float("Inf")

    while(diff > epsilon):  # While the error is too big
        previous_x = x.copy()
        for i in range(0,n):
            x[i] = 1/A[i, i] * (b[i] - sum(A[i,0:i] *x[0:i]) - sum(A[i,(i+1):n]*x[(i+1):n]))
        diff = sum((x-previous_x)**2)
    return np.array([x])


# --------------- EXAMPLE ---------------

# A = np.array([[1,2,4], [1,3,9], [1,4,16]], dtype=np.float32)
# b = np.identity(3)
#
# for i in range(0,100):
#     x = np.concatenate((gaussSeidel(A,b[0,:]),gaussSeidel(A,b[1,:]),gaussSeidel(A,b[2,:])),axis=0)
#
# print(x)
