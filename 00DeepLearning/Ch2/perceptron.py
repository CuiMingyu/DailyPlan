import numpy as np


# 2.3.1
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1


# 2.3.2
x = np.array([0, 1])
w = np.array([0.5, 0.5])
b = -0.7
# this is dot *
print(w * x)
print(np.sum(w * x))
print(np.sum(w * x) + b)


# 2.3.3
def AND1(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * b) + b
    if tmp <= 0:
        return 0
    else:
        return 1
