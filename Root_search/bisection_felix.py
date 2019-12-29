#bisection - Felix
def bisection(f, a, b, err):
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    mid = (b + a)/2
    f_mid = abs(f(mid))
    while abs(f(mid)) >= err:
        mid = (b + a)/2
        if (f(a) > 0 and f(b) > 0) or (f(a) < 0 and f(b) < 0):
            return None
        if f(mid) == 0:
            return mid
        if (f(mid) > 0 and f(a) > 0) or (f(mid) < 0 and f(a) < 0):
            a = mid
        else :
            b = mid
    return (a, b)

if __name__ == "__main__":
    f = lambda x : 3*x -3
    print(bisection(f, -5, 5, 0.0000001))
    print(bisection(lambda x : 1, -5, 5, 0.001))