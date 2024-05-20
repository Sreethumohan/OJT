#Write a Python program to calculate the factorial of a number using a lambda function and reduce function.
from functools import reduce
def factorial(n):
    if n == 0:
        return 1
    else:
        return reduce(lambda x, y: x * y, range(1, n + 1))
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")