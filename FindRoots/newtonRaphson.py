def newtonRaphson(f,df,a,b,tol=1.0e-9):
    x = 0.5*(a + b)
    for i in range(30):
        fx = f(x)
        if fx == 0.0:
            print("number of iteration",i)
            return x

        dfx = df(x)
        dx  = -fx/dfx
        x   = x + dx

      # Check for convergence
        if abs(dx) < tol*max(abs(b),1.0):
            print("number of iteration : ",i)
            return x
    print('Too many iterations in Newton-Raphson')

def df(x): return 4*x**3+6*x**2-14*x

print(newtonRaphson(f,df, 0.79, 0.80, 1e-8))
print(newtonRaphson(f,df, 1.61, 1.62, 1e-8))    
