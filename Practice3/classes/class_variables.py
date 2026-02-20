# 1) class variable
class Dog:
    species="Canine"
d1=Dog()
print(d1.species)

# 2) instance variable
class Dog:
    def __init__(self,name):
        self.name=name
d2=Dog("Rex")
print(d2.name)

# 3) class variable изменяемый
class Dog:
    count=0
    def __init__(self,name):
        self.name=name
        Dog.count+=1
d1=Dog("Rex")
d2=Dog("Max")
print(Dog.count)

# 4) class и instance переменные вместе
class Dog:
    species="Canine"
    def __init__(self,name):
        self.name=name
d=Dog("Rex")
print(d.name,d.species)

# 5) доступ к class variable через экземпляр
class Dog:
    species="Canine"
d=Dog()
print(d.species)
