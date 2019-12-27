import numpy as np
def newton_cote_2(f,n,a,b):
    h = (b - a) / n
    x_current = a
    to_r = 0
    for i in range(0,n,2):
        to_r += f(x_current) + 4 f(x_current + h) + f(x_current + 2 * h)
        x_current += 2 * h

    return to_r * h/3

def f(x):
    return np.log(1 + np.tan(x))

print(newton_cote_2(f,10,0,np.pi/4))