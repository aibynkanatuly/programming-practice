# 1) простой наследник
class Animal:
    def speak(self):
        print("Animal sound")
class Dog(Animal):
    pass
d=Dog()
d.speak()

# 2) наследник с методом
class Animal:
    def speak(self):
        print("Animal sound")
class Cat(Animal):
    def meow(self):
        print("Meow")
c=Cat()
c.speak()
c.meow()

# 3) наследование __init__
class Animal:
    def __init__(self,name):
        self.name=name
class Dog(Animal):
    pass
d=Dog("Rex")
print(d.name)

# 4) наследник добавляет атрибут
class Animal:
    def __init__(self,name):
        self.name=name
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
d=Dog("Rex","Bulldog")
print(d.name,d.breed)

# 5) метод переопределение
class Animal:
    def speak(self):
        print("Some sound")
class Dog(Animal):
    def speak(self):
        print("Woof!")
d=Dog()
d.speak()
