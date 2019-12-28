#least square - Felix
import numpy as np
def least_square(xData, yData):
    def Asomme(xData, degre):
        s = 0
        for i in xData:
            s += i**degre
        return s
    def bsomme(xData, yData, n):
        s = 0
        for i in range(len(xData)):
            s += yData[i]*(xData[i]**n)
        return s
    def least_square_(xData, yData, n, x):
        a = np.zeros((n, n))
        b = np.zeros((n, 1))
        for i in range(n**2):
            data = Asomme(xData, i)
            j = 0
            i_temp = i
            # print("i {}".format(i))
            while i_temp >= n:
                j += 1
                i_temp -= 1
            while j <= i and j < n:
                # print("i {} j {}".format(i_temp, j))
                a[i_temp][j] = data
                j += 1
                i_temp -= 1
        for i in range(n):
            b[i][0] = bsomme(xData, yData, i)
        a_factors = np.linalg.solve(a, b).tolist()
        # print(type(x))
        s = 0
        for i in range(len(a_factors)):
            s += a_factors[i][0] * x**i
        return s
    return lambda n, x : least_square_(xData, yData, n, x)


if __name__ == "__main__":
    xData = [1, 2, 3, 4, 5]
    yData = [0, 1, 0, 1, 0]
    a = least_square(xData, yData, 4)
    a(1, 1)
    print(a(2, 26))