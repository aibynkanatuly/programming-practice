# 1) Позиционные аргументы
def greet(name, age):
    print(f"Hello {name}, you are {age} years old")
greet("Yeldar", 16)

# 2) Аргумент по умолчанию
def greet_default(name="Student"):
    print(f"Hello {name}!")
greet_default()
greet_default("Aigerim")

# 3) *args пример
def sum_all(*args):
    return sum(args)
print(sum_all(1,2,3,4,5))

# 4) **kwargs пример
def print_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Yeldar", course="Python")

# 5) Смешанные аргументы
def mixed(a, b=2, *args, **kwargs):
    print(a,b,args,kwargs)
mixed(1,3,5,6,name="Yeldar")
