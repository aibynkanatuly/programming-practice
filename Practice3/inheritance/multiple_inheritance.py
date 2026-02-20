# 1) простое множественное наследование
class Flyer:
    def fly(self):
        print("Flying")
class Swimmer:
    def swim(self):
        print("Swimming")
class Duck(Flyer,Swimmer):
    pass
d=Duck()
d.fly()
d.swim()

# 2) множественное с методами
class A:
    def a(self):
        print("A")
class B:
    def b(self):
        print("B")
class C(A,B):
    pass
c=C()
c.a()
c.b()

# 3) super() в множественном наследовании
class X:
    def hello(self):
        print("X")
class Y:
    def hello(self):
        print("Y")
class Z(X,Y):
    def hello(self):
        super().hello()
z=Z()
z.hello()

# 4) добавление атрибута
class Flyer:
    def __init__(self):
        self.can_fly=True
class Swimmer:
    def __init__(self):
        self.can_swim=True
class Duck(Flyer,Swimmer):
    def __init__(self):
        Flyer.__init__(self)
        Swimmer.__init__(self)
d=Duck()
print(d.can_fly,d.can_swim)

# 5) комбинированные методы
class A:
    def action(self):
        print("A action")
class B:
    def action(self):
        print("B action")
class C(A,B):
    def action(self):
        A.action(self)
        B.action(self)
c=C()
c.action()
