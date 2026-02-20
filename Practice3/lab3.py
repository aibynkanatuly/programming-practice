# # 301
# def valid_number(x):
#    valid = False
   
#    for i in str(x): 
#       if int(i) % 2 != 0: break
#    else: valid = True
   
#    return valid

# num = int(input())

# if valid_number(num): print("Valid")
# else: print("Not valid")

# # 302
# def isUsual(num):
#    if num <= 0:
#       return False
#    for prime in (2, 3, 5):
#       while num % prime == 0:
#          num //= prime    
#    return num == 1

# n = int(input())
# print("Yes" if isUsual(n) else "No")

# # 303
# s, a, b = input(), '', ''
# def arithmetic_operation(x, y):
#    f_number, s_number = "", ""
   
#    for i in range(0, len(x), 3): f_number += str(dict_of_numbers[x[i: i+3]])
#    for i in range(0, len(y), 3): s_number += str(dict_of_numbers[y[i: i+3]])
   
#    if '+' in s: return int(f_number) + int(s_number)
#    elif '-' in s: return int(f_number) - int(s_number)
#    elif '*' in s: return int(f_number) * int(s_number)

# dict_of_numbers = {"ONE": 1, "TWO": 2, "THR": 3, "FOU": 4, "FIV": 5, "SIX": 6, "SEV": 7, "EIG": 8, "NIN": 9, "ZER": 0}
# reverse = {value: key for key, value in dict_of_numbers.items()}

# if '+' in s:
#    a, b = s.split('+')
#    res = arithmetic_operation(a, b)
# elif '-' in s:
#    a, b = s.split('-')
#    res = arithmetic_operation(a, b)
# elif '*' in s:
#    a, b = s.split('*')
#    res = arithmetic_operation(a, b)
# else:
#    for i in range(0, len(s), 3):
#       res += str(dict_of_numbers[s[i: i+3]])

# str_res = ''
# for i in str(res):
#    str_res += reverse[int(i)]
# print(str_res)

# # 304
# class StringHandler:
#    def getString(self):
#       self.text = input()
      
#    def printString(self):
#       print(self.text.upper())

# s = StringHandler()
# s.getString()
# s.printString()

# # 305
# class Shape:
#    def area(self):
#       return 0

# class Square(Shape):
#    def __init__(self, length):
#       self.length = length
   
#    def area(self):
#       return self.length ** 2
   
# square = Square(int(input()))
# print(square.area())
# # 306
# class Shape:
#    def area(self):
#       return 0

# class Rectangle(Shape):
#    def __init__(self, length, width):
#       self.length = length
#       self.width = width

#    def area(self):
#       return self.length * self.width

# a, b = input().split()
# s = Rectangle(int(a), int(b))
# print(s.area())

# # 307
# import math

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def show(self):
#         print(f"({self.x}, {self.y})")

#     def move(self, new_x, new_y):
#         self.x = new_x
#         self.y = new_y

#     def dist(self, other_point):
#         return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

# x1, y1 = map(int, input().split())
# new_x, new_y = map(int, input().split())
# x2, y2 = map(int, input().split())

# p1 = Point(x1, y1)
# p1.show()
# p1.move(new_x, new_y)
# p1.show()
# p2 = Point(x2, y2)

# distance = p1.dist(p2)
# print(f"{distance:.2f}")

# # 308
# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             return self.balance
#         else:
#             return "Insufficient Funds"

# balance, withdrawal = map(int, input().split())
# acc = Account("Nurmukhamed", balance)
# print(acc.withdraw(withdrawal))

# # 309
# class Circle:
#    def __init__(self, radius):
#       self.radius = radius

#    def area(self):
#       return (self.radius**2) * 3.14159

# n = int(input())
# s = Circle(n)
# print(f"{s.area():.2f}")

# # 310
# class Person:
#    def __init__(self, name):
#       self.name = name

# class Student(Person):
#    def __init__(self, name, gpa):
#       super().__init__(name)
#       self.gpa = gpa
   
#    def display(self):
#       return f"Student: {self.name}, GPA: {self.gpa}"

# name, gpa = input().split()
# stud = Student(name, gpa)

# print(stud.display())

# # 311
# class Pair:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def add(self, other):
#         return Pair(self.a + other.a, self.b + other.b)

# a1, b1, a2, b2 = map(int, input().split())
# p1 = Pair(a1, b1)
# p2 = Pair(a2, b2)
# result = p1.add(p2)
# print(f"Result: {result.a} {result.b}")

# # 312
# class Employee:
#     def __init__(self, name, base_salary):
#         self.name = name
#         self.base_salary = base_salary

#     def total_salary(self):
#         return self.base_salary


# class Manager(Employee):
#     def __init__(self, name, base_salary, bonus_percent):
#         super().__init__(name, base_salary)
#         self.bonus_percent = bonus_percent

#     def total_salary(self):
#         return self.base_salary * (1 + self.bonus_percent / 100)


# class Developer(Employee):
#     def __init__(self, name, base_salary, completed_projects):
#         super().__init__(name, base_salary)
#         self.completed_projects = completed_projects

#     def total_salary(self):
#         return self.base_salary + self.completed_projects * 500


# class Intern(Employee):
#     pass

# data = input().split()

# role = data[0]

# if role == "Manager":
#     _, name, base_salary, bonus_percent = data
#     employee = Manager(name, int(base_salary), int(bonus_percent))

# elif role == "Developer":
#     _, name, base_salary, completed_projects = data
#     employee = Developer(name, int(base_salary), int(completed_projects))

# elif role == "Intern":
#     _, name, base_salary = data
#     employee = Intern(name, int(base_salary))


# print(f"Name: {employee.name}, Total: {employee.total_salary():.2f}")

# # 313
# nums = list(map(int, input().split()))
# is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
# primes = list(filter(is_prime, nums))

# if primes:
#     print(*primes)
# else:
#     print("No primes")

# # 314
# n = int(input())
# arr = list(map(int, input().split()))
# q = int(input())

# for i in range(q):
#     op = input().split()
    
#     if op[0] == "add":
#         x = int(op[1])
#         arr = list(map(lambda a: a + x, arr))
#     elif op[0] == "multiply":
#         x = int(op[1])
#         arr = list(map(lambda a: a * x, arr))
#     elif op[0] == "power":
#         x = int(op[1])
#         arr = list(map(lambda a: a ** x, arr))
#     elif op[0] == "abs":
#         arr = list(map(lambda a: abs(a), arr))

# print(*arr)