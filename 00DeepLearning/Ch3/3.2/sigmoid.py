# 3.2.2
# only support float not numpy
import numpy as np
import matplotlib.pylab as plt


def step_function(x):
    if x > 0:
        return 1
    else:
        return 0


# 1. boolean judge elements in x and give it to y
# 2. transform boolean into int
def step_function_np(x):
    y = x > 0
    return y.astype(np.int)


# 3.2.3
def step_function_np_1(x):
    return np.array(x > 0, dtypen=np.int)


x = np.arange(-5.0, 5.0, 0.1)
y = step_function_np_1(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)


# 3.2.4
def sigmoid(x):
    return 1 / (1 + np.exp(x))


# 3.2.7
def relu(x):
    return np.maximum(0, x)
