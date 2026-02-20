# All classes have a built-in method called __init__(), which is always executed when the class is being initiated
# The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)
print(p1.name)
print(p1.age) 

# Without the __init__() method, you would need to set properties manually for each object
# Create a class without __init__()
class Person:
  pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25
print(p1.name)
print(p1.age)

# You can also set default values for parameters in the __init__() method
# Set a default value for the age parameter
class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)

# Without self, python would not know which object's properties you want to access
# The self parameter links the method to the specific object
class Person:
  def __init__(self, name):
    self.name = name

  def printname(self):
    print(self.name)

p1 = Person("Tobias")
p2 = Person("Linus")

p1.printname()
p2.printname() 

# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any method in the class

# Access multiple properties using self
class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info() 

# Call one method from another method using self:
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet()
    print(message + "! Welcome to our website.")

p1 = Person("Tobias")
p1.welcome() 