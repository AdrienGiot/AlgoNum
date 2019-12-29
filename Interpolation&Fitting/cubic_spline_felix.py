#cubic spline - Felix
#Tout est fait en classe parce que sinon c'est galère pour choisir un interval
#Aussi ça permet d'éviter de passer 1000 variable dans une fonction
import numpy as np
import math
class CubicSpline:
    def __init__(self, xData, yData):
        self.xData = xData
        self.yData = yData
        self.kData = [i[0] for i in self.create_kData()]
        self.dico = self.set_intervals()

    def create_kData(self):
        k_map = np.zeros((len(self.yData), len(self.yData)), dtype=np.float64)
        k_map[0][0] = 1
        k_map[-1][-1] = 1
        iter = 0
        while iter < len(k_map) - 2:
            k_map[iter+1][iter:iter+3] = np.array([1,4,1])
            iter += 1
        y_to_solve = np.zeros((len(self.yData), 1), dtype=np.float64)
        for i in range(1, len(self.yData)-1):
            h = self.xData[i] - self.xData[i-1]
            y_to_solve[i][0] = (6*(self.yData[i-1]-2*self.yData[i]+self.yData[i+1]))/h**2
        kData = np.linalg.solve(k_map, y_to_solve)
        return kData
    def set_intervals(self):
        d = {}
        iter = 0
        while iter < len(self.xData) -1 :
            d[(self.xData[iter], self.xData[iter + 1])] = self.make_funct(iter)
            iter += 1
        return d

    def make_funct(self,i):
        def make_fucnt_(i, x):
            kData = self.kData
            xData = self.xData
            yData = self.yData
            first = (kData[i]/6) * ((((x-xData[i+1])**3)/(xData[i]-xData[i+1])) - (x - xData[i+1])*(xData[i]-xData[i+1]))
            second = (kData[i+1]/6) * ((((x-xData[i])**3)/(xData[i]-xData[i+1])) - (x - xData[i])*(xData[i]-xData[i+1]))
            third = (yData[i]*(x - xData[i+1]) - yData[i+1]*(x - xData[i]))/(xData[i]-xData[i+1])
            return first - second + third
        return lambda x : make_fucnt_(i, x)


    def calcul(self, x):
        if isinstance(x, np.ndarray):
            
            l = []
            for i in x:
                l.append(self.calcul(i))
            return l
        for interval in self.dico:
            if self.in_interval(interval, x):
                return self.dico[interval](x)
        #Cas hors de l'interval -> approximation dégueu
        if x < self.xData[0]:
            return self.dico[(self.xData[0], self.xData[1])](x)
        if x > self.xData[-1]:
            return self.dico[(self.xData[-2], self.xData[-1])](x)
        return None

    def in_interval(self, interval, x):
        if x >= interval[0] and x <= interval[1]:
            return True
        return False


if __name__ == "__main__":
    xData = [1, 2, 3, 4, 5]
    yData = [0, 1, 0, 1, 0]
    a = CubicSpline(xData, yData)
    b = a.calcul
    print(b(1))
    print(b(2))
    print(b(3))
    print(b(4))
    print(b(5))
