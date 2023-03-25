
class GoldenSection:
    def __init__(self, a, b, f) -> None:
        self.a = a
        self.b = b
        self.f = f
    
    def iterate(self, itr):
        func = self.f
        a = self.a
        b = self.b
        rho = 0.381966011
        
        for i in range(itr):
            new_a = a + rho*(b - a)
            new_b = b - rho*(b - a)

            f_new_a = func(new_a)
            f_new_b = func(new_b)

            if f_new_a < f_new_b:
                b = new_b
            elif f_new_b < f_new_a:
                a = new_a
            else:
                a = new_a
                b = new_b

        return (a + b) / 2

class test_functions:
    def x_squared(x):
        return x * x
    
if __name__ == '__main__':
    gold = GoldenSection(-1,5, test_functions.x_squared)
    print(gold.iterate(10))
