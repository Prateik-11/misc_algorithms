
class Fibonacci:
    def __init__(self, a, b, f, epsilon) -> None:
        self.a = a
        self.b = b
        self.f = f
        self.epsilon = epsilon
    
    def fibo(self, n):
        x = 0
        y = 1
        while(n > 0):
            temp = x
            x = y
            y = y + temp
            n = n - 1
        return y

    def iterate(self, itr):
        a = self.a
        b = self.b
        func = self.f
        n = itr
        
        for i in range(itr):
            # print (list([a, b]))
            # print(list([self.fibo(n-2), self.fibo(n-1)]))

            # new_a = a + (self.fibo(n-2) / self.fibo(n)) * (b - a)
            # new_b = a + (self.fibo(n-1) / self.fibo(n)) * (b - a)

            rho = 1 - (self.fibo(n) / self.fibo(n + 1))
            
            #print([self.fibo(n),self.fibo(n + 1)])
            
            if rho == (1/2):
                rho = rho - self.epsilon
            
            new_a = a + rho*(b - a)
            new_b = a + (1 - rho)*(b - a)

            f_new_a = func(new_a)
            f_new_b = func(new_b)

            if f_new_a < f_new_b:
                b = new_b
            elif f_new_b < f_new_a:
                a = new_a
            else:
                a = new_a
                b = new_b
            n = n - 1
            # print([a,b])

        return (a + b) / 2

class test_functions:
    def x_squared(x):
        return x * x
    
if __name__ == '__main__':
    fib = Fibonacci(-5,15, test_functions.x_squared, 0.0000000001)
    # fib.iterate(7)
    print(fib.iterate(7))