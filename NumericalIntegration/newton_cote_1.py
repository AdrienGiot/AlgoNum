import numpy as np


def composite_trapezoid(f, n, x_start, x_stop):
    h = (x_stop - x_start) / n
    x_current = x_start
    to_r = 0
    for i in range(n):
        to_r += f(x_current) + f(x_current + h)
        x_current += h
    return to_r * h / 2  # pas oublier de multiplier la somme


def f(x):
    return np.log(1 + np.tan(x))

def recursive_trapezoid(f, k, x_start, x_stop):
    if k == 1:
        h = (x_stop - x_start)
        return (f(x_start) + f(x_stop)) * h / 2
    else:
        h = (x_stop - x_start) / 2 ** (k - 1)
        x_current = x_start + h
        term = f(x_current)
        for i in range(2 ** (k - 2) - 1):
            x_current += 2 * h
            term += f(x_current)
        return term * h + recursive_trapezoid(f, k - 1, x_start, x_stop) * 0.5


print(recursive_trapezoid(f, 3, 0, np.pi / 4))
print(composite_trapezoid(f,3, 0, np.pi / 4))