import math
class Adam:
    def __init__(self, df, bet1, beta2) -> None:
        self.df = df
        self.beta1 = bet1
        self.beta2 = beta2
    
    def iterate(self, x0, n, alpha):
        m = 0
        v = 0
        x = x0
        b1 = self.beta1
        b2 = self.beta2
        for i in range(n):
            g = self.df(x)
            m = (b1 * m) + (1 - b1) * g
            v = (b2 * v) + (1 - b1) * g * g
            m = m / (1 - b1)
            v = v / (1 - b2)
            x = x - ((alpha * m) / math.sqrt(v))
        return x

class Test:
    def x_squared(x):
        return x*x
    def two_x(x):
        return 2*x
    def five_x_plus_two(x):
        return 5*x + 2

if __name__ == '__main__':
    ad = Adam(Test.two_x)
    print(ad.iterate(40,100,0.1))

    ad = Adam(Test.five_x_plus_two)
    print(ad.iterate(40,9,0.1))