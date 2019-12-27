import numpy as np


def euler(F, x, y, xStop, h):
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x < xStop:
        h = min(h, xStop - x)
        y = y + h * F(x, y)
        x = x + h
        X.append(x)
        Y.append(y)
    return np.array(X), np.array(Y)


def F(x, y):
    to_r = np.zeros(len(y))
    to_r[0] = y[1]
    to_r[1] = -4 * y[0]
    return to_r


print(euler(F, 0.0, [1.0, 0.0], 5.0, 0.2))
