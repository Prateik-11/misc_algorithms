
class Newton:
    def __init__(self, df, d2f):
        self.df = df
        self.d2f = d2f
    
    def iterate(self, x0, itr):
        if itr == 0:
            return x0
        else:
            return self.iterate(x0 - self.df(x0)/self.d2f(x0), itr - 1)
        
class test_functions:
    def x_squared(x):
        return x * x
    
    def two_x(x):
        return 2 * x

    def two(x):
        return 2
    
if __name__ == '__main__':
    newt = Newton(test_functions.two_x, test_functions.two)
    print(newt.iterate(45, 10))
