import numpy as np


def euler_modified(f, x, y, x_stop, h):
    x_lst = []
    y_lst = []
    x_lst.append(x)
    y_lst.append(y)
    while x < x_stop:
        h = min(h, x_stop - x)
        x += h
        y += h * f(x + (h / 2), y + (h / 2) * f(x, y))
        x_lst.append(x)
        y_lst.append(y)
    return np.array(x_lst), np.array(y_lst)
def f(x, y):
    to_r = np.zeros(len(y))
    to_r[0] = y[1]
    to_r[1] = -4 * y[0]
    return to_r


print(euler_modified(f, 0.0, [1.0, 0.0], 5.0, 0.2))
