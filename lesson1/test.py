x = 20
y = 10
container_for_money = 100

# 1 ім'я змінної в пайтоні може бути тільки з цифр букв і знаків підчеркування _
a_1 = 20

# 2 ім'я змінної не може починатись з цифри, але може з нижнього знаку підчеркування
_a = 20

# 3 використання зарезервованих слів в якості назви змінної буде приводити до помилки
# False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else,
# except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise,
# return, try, while, with, yield
if_ = 30

# Оператори і операнди

# оператори -> математичні дії + - * / // % **
# операнди -> змінні(числа) x, y
print(x + y)  # 30
print(x - y)  # 10
print(x * y)  # 200
print(x / y)  # 2.0
print(x // y)  # 2
print(x % y)  # 0
print(x ** 2)  # 20 * 20 -> 400

# Типи даних

# 1 None -> пустий тип
b = None

# 2 Числа -> цілі числа, дробові числа, комплексні числа(int(integer(1, 43, 645, 123, 5345)), float(10.1, 12.3, 1321.312), complex(3j))

# 3 Bool(Boolean) -> булевий(логічний тип) True or False(правда або брехня) -> 1 or 0

# 4 Рядки(str(string)) -> текст в лапках
print('hello world')


# Рядки
hello = 'hello world'
print(hello[1])
s1 = 'Hello,'
s2 = 'World!'
print(s1 + s2)
name = 'Sasha'

print(f'Hello, {name}')  # f'Hello, Sasha'  Hello, Sasha  Hello, name
# '232' -> рядок
# 232 -> число
print(int('20') + int('10'))  # 2010  int('10') -> 10

# Приведення типів (int, float, bool, str)
