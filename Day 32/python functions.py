# Creating several basic functions.
# Function: Add
def add(a, b):
     print ("Adding : %d + %d" % (a, b)) 
     return a + b
# Function: Subtract
def subtract(a, b):
     print ("Subtracting : %d - %d" % (a, b))
     return a - b
# Function: Multiply
def multiply(a, b):
     print ("Multiplying : %d * %d" % (a, b)) 
     return a * b
# Function: Divide
def divide(a, b):
     print ("Dividing : %d / %d" % (a, b)) 
     return a / b
print("Let's use the functions created by us")

# Calling Functions 
A = add(5, 5)
B = subtract(5, 6)
C = multiply(6, 5)
D = divide(5, 5)
print ("A : %d | B : %d | C : %d | D : %d" % (A, B, C, D))
# Default Arguments
# example 1
def empinfo(designation, name="ABC"):
    print("Name : ", name)
    print("Designation : ", designation)
    return

empinfo(designation="Dev")

# example 2
def empinfo(designation, name="XYZ"):
    print("Name : ", name)
    print("Designation : ", designation)
    return

empinfo(designation="Dev", name="ABC")
empinfo(designation="Dev")

# Required Arguments
# Example
def callme(str):
    print(str)

callme("Hello, world!")

# Keyword Arguments
# Example
def callme(str_value):
    print(str_value)

callme(str_value="Calling that function")

# Explanation
def empinfo(name, designation):
    print("Name:", name)
    print("Designation:", designation)

empinfo(name="ABC", designation="Dev")
# Variable Length Arguments

def callme(arg, *vartuple):
    print("India??")
    print(arg)
    for var in vartuple:
        print(var)

callme("Democracy", "or", "Gerontocracy")









