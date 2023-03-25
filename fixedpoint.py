import math

def fixed_point_iteration(func, p_0, tol, max_iterations = 500):
    i = 1
    while i < max_iterations:
        p = func(p_0)
        if abs(p - p_0) < tol:
            break
        i = i + 1
        p_0 = p
    
    if i < max_iterations:
        print("Converged to :"+str(p))
        print("Iterations   :"+str(i))
        print("Tolerance    :"+str(tol))
    else:
        print("Failed to converge to tolerance within specified number of iterations")
        print("Last value reached: "+str(p))
        print("Tolerance:      "+str(tol))
        print("Max iterations: "+str(max_iterations))


if __name__ == "__main__":
    #func = lambda x: 2*x - math.cos()
    g_1 = lambda x: (3 + x - (2 * (x ** 2)))**(1/4)
    g_2 = lambda x: ((x + 3 - (x**4)) / (2))**(0.5)
    g_3 = lambda x: ((x + 3)/((x**2) + 2))**0.5
    g_4 = lambda x: (3*(x**4) + 2*(x**2) + 3)/(4*(x**3) + 4*x -1)
    p0 = 1
    tol = 1e-10
    max_iter = 100              
    fixed_point_iteration(g_4, p0, tol, max_iter)
    