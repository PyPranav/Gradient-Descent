import numpy as np


def gradient_descent(x,y):
    if len(x)!=len(y):
        raise Exception("Invalid Input")
    m_curr = b_curr = 0
    n = len(x)

    # the number of iteration and learning rate 
    # may be tweeked acc to the input for the best results
    iterations = 10000
    learning_rate = 0.08


    for i in range(iterations):
        y_predicted = m_curr*x + b_curr
        cost = (1/n)*sum((y-y_predicted)**2)
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        # print(f'{i}: m {m_curr}, b {b_curr}, cost {cost}')
    return (m_curr, b_curr)

# change the values of x and y for custom input
x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])
print(gradient_descent(x,y))