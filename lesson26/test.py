from functools import reduce
a = [1, 2, 3, 4, 5]  # 1 * 1, 2 * 2, 3 * 3, 4 * 4, 5 * 5


# map
def square(x):
    return x ** 2


squared_numbers = map(square, a)
print(list(squared_numbers))


# filter
# filter(function, iterable)


def is_even(x):
    return x % 2 == 0


even_numbers = filter(is_even, a)
print(list(even_numbers))


# reduce
# reduce(function, iterable(, initializer))

def add(x, y):
    return x + y


total_sum = reduce(add, a)
print(total_sum)
