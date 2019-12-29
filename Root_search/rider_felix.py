#rider - Felix
from math import sqrt
def rider(f, a, b, err):
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    if (f(a) > 0 and f(b) > 0) or (f(a) < 0 and f(b) < 0):
        return None
    mid = (a + b)/2
    if (f(a) - f(b)) > 0:
        new = mid + (mid - a) * f(mid)/sqrt((f(mid)**2) - f(a)*f(b))
    else :
        new = mid - (mid - a) * f(mid)/sqrt((f(mid)**2) - f(a)*f(b))
    while f(new) >= err:
        if (f(new) > 0 and f(a) > 0 ) or (f(new) < 0 and f(a) < 0):
            a = new
        else:
            b = new
        if (f(a) - f(b)) > 0:
            new = mid + (mid - a) * f(mid)/sqrt((f(mid)**2) - f(a)*f(b))
        else :
            new = mid - (mid - a) * f(mid)/sqrt((f(mid)**2) - f(a)*f(b))
    return new


if __name__ == "__main__":
    f = lambda x : 3*x - 2
    print(rider(f, -5, 5, 0.0000001))
    print(rider(lambda x : 1, -5, 5, 0.001))