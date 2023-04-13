def say_hello():
    print('Hello world!')


say_hello()



def print_max(a, b): # a, b -> параметри функції
    if a > b:
        print(f'{a} максимальне')
    elif a == b:
        print(f'{a} == {b}')
    else:
        print(f'{b} максимальне')


print_max(3, 4) # 3, 4 -> аргументи функції, пряма передача значень
x = 5
y = 7
print_max(x, y) # передача змінних в якості аргументів


# повернення результату


def add(a, b):
    return a + b


print(add(10, 15))
# user_input = input('Enter your age: ')

x = 50

def test_func():
    x = 2
    print('Заміна глобального х на', x)

test_func()
print('x все ще', x)


x = 50

def test_func():
    global x
    print('x ==', x)
    x = 2
    print('Заміна глобального х на', x)

test_func()
print('x ==', x)
