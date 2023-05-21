numbers = {
    1: "one",
    2: "two",
    3: "three"
}

for key in numbers.values():
    print(key)


for key, value in numbers.items():
    print(key, value)


# множина
a = set()
print(a)

a = set('hello')
print(a)

b = {1, 2, 3, 4}
print(b)

numbers = {1, 2, 3, 1, 2, 3, 3, 2}
print(numbers)


# add(item) - додає елемент в множину
numbers = {1, 2, 3}
numbers.add(4)
print(numbers)

# remove(item) -> видаляє елемент з множини, буде помилка, якщо такого елементу немає
numbers = {1, 2, 3}
numbers.remove(3)
print(numbers)

# discard(item) -> видаляє елемент з множини, не викликає помилки, якщо такого елементу немає
numbers = {1, 2, 3}
numbers.discard(3)
print(numbers)


a = set('hello')
print(a)

b = set('hi there!')
print(b)

# спільні елементи двох множин
print(a & b)


# всі елементи з двох множин окрім спільних
print(a ^ b)

# об'єднаємо елементи двох множин
print(a | b)

points = {
    (0, 0): '0',
    (1, 1): '1',
    (2, 2): '2'
}

not_empty = (1, 2, 3, 4, 5)


print(points)
# points1 = {
#     [0, 0]: '0',
#     [1, 1]: '1',
#     [2, 2]: '2'
# }