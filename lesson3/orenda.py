name = input('Enter your name: ')
age = int(input('Enter your age: '))
has_driver_license = input('Do you have driver license, enter(yes, no): ') # yes
money = int(input('Which you have money?: '))

if has_driver_license == 'yes':
    has_driver_license = True
else:
    has_driver_license = False

if name and age >= 18 and has_driver_license and money >= 1000:
    print(f'User {name} can rent a car')

