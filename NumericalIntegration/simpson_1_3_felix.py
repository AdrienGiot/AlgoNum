#simpson 1/3 - Felix
from trapezoid import trapezoid
def simpson_1_3(f, n):
    def simpson_(f, n, a, b):
        h = (b - a)/n
        s = 0
        i = 0
        xData = []
        for k in range(n + 1):
            xData.append(a + k * h)
        if n % 2:
            s += trapezoid(f, n)(xData[0], xData[1])
            i = 1
        while i < n - 1:
            add = (h/3) * (f(xData[i]) + 4 * f(xData[i+1]) + f(xData[i+2]))
            s += add
            i += 2
        return s
    return lambda a, b: simpson_(f, n, a, b)


if __name__ == "__main__":
    # def f(x): return 1
    # F = simpson_1_3(f, 100)
    # print(F(0, 2))
    def g(x): return x
    G = simpson_1_3(g, 101)
    print(G(0, 1.5))
    print(G(1.5, 3))
