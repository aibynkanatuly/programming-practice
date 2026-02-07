# For loop with continue

# Example 1
for i in range(5):
    if i == 2:
        continue
    print(i)

# Example 2
for x in range(6):
    if x % 2 == 0:
        continue
    print(x)

# Example 3
for ch in "Python":
    if ch == "o":
        continue
    print(ch)

# Example 4
for i in range(1, 6):
    if i == 4:
        continue
    print(i)

# Example 5
for num in range(10):
    if num < 5:
        continue
    print(num)
