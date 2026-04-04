# math.py

import math
import random

# Built-in math functions
numbers = [4, 9, -3, 7]

print("Min:", min(numbers))
print("Max:", max(numbers))
print("Absolute:", abs(-10))
print("Round:", round(3.567, 2))
print("Power:", pow(2, 3))

# math module
print("Square root:", math.sqrt(16))
print("Ceil:", math.ceil(3.2))
print("Floor:", math.floor(3.8))
print("Pi:", math.pi)
print("Euler:", math.e)

# random module
print("Random number:", random.random())
print("Random integer:", random.randint(1, 10))

list_items = ["apple", "banana", "cherry"]
print("Random choice:", random.choice(list_items))

random.shuffle(list_items)
print("Shuffled list:", list_items)