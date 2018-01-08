# Basic Statistics

# Import packages
import numpy as np

height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

np_height = np.array(height)
np_weight = np.array(weight)

np_2d = np.array([height, weight])

print(np.mean(np_2d[0,:]))
# print(np.mean(np_2d[:,2]))
print(np.median(np_2d[1,:]))

np_corr = np.corrcoef(np_2d[0,:], np_2d[1,:])
print(np_corr)

np_std = np.std(np_2d[0,:])
print(np_std)

height_new = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight_new = np.round(np.random.normal(60.32, 15, 5000), 2)
np_city = np.column_stack((height_new, weight_new))
print(np_city)
np_next = np.row_stack((height_new, weight_new))
print(np_next)