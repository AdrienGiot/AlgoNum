#newton - Felix
def newton(xData, yData):
    def y_inv(i, j, xData, yData):
        if j == 0:
            return yData[i]
        elif j == 1:
            return (yData[i] - yData[i-1])/(xData[i] - xData[i-1])
        else:
            num = y_inv(i, j-1, xData, yData) - y_inv(i-1, j-1, xData, yData)
            den = xData[i] - xData[i-1]
            return num/den
    def newton_(xData, yData, x, k = len(xData)):
        n = len(xData) - k
        print(n)
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