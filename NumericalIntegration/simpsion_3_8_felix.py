from simpson_1_3 import simpson_1_3
def simpson_3_8(f, n):
    def simpson_(f, n, a, b):
        h = (b - a)/n
        s = 0
        i = 0
        xData = []
        for k in range(n + 1):
            xData.append(a + k * h)
        if n % 3:
            s += simpson_1_3(f, n)(xData[0], xData[1])
            i = n % 3
        while i < n - 2 :
            add = (3*h/8) * (f(xData[i]) + 3 * f(xData[i+1]) + 3*f(xData[i+2]) + f(xData[i+3]))
            s += add
            i += 3
        return s
    return lambda a, b: simpson_(f, n, a, b)


if __name__ == "__main__":
    def f(x): return 1
    F = simpson_3_8(f, 200000)
    print(F(0, 2))
    def g(x): return x
    G = simpson_3_8(g, 2000)
    print(G(0, 3))
