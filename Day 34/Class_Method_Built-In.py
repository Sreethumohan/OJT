# getattr(obj, name[, default]) : to access the attribute of object. hasattr(obj,name) : to check if an attribute exists or not. setattr(obj,name,value) : to set an attribute. If the attribute does not exist, then it would be created. delattr(obj, name) : to delete an attribute.

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

# Create an instance of the Student class
Student1 = Student("A", 21, "A")

# Check if the 'age' attribute exists
print(hasattr(Student1, "age"))  # Output: True

# Check if the 'marks' attribute exists
print(hasattr(Student1, "marks"))  # Output: False

# Set the 'marks' attribute
setattr(Student1, "marks", "75")

# Check if the 'marks' attribute exists now
print(hasattr(Student1, "marks"))  # Output: True

# Get the 'grade' attribute
print(getattr(Student1, "grade"))  # Output: A

# Get the 'name' attribute
print(getattr(Student1, "name"))  # Output: A

# Delete the 'marks' attribute
delattr(Student1, "marks")

# Check if the 'marks' attribute still exists
print(hasattr(Student1, "marks"))  # Output: False
