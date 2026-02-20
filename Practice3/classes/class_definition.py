# 1) простой класс
class Student:
    def __init__(self,name):
        self.name = name
s = Student("Yeldar")
print(s.name)

# 2) класс с двумя атрибутами
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p = Person("Yeldar",16)
print(p.name,p.age)

# 3) класс с методом
class Calculator:
    def add(self,a,b):
        return a+b
calc = Calculator()
print(calc.add(3,4))

# 4) класс с print внутри метода
class Greeter:
    def greet(self,name):
        print(f"Hello {name}")
g = Greeter()
g.greet("Yeldar")

# 5) класс с конструктором и методом
class Dog:
    def __init__(self,name):
        self.name=name
    def bark(self):
        print(f"{self.name} says Woof!")
d=Dog("Rex")
d.bark()
