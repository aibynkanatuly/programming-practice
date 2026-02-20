# 1) super() вызов родителя
class Animal:
    def __init__(self,name):
        self.name=name
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
d=Dog("Rex","Bulldog")
print(d.name,d.breed)

# 2) super() метод
class Animal:
    def speak(self):
        print("Animal sound")
class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof!")
d=Dog()
d.speak()

# 3) super() с дополнительным методом
class A:
    def greet(self):
        print("Hello from A")
class B(A):
    def greet(self):
        super().greet()
        print("Hello from B")
b=B()
b.greet()

# 4) super() __init__ с аргументами
class A:
    def __init__(self,x):
        self.x=x
class B(A):
    def __init__(self,x,y):
        super().__init__(x)
        self.y=y
b=B(5,10)
print(b.x,b.y)

# 5) super() в многоуровневом наследовании
class A:
    def hi(self):
        print("A")
class B(A):
    def hi(self):
        super().hi()
        print("B")
class C(B):
    def hi(self):
        super().hi()
        print("C")
c=C()
c.hi()
