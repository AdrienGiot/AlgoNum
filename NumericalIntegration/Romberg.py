import numpy as np


def romberg(f, dim, a, b):
    def recursive_trapezoid(f, k, x_start, x_stop, matrix):
        if k == 1:
            h = (x_stop - x_start)
            matrix[0, 0] = (f(x_stop) + f(x_start)) * h / 2
            return matrix[0, 0]
        else:
            h = (x_stop - x_start) / 2 ** (k - 1)
            x_current = x_start + h
            term = f(x_current)
            for i in range(2 ** (k - 2) - 1):
                x_current += 2 * h
                term += f(x_current)
            matrix[k - 1, 0] = term * h + recursive_trapezoid(f, k - 1, x_start, x_stop, matrix) * 0.5
            return matrix[k - 1, 0]

    matrix = np.zeros((dim,dim))
    recursive_trapezoid(f, dim, a, b, matrix)
    for i in range(1,dim):
        for j in range(i,dim):
            matrix[j,i] = (4**(i) * matrix[j,i-1] - matrix[j-1,i-1]) / (4**(i) - 1) # on commence à 1 dans le formulaire,
                                                                                    # d'où i-1 -> i avec des index qui
                                                                                    # commencent à 0
    return matrix






def f(x):
    return np.sin(x)
print(romberg(f, 4, 0, np.pi))
