import numpy as np

class ConjugateGradientDescent:
    def __init__(self, Q, b) -> None:
        self.Q = np.array(Q)
        self.b = np.array(b)
        # self.b = 
    
    def quadratic(self, x):
        x = np.array(x)
        xT = self.m_transpose(x)
        return  0.5 * xT.dot(self.Q.dot(x)) - xT.dot(self.b)
    
    def gradient(self, x):
        x = np.array(x)
        return self.Q.dot(x) - self.b
    
    def m_transpose(self, x):
        if x.ndim == 1 :
            return x.reshape(x.shape[0],1)
        else:
            return x.T
    
    def iterate(self, x0):
        list_of_x = []
        x0 = np.array(x0)
        Q = self.Q

        # Set initial g and d
        g0 = self.gradient(x0)
        if np.all(g0 == 0):
            return list_of_x
        else:
            d0 = -g0
        
        # Assing their values to loop variables
        g = g0
        d = d0
        x = x0
        #print(g0)

        while True:
            dT = self.m_transpose(d)
            gT = self.m_transpose(g)
            # print(d)
            # print(Q)
            # print(g)
            alpha = - (gT.dot(d)) / (dT.dot(Q.dot(d)))
            x = x + alpha * d
            list_of_x.append(x.tolist())
            if len(list_of_x) == Q.shape[1]:
                break;
            g = self.gradient(x)
            if np.all(g == 0):
                break;
            gT = self.m_transpose(g)
            beta = (gT.dot(Q.dot(d))) / (dT.dot(Q.dot(d)))
            d = -g + beta * d

        return list_of_x


if __name__ == '__main__':
    Q = [[3,0,1],[0,4,2],[1,2,3]]
    b = [[3],[0],[1]]

    # b = np.array(b)
    # new_b = b.reshape(b.shape[0],1)
    # print(b)
    # print(new_b)

    cgd = ConjugateGradientDescent(Q, b)
    answers = cgd.iterate([[0],[0],[0]])
    print(answers)
    print()
    print("Final value of x_k:", answers[len(answers) - 1])