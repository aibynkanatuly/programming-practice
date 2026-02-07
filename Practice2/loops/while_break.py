# While loop with break

# Example 1
i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1

# Example 2
x = 0
while True:
    print(x)
    if x == 2:
        break
    x += 1

# Example 3
num = 1
while num <= 10:
    if num == 7:
        break
    print(num)
    num += 1

# Example 4
i = 0
while i < 5:
    print(i)
    if i == 2:
        break
    i += 1

# Example 5
while True:
    print("Stop")
    break
