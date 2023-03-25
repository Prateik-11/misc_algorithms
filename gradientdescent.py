class GradientDescent:
    def __init__(self, df) -> None:
        self.df = df
    
    def iterate(self, x0, n, alpha):
        x = x0
        for i in range(n):
            x = x - alpha * self.df(x)
            # print(x)
        return x

class Test:
    def x_squared(x):
        return x*x
    def two_x(x):
        return 2*x
    def five_x_plus_two(x):
        return 5*x + 2


if __name__ == '__main__':
    gd = GradientDescent(Test.two_x)
    print(gd.iterate(40,100,0.1))

    gd = GradientDescent(Test.five_x_plus_two)
    print(gd.iterate(40,9,0.1))