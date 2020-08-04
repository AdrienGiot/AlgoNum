import numpy as np
import math


### recup dans chap 1
def choleskiDecomp(a):
    n = len(a)
    for k in range(n):
        try:
            a[k, k] = math.sqrt(a[k, k] - np.dot(a[k, 0:k], a[k, 0:k])) # Compute diagonal value
        except ValueError:
            raise Exception("Matrix is not positive definite")
        for i in range(k+1, n):
            a[i, k] = (a[i, k] - np.dot(a[i, 0:k], a[k, 0:k])) / a[k, k] # Compute off-diagonal values
    for k in range(1, n):
        a[0:k, k] = 0.0 # Erase upper triangle
    return a

def choleskiSolve(L, b):
    n = len(L)
    for k in range(n):
        b[k] = (b[k] - np.dot(L[k, 0:k], b[0:k])) / L[k, k]
    for k in range(n-1, -1, -1):
        b[k] = (b[k] - np.dot(L[k+1:n, k], b[k+1:n])) / L[k, k]
    return b



def CubicDevFindCoef(xData, yData, deg):
    """
    :param xData: valeurs x données
    :param yData: valeurs y associées aux valeurs x
    :param deg: le degré du polynome
    :return: retourne le tableau des coefs (tout les a du polynomes)
    """
    n = len(xData)
    deg+=1

    # CALCULE DE A
    A = np.zeros((deg,deg))

    for i in range(deg):
        for j in range(deg):
            for k in range(n):
                A[i, j] += pow(xData[k], i+j)
    A[0,0] = n


    # CALCULE DE B
    b = np.zeros(deg)
    for i in range(deg):
            for k in range(n):
                b[i] += pow(xData[k], i) * yData[k]

    return choleskiSolve(choleskiDecomp(A), b)

def AproxFun(x,a):
    """
    :param x: la valeur de x
    :param a: trouvé avec CubicDevFindCoef()
    :return: la valeur du polynome   a0 + (a1 * x) + (a2 * x^2) +...
    """
    sum = 0
    for i in range(len(a)):
        sum += a[i] * pow(x,i)
    return sum

def findTeta(xData, yData, a, deg):
    """
    :param xData: valeurs x données
    :param yData: valeurs y associées aux valeurs x
    :param a: trouvé avec CubicDevFindCoef()
    :param deg: le degré du polynome
    :return: la valeur de la racine carré de S/(n-m)
    """
    sum = 0
    for i in range(len(xData)):
        sum += pow( yData[i] - AproxFun(xData[i], a) , 2)
    return math.sqrt( sum / (len(xData) - deg+1))


def standDev(x,a):
    """
    :param x: la valeur x
    :param a: trouvé avec CubicDevFindCoef()
    :return: la valeur du polynome une fois dérivé    a1 + 2*(a2 * x) + 3*(a3 * x^2) +...
    """
    sum = 0
    for i in range(1, len(a)):
        sum += i * a[i] * pow(x,i-1)
    return sum


def findBestPolyDeg(xData, yData, max):
    """
    :param xData: valeurs x données
    :param yData: valeurs y associées aux valeurs x
    :param max: le degré maximum à évaluer
    :return: le meilleur degré à utiliser
    """
    minTeta = math.inf
    for deg in range(1,max):
        print("Deg : ", deg)
        coef = CubicDevFindCoef(xData, yData, deg)
        print("Coef : ", coef)
        teta = findTeta(xData, yData, coef, deg)
        print("Teta : ", teta)
        print()

        if(minTeta>teta):
            minTeta=teta
        else:
            return deg-1 #psq le meilleur est donc le précédent vu que plus petit que celui ci
    return max



### TEST

#Valeurs
xData = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4]
yData = [1.9934, 2.1465, 2.2129, 2.1790, 2.0683, 1.9448, 1.7655, 1.5891]

#Trouver le meilleur deg de polynome
deg = findBestPolyDeg(xData, yData, 10) # le degré du polynome à tester
print()
print("Best deg : ", deg)

#Trouver les a
coef = CubicDevFindCoef(xData, yData, deg) #trouver les a du polynomes
print()
print(coef)

# évaluer la fct en f'(0) et f'(1)
print()
print("Valeur en f'(0) : ", standDev(0, coef))
print("Valeur en f'(1) : ", standDev(1, coef))