# 2d Numpy arrays

# Import packages
import numpy as np

height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

np_height = np.array(height)
np_weight = np.array(weight)

# 2D Numpy array
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79], [65.4, 59.2, 63.6, 88.4, 68.7]])
print(np_2d)

print(np_2d.shape)

np_newtype = np.array([[1.73, 1.68, 1.71, 1.89, 1.79], [65.4, 59.2, 63.6, 88.4, "68.7"]])
print(np_newtype)

# print(np_2d[0])
# print(np_2d[0][2])
# print(np_2d[0,2])

print(np_2d[:,1:3])
print(np_2d[1,:])

conversion = np.array([1, 10, 100, 1000, 10000])

print(np_2d * conversion)