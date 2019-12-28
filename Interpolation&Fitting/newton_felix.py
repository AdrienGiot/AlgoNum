#newton - Felix
def newton(xData, yData):
    def y_inv(i, n, xData, yData):
        if n == 0:
            return yData[i]
        elif n == 1:
            return (yData[i] - yData[n-1])/(xData[i] - xData[n-1])
        else:
            num = y_inv(i, n-1, xData, yData) - y_inv(n-1, n-1, xData, yData)
            den = xData[i] - xData[n-1]
            return num/den
    def newton_(xData, yData, x, k = len(xData)):
        n = len(xData) - k
        if k == 0:
            return xData[-1]
        return y_inv(n, n, xData, yData) + (x - xData[n]) * newton_(xData, yData, x, k - 1)

    return lambda x : newton_(xData, yData, x)


if __name__ == "__main__":
    xData = [1,2,3]
    yData = [2,4,6]

    s = newton(xData, yData)
    print(s(1))
    print(s(2))
    print(s(4))
