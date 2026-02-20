nums = [1,2,3,4,5,6]

# 1) filter четные
even = list(filter(lambda x: x%2==0, nums))
print(even)

# 2) filter >3
gt3 = list(filter(lambda x: x>3, nums))
print(gt3)

# 3) filter <5
lt5 = list(filter(lambda x: x<5, nums))
print(lt5)

# 4) filter строк
words = ["apple","bat","cat"]
short = list(filter(lambda w: len(w)<=3, words))
print(short)

# 5) filter сложное условие
nums = [1,2,3,4,5,6]
filtered = list(filter(lambda x: x%2==0 and x>3, nums))
print(filtered)
