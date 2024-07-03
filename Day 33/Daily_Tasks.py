# Class
# The class is a blueprint that defines the nature of a future object. A class is a collection of objects 
class MyClass():
     "This is a DocString" 
     x = 5 
MyClass = MyClass() 
print(MyClass) 
print(MyClass.x) 
print(MyClass.__doc__) 
# Object
# An instance is a specific object created from a particular class. 
class MyClass():
    x = 5 
    def myFunction(): 
        print('Hello') 
my_object = MyClass() 
print(my_object.x) 
print(MyClass.myFunction) 
print(my_object.myFunction)
# Polymorphism 
# Poly means 'many' and Morphism means 'forms'. In Polymorphism, the functions are of the same name but their functionalities are different

class Jasmine():
    def color(self):
        print("Jasmine flower comes in white, pink, blue, orange, yellow, purple, and red color")
    
    def scientific_name(self):
        print("Jasminum sambac is the scientific name of Jasmine")
    
    def family(self):
        print("Jasmine is from the Oleaceae family")

class Lily():
    def color(self):
        print("Lilies commonly grow in white, yellow, pink, red, and orange color.")
    
    def scientific_name(self):
        print("Lilium is the scientific name of Lily")
    
    def family(self):
        print("Lily is from the Liliaceae family")

obj_jasmine = Jasmine()
obj_lily = Lily()

for flower in (obj_jasmine, obj_lily):
    flower.color()
    flower.scientific_name()
    flower.family()
# Inheritance
# By using inheritance, we can create a class that uses all the properties and behavior of another class. In Inheritance we have a parent and a child class, as in real life a child inherits the characteristics of his/her parents, likewise, child class has properties of the parent class.

class Flower:
    def color(self):
        print("Flowers are found in various colors")

    def scientific_name(self):
        print("These are some Binomial nomenclature for categorize species")

    def family(self):
        print("Every flower has a family")

    def odour(self):
        print("Every flower has its own odour by which it can be identified")

class Jasmine(Flower):
    def color(self):
        print("Jasmine flower comes in white, pink, blue, orange, yellow, purple, and red color")

    def scientific_name(self):
        print("Jasminum sambac is the scientific name of Jasmine")

    def family(self):
        print("Jasmine is from the Oleaceae family")

class Lily(Flower):
    def color(self):
        print("Lilies commonly grow in white, yellow, pink, red, and orange color.")

    def scientific_name(self):
        print("Lilium is the scientific name of Lily")

    def family(self):
        print("Lily is from the Liliaceae family")

obj_Flower = Flower()
obj_jasmine = Jasmine()
obj_lily = Lily()

obj_Flower.color()
obj_Flower.scientific_name()
obj_Flower.family()
obj_Flower.odour()

obj_jasmine.color()
obj_jasmine.scientific_name()
obj_jasmine.family()
obj_jasmine.odour()

obj_lily.color()
obj_lily.scientific_name()
obj_lily.family()
obj_lily.odour()

# Encapsulation
# Encapsulation refers to restricting access. This is how we can wrap up and remove unnecessary data. So basically, Encapsulation is the process of using private variables within classes to prevent unintentional modification of data.

class myClass(object):
    def __init__(self):
        self.a = 123  # public variable
        self._b = 123  # protected variable
        self.__c = 123  # private variable, double underscore

obj = myClass()
print(obj.a)  # accessible, public variable
print(obj._b)  # accessible, protected variable
print(obj.__c)  # not accessible, will raise an AttributeError

# Private variables are intended to be changed using getter and setter methods. These provide indirect access to them.
class myClass(object):
    def __init__(self):
        self.__version = 22  # private variable, double underscore

    def getVersion(self):
        print(self.__version)

    def setVersion(self, version):
        self.__version = version

obj = myClass()
obj.getVersion()  # This will print 22
obj.setVersion(23)
obj.getVersion()  # This will print 23

# Accessing the private variable directly will result in an AttributeError
# print(obj.__version)  # Uncommenting this line will raise an AttributeError

# Accessing the mangled private variable
print(obj._myClass__version)  # This will print 23



