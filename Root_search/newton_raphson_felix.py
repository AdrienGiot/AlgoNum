#newton raphson - Felix
import numpy as np
import bisection
def nr(f,a, b, err):
    bracket = bisection.bisection(f, a, b, 1)
    if type(bracket) != tuple:
        return bracket
    x = (bracket[0] + bracket[1])/2
    df = lambda x : (f(x + err) - f(x - err))/err*2
    # print(df(x))
    if df(x) == 0:
        return None
    while f(x) >= err:
        x = x - f(x)/df(x)
    return x

if __name__ == "__main__":
    f = lambda x : 3*x - 2
    print(nr(f, -5, 5, 0.0000001))
    print(nr(lambda x : 1, -5, 5, 0.001))