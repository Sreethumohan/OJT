#  Write a Python program to swap two numbers without using a temporary variable.
a=5
b=10
print("before swaping:")
print("a=",a)
print("b=",b)
a=a+b
b=a-b
a=a-b
print("After swaping")
print("a=",a)
print("b=",b)