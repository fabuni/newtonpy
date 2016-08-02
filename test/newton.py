from numpy.linalg import norm


def newton(f,Df,x0,tol):
    #print("newton")
    x = x0
    print("--------------")
    while norm(f(x))>tol:
        x = x - f(x)/Df(x)
        print(x)

    return x

#if __name__ == '__main__':
#    from numpy import sin, cos
#    print(newton(sin, cos, 0.5,1e-8))
