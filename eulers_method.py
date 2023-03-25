

# importing the required module
import matplotlib.pyplot as plt

def question_4(w0, h, a, b):
    t = a
    w_t = w0
    while t <= b:
        print("t = " +str(t) + "    " +str(w_t))
        w_t = w_t + h + (h * ((t - w_t) ** 2))  
        t = t + h
    
if __name__ == '__main__':
    question_4(w0 = 1, h = 0.5, a = 2, b = 6)