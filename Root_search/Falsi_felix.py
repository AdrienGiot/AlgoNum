#Falsi - Félix

def falsi(f, a, b, err):
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    if (f(a) > 0 and f(b) > 0) or (f(a) < 0 and f(b) < 0):
        # print("coucou")
        return None
    new = b - f(b) * (b - a)/(f(b) - f(a))
    while f(new) >= err:
        if (f(new) > 0 and f(a) > 0 ) or (f(new) < 0 and f(a) < 0):
            a = new
        else:
            b = new
        new = b - f(b) * (b - a)/(f(b) - f(a))

    return new

if __name__ == "__main__":
    f = lambda x : 3*x -2
    print(falsi(f, -5, 5, 0.0000001))
    print(falsi(lambda x : 1, -5, 5, 0.001))