class Bisection:
    def __init__(self, a, b, df) -> None:
        self.a = a
        self.b = b
        self.df = df
    
    # def iterate(self, itr):
    #     a = self.a
    #     b = self.b
    #     func = self.df
    #     for i in range(itr):
    #         c = (a + b) / 2
    #         if func(c) == 0:
    #             return c
    #         if func(a) * func(c) < 0:
    #             b = c
    #         elif func(b) * func(c) < 0:
    #             a = c
    #     return (a + b) / 2
    
    # def iterate(self, tolerance, itr = 99999):
    #     a = self.a
    #     b = self.b
    #     func = self.df
    #     i = 1
    #     while i <= itr & (b-a)/2 > tolerance:
    #         c = (a + b) / 2
    #         if func(c) == 0:
    #             return c
    #         if func(a) * func(c) < 0:
    #             b = c
    #         elif func(b) * func(c) < 0:
    #             a = c
    #         i = i + 1
    #     return (a + b) / 2

    def iterate(self, tolerance):
        a = self.a
        b = self.b
        func = self.df
        n = 0
        while (b-a)/2 > tolerance:
            p = (a + b) / 2
            if func(a) * func(p) < 0:
                b = p
            else:
                a = p
            n = n + 1
            print(str(n)+" iterations done", end = '\r')
        return p, n

class functions:
    def x_squared(x):
        return x * x
    
    def two_x(x):
        return 2 * x

    def two(x):
        return 2
    
    def x_squared_minus_three(x):
        return x*x - 3
    
if __name__ == '__main__':
    bi = Bisection(0, 4, functions.x_squared_minus_three)
    print(bi.iterate(10**(-5)))