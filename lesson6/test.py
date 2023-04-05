# int('a')
# print('name')
# print(10 / 0)


try:
    user_input = int(input('Enter your age: '))
except ValueError:
    print('У нас сталась помилка ValueError')
except ZeroDivisionError:
    print('Неможливе ділення на нуль')
else:
    print(f'Your age: {user_input}')
finally:
    print('Виконається в будь-якому випадку')



age = input('How old are you?: ')
try:
    age = int(age)
    if age >= 18:
        print('You are adult')
    else:
        print('You are infant yet')
except ValueError:
    print(f'{age} is not a number')

# ZeroDivisionError - ділення на нуль
# ValueError - виникає коли тип операнда підходить, але значення таке шо операцію неможливо виконати
# SyntaxError - синтаксична помилка
# IndentationError - помилка яка виникає якщо при виділенні блоків інструкцій пробілами допущена помилка
# TabError - виникає якщо в одному файлі використовувати пробіли і табуляції для виділення блоків інструкцій
# TypeError - виникає коли операція з змінною цього типу неможлива
print('a' * 3)
print(0.1 + 0.2) # 0.30000000000000004
print(0.1 + 0.2 == 0.3 + 0.0)  # False 101001010101011010101010101
print(0.3 + 0.0)