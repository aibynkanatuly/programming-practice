# 1) Простейшая функция без аргументов
def greet():
    print("Hello, Yeldar!")

greet()

# 2) Функция с одним аргументом
def square(x):
    return x**2

print(square(5))

# 3) Функция с двумя аргументами
def add(a, b):
    return a + b

print(add(3, 7))

# 4) Функция с возвратом нескольких значений
def min_max(numbers):
    return min(numbers), max(numbers)

print(min_max([1,5,3,9]))

# 5) Функция с документированием
def multiply(a, b):
    """Возвращает произведение двух чисел"""
    return a * b

print(multiply(4,6))
