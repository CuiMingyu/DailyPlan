import numpy as np

A = np.array([1, 2], [3, 4])
print(A)
B = np.array([5, 6], [7, 8])
np.dot(A, B)

# 3.3.3 Neural network dot X * W = Y
X = np.array([1, 2])
# X.shape is (2, )
W = np.array([1, 3, 5], [2, 4, 6])
# W is 2 * 3
Y = np.dot(X, W)
# Y is 1 * 3 is (3, )
