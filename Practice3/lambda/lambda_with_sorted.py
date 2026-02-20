names = ["Yeldar","Aigerim","Zhanerke"]

# 1) простая сортировка
sorted_names = sorted(names)
print(sorted_names)

# 2) по длине
sorted_len = sorted(names, key=lambda x: len(x))
print(sorted_len)

# 3) по первой букве
sorted_first = sorted(names, key=lambda x: x[0])
print(sorted_first)

# 4) обратный порядок
sorted_rev = sorted(names, reverse=True)
print(sorted_rev)

# 5) по последней букве
sorted_last = sorted(names, key=lambda x: x[-1])
print(sorted_last)
