
# Create a class Square that inherits from the Rectangle class.
# Add a method calculate_diagonal() to calculate the diagonal of the square.

import math
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def calculate_diagonal(self):
        return math.sqrt(2) * self.length

square = Square(4)
print("Diagonal:", square.calculate_diagonal())