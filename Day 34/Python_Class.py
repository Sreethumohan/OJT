# Python Class

class Student: 
    """
    This is a class for creating Student objects.
    """
    def __init__(self, name, age, grade): 
        self.name = name 
        self.age = age 
        self.grade = grade

# Create an instance of the Student class
student1 = Student('Neeraj', 12, 'A') 

# Access the attributes of the student1 object
print(student1.name)   # Output: Neeraj
print(student1.age)    # Output: 12
print(student1.grade)  # Output: A

# Special class attributes
# __dict__: Dictionary containing the class's namespace.
# __doc__: Class documentation string or None if undefined.
# __name__: Class name.
# __module__: Module name in which the class is defined. This attribute is "__main__" in interactive mode.
# __bases__: A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.

print(Student.__doc__)     # Output: This is a class for creating Student objects.
print(Student.__name__)    # Output: Student
print(Student.__module__)  # Output: __main__ (if run as a script)
print(Student.__bases__)   # Output: (<class 'object'>,)
print(Student.__dict__)    # Output: dictionary containing class-level attributes and methods

# Create more instances of the Student class
student2 = Student("A", 1, "A") 
student3 = Student("B", 2, "B")

# Delete the instances
del student2
del student3


# Functions in Classes

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def displayStudent(self):
        return "Student name is " + self.name + " and age is " + str(self.age)

# Create an instance of the Student class
student1 = Student("BOB", 21, "A")

# Call the displayStudent method and print the result
print(student1.displayStudent())
