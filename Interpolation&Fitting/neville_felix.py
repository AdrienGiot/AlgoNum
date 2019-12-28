#neville - Felix
def neville(xData, yData):
    def neville_(xData, yData, x):
        if len(xData) == 1:
            return yData[0]
        else:
            num1 = (x - xData[-1]) * neville_(xData[:-1], yData[:-1], x)
            num2 = (xData[0] - x) * neville_(xData[1:], yData[1:], x)
            den = xData[0] - xData[-1]
            return (num1+num2)/den

    return lambda x : neville_(xData, yData, x)


if __name__ == "__main__":
    xData = [1,2,3]
    yData = [2,4,6]


    p = neuville(xData, yData)
    print(p(3))