# 1) переопределение метода
class Animal:
    def speak(self):
        print("Some sound")
class Dog(Animal):
    def speak(self):
        print("Woof!")
d=Dog()
d.speak()

# 2) вызов родительского метода
class Animal:
    def speak(self):
        print("Animal sound")
class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof!")
d=Dog()
d.speak()

# 3) override с __init__
class Person:
    def __init__(self,name):
        self.name=name
class Student(Person):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
s=Student("Yeldar",16)
print(s.name,s.age)

# 4) override с добавлением метода
class Animal:
    def info(self):
        print("Animal")
class Dog(Animal):
    def info(self):
        print("Dog")
d=Dog()
d.info()

# 5) комбинированный override
class A:
    def greet(self):
        print("Hello from A")
class B(A):
    def greet(self):
        print("Hello from B")
b=B()
b.greet()
