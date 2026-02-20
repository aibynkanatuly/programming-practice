numbers = [1,2,3,4,5]

# 1) map с lambda
squared = list(map(lambda x: x**2, numbers))
print(squared)

# 2) map с несколькими списками
a = [1,2,3]
b = [4,5,6]
sum_list = list(map(lambda x,y: x+y, a,b))
print(sum_list)

# 3) map с str
words = ["python","java"]
lengths = list(map(lambda w: len(w), words))
print(lengths)

# 4) map с float
nums = [1.1,2.2,3.3]
rounded = list(map(lambda x: round(x), nums))
print(rounded)

# 5) map + условие
nums = [1,2,3,4]
even_squared = list(map(lambda x: x**2 if x%2==0 else x, nums))
print(even_squared)
