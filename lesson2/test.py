# 1 Присвоїти змінній значення True або False
a = True
b = False

# 2 Присвоїти змінній результат виконання логічного виразу наприклад порівняння
age = 18
adult = age >= 18  # 18 >= 18
print(adult)

a = 3
b = 5
c = a < b  # True
d = a > b  # False
g = a == b # False
h = a != b # True

print('Hello World!')
user_input = input('Input your age: ')
print(type(user_input)) # '18'
# print(user_input > 18)  'Саша' > 18
# '18'
age = int(user_input)  # int('18') -> 18
print(type(age))  # 18
print(age == 18)

# Приведення типів (int, float, bool, str)
pi = '3.14'
# 2 piR, pi -> 3.14, R = якесь рандомне значення
pi = float(pi)
print(pi)
