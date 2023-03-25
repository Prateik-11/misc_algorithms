import math

class Nesterov:
    def __init__(self, df) -> None:
        self.df = df
    
    def iterate(self, x0, n, alpha):
        x = x0
        lambda_k = 0
        v = 0
        for i in range(n):
            lambda_k1 = (1 + math.sqrt(1 + 4 * lambda_k * lambda_k)) / 2
            gamma = (1 - lambda_k) / lambda_k1
            v1 = x - alpha * self.df(x)
            x = (1 - gamma) * v1 + gamma * v
            lambda_k = lambda_k1
            v = v1
        return x

class Test:
    def x_squared(x):
        return x*x
    def two_x(x):
        return 2*x
    def five_x_plus_two(x):
        return 5*x + 2

if __name__ == '__main__':
    nest = Nesterov(Test.two_x)
    print(nest.iterate(40,9,0.1))

    nest = Nesterov(Test.five_x_plus_two)
    print(nest.iterate(40,9,0.1))