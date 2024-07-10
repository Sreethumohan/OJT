# Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100

from numpy import random
x=random.randint(100,size=(3,5))
print(x)
