# Install packages by using get-pip.py

# Go to website http://pip.readthedocs.io/en/stable/installing/
# Download get-pip.py
# Use the following commands in the terminal


# python3 get-pip.py # Remove comment for this line
# pip3 install numpy # Remove comment for this line

# Import packages
import numpy

Arr1 = numpy.array([1,2,3])
print(Arr1)

# Import and change name
import numpy as np
Arr2 = np.array([4,5,6])
print(Arr2)

# Import just one function from module
from numpy import array
Arr3 = array([7,8,9])
print(Arr3)