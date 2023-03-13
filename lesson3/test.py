# в Пайтоні існує три методи управління потоком виконання
# 1 умовне виконання -> виконання блоку інструкцій при наступленні якоїсь умови
# 2 цикли -> повторення блока інструкцій поки виконується якась умова
# 3 винятки -> виконання блоку інструкцій якщо буде помилка


age = input('How old are you?: ')

if int(age) >= 18:
    print('You are adult already')
else:
    print('You are infant yet')


# Правила приведення до bool(True or False(1, 0))

# 1 Число 0 завжди приводиться до False, коли в умові фолс, вона ніколи не виконається!!!
money = 1000
if money:
    print(f'You have {money} on your bank account')
else:
    print('You have no money and no debts')

# 2 Число None приводиться до False
result = None
if result:
    print(result)
else:
    print('Box is None, do something')

# 3 Пустий контейнер(пустий рядок і тд тп) приводяться до False
user_name = input('Enter your name: ')

if user_name:
    print(f'Hello {user_name}')
else:
    print('Hi Anonym!')

