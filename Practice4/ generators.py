# generators.py

# ---------- ITERATOR EXAMPLE ----------

numbers = [1, 2, 3, 4, 5]

my_iter = iter(numbers)

print("Iterator example:")
print(next(my_iter))
print(next(my_iter))


# ---------- CUSTOM ITERATOR ----------

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

print("\nCustom iterator:")
my_class = MyNumbers()
for x in my_class:
    print(x)


# ---------- GENERATOR FUNCTION ----------

def my_generator():
    for i in range(5):
        yield i

print("\nGenerator function:")
for value in my_generator():
    print(value)


# ---------- GENERATOR EXPRESSION ----------

print("\nGenerator expression:")
gen_exp = (x * x for x in range(5))
for num in gen_exp:
    print(num)