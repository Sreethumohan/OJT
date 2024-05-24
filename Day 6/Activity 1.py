#4. Create a class called MathOperations with class methods for 
# basic mathematical operations like addition, subtraction, multiplication, 
# and a static method to find the factorial of a number.

class MathOperations:
    @classmethod
    def add(cls, num1, num2):
        return num1 + num2

    @classmethod
    def sub(cls, num1, num2):
        return num1 - num2

    @classmethod
    def mul(cls, num1, num2):
        return num1 * num2

    @staticmethod
    def fact(num):
        if num == 0:
            return 1
        else:
            return num * MathOperations.fact(num - 1)
print("Addition:", MathOperations.add(5, 3))          
print("Subtraction:", MathOperations.sub(5, 3))   
print("Multiplication:", MathOperations.mul(5, 3))  
print("Factorial:", MathOperations.fact(5))           