# 1) Простейший lambda
square = lambda x: x**2
print(square(5))

# 2) Lambda с двумя аргументами
add = lambda a,b: a+b
print(add(3,4))

# 3) Lambda с условием
is_even = lambda x: x%2==0
print(is_even(6))

# 4) Lambda возвращает строку
greet = lambda name: f"Hello {name}"
print(greet("Yeldar"))

# 5) Lambda с списком
double = lambda lst: [x*2 for x in lst]
print(double([1,2,3]))
