#6. Create a class called Person with attributes for name, age, and email. 
# Implement validation to ensure that age is a positive integer and email follows a valid format.
import re

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age if isinstance(age, int) and age > 0 else None
        self.email = email if re.match(r"[^@]+@[^@]+\.[^@]+", email) else None

person1 = Person("Alice", 25, "alice@example.com")
person2 = Person("Bob", -30, "bob@example")
person3 = Person("Charlie", 35, "charlie@example.com")

print(person1.name, person1.age, person1.email) 
print(person2.name, person2.age, person2.email)
print(person3.name, person3.age, person3.email)