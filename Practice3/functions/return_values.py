# 1) Простейший return
def add(a,b):
    return a+b
print(add(2,3))

# 2) Return кортежа
def min_max(numbers):
    return min(numbers), max(numbers)
print(min_max([1,4,7,2]))

# 3) Return списка
def double_list(lst):
    return [x*2 for x in lst]
print(double_list([1,2,3]))

# 4) Return словаря
def make_dict(keys, values):
    return dict(zip(keys, values))
print(make_dict(["a","b"],[1,2]))

# 5) Return с условием
def check_even(num):
    if num%2==0:
        return True
    else:
        return False
print(check_even(5))
