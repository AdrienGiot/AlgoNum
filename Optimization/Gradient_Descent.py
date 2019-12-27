import numpy as np
import math


def central_diff_x(f, x, y, h=0.01):
    return (f(x + h, y) - f(x - h, y)) / (2 * h)


def central_diff_y(f, x, y, h=0.01):
    return (f(x, y + h) - f(x, y - h)) / (2 * h)


def f(x, y, lam=100.0):
    return 6 * x ** 2 + y ** 3 + x * y + lam * min(0.0, y + 2) ** 2


def gradient_f(x, y):
    deri_x = 12 * x + y
    deri_y = x + 3 * y**2
    return np.array([deri_x, deri_y])


def gradient_descent(x, y, f, n=1.0, tol=0.000001):
    v_current = np.array([x, y])
    for i in range(30):
        v_prev = v_current
        v_current -= n * gradient_f(f, v_current[0], v_current[1])
        n *= 0.95
        if math.sqrt(np.dot(v_prev - v_current, v_prev - v_current)) <= tol:
            return v_current
print(gradient_descent(0.0,0.0,f))
