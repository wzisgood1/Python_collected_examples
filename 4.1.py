# Numpy

# Import packages
import numpy as np

height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

# Operations on lists failed here
# weight / height ** 2

np_height = np.array(height)
np_weight = np.array(weight)
# print(np_height, np_weight)
bmi = np_weight / np_height ** 2
print(bmi)
bmi[1]
print(bmi[2:4])

# Numpy arrays: contain only one type
np_a1 = np.array([1.0, "is", True])
print(np_a1)
print(type(np_a1))

# Different methods for lists/arrays (different types: different behavior)
python_list = [1,2,3]
numpy_array = np.array([1,2,3])
print(python_list + python_list)
print(numpy_array + numpy_array)

bmi_high = bmi > 23
print(bmi_high)
# print(type(bmi_high))
print(bmi[bmi > 23])

bmi_light = bmi[bmi < 21]

bmi_subset = bmi[2:5]
print(bmi_subset)
