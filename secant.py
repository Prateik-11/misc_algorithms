import math

def secant_method(f, x0, x1, tol, iterations):
    """Return the root calculated using the secant method."""
    for i in range(iterations):
        x2 = x1 - f(x1) * (x1 - x0) / float(f(x1) - f(x0))
        if abs(x2 - x1) < tol:
            break
        x0, x1 = x1, x2
    print('Root:       '+str(x2))
    print('Tolerance:  '+str(tol))
    print('Iterations: '+str(i+1))
    return x2

if __name__ == '__main__':
    f = lambda x: -x**3-math.cos(x)
    x0 = -1.0
    x1 = 0.0
    tol = 1.0e-100
    itr = 30
    secant_method(f, x0, x1, tol, itr)
