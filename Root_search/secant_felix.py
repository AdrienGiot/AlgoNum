#secant - Felix
def secant(f, a, b, err):
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    if (f(a) > 0 and f(b) > 0) or (f(a) < 0 and f(b) < 0):
        return None
    new = b - f(b) * (b - a)/(f(b) - f(a))
    while f(new) >= err:
        a = b
        b = new
        new = b - f(b) * (b - a)/(f(b) - f(a))
    return new

if __name__ == "__main__":
    f = lambda x : 3*x -2
    print(secant(f, -5, 5, 0.0000001))
    print(secant(lambda x : 1, -5, 5, 0.001))