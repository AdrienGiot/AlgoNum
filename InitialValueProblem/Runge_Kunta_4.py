import numpy as np

def integrate(F,x,y,xStop,h):
    def run_kut4(F,x,y,h):
        K0 = h*F(x,y)
        K1 = h*F(x + h/2.0, y + K0/2.0)
        K2 = h*F(x + h/2.0, y + K1/2.0)
        K3 = h*F(x + h, y + K2)
        return (K0 + 2.0*K1 + 2.0*K2 + K3)/6.0

    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x < xStop:
        h = min(h, xStop - x)
        y += run_kut4(F, x, y, h)
        x += x + h
        X.append(x)
        Y.append(y)
    return np.array(X), np.array(Y)

def runge_kunta_4(f, x, y, x_stop, h):
    def rk(F, x, y, h):
        K0 = h * F(x, y)
        K1 = h * F(x + h / 2.0, y + K0 / 2.0)
        K2 = h * F(x + h / 2.0, y + K1 / 2.0)
        K3 = h * F(x + h, y + K2)
        return (K0 + 2.0 * K1 + 2.0 * K2 + K3) / 6.0

    x_lst = []
    y_lst = []
    x_lst.append(x)
    y_lst.append(y)
    while x < x_stop:
        h = min(h, x_stop - x)
        y = y + rk(f, x,y,h)
        x = x + h
        x_lst.append(x)
        y_lst.append(y)
    return np.array(x_lst), np.array(y_lst)

def f(x, y):
    to_r = np.zeros(len(y))
    to_r[0] = y[1]
    to_r[1] = -4 * y[0]
    return to_r

print(runge_kunta_4(f,0.0,[1.0,0.0],5.0,0.2))
