#creating matrix in numpy
import numpy as np

# String input
a = np.matrix('1 2; 3 4')
print("Via String input : \n", a, "\n\n")

# Array-like input
b = np.matrix([[5, 6, 7], [4, 6, 8]])
print("Via array-like input : \n", b)
