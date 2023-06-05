from pathlib import Path
a = 'didn\'t'  # didn't

# рядки - це незмінна впорядкована послідовність символів

s = 'Hello world'

# upper() -> всі символи в верхній регістр
s = 'Hello'
print(s.upper())


# lower() -> всі символи в нижній регістр
s = 'HELLO'
print(s.lower())


# startswith() -> щоб перевірити чи рядок починається з підрядка
s = 'Bill Jons'
print(s.startswith('Bi'))


# endswith() -> перевірити чи рядок закінчується підрядком
s = 'hello.jpeg'
print(s.endswith('.jpeg'))


# list, dict, set, tuple, str
# 1 перевірка на входження
# 2 кількість елементів
# 3 перебір всіх елементів в циклі for


# 1 перевірка на входження
password = 'qwerty123'
if 'sasha' in password or '123' in password:
    print('This password is too weak!')


numbers = [1, 2, 3, 4, 5]
for i in numbers:
    if i in (1, 2, 3):
        print(i)

prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23}
is_prime = 3 in prime_numbers
print(is_prime)


# 2 кількість елементів
password = input('Password: ')
if len(password) < 8:
    print('Your password is too short')
else:
    print('Ok)')


alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for char in alphabet:
    print(char)


# Пакет pathlib
p = Path('C:/Users/pc/Desktop/заняття/group_02-02/lesson13')

print(p.parent)
print(p.name)
print(p.suffix)
print(p.exists())
print(p.is_dir())
print(p.is_file())
for i in p.iterdir():
    print(i.name)