# порівняти дві дати народження двох людей
# дати народження будуть вводитись з консолі через функцію input
# потім будемо прокидувати дані в об'єкт datetime
from datetime import datetime

# 2004.11.28
# 2004.07.09

first = int(input('Input a year: '))
second = int(input('Input another year: '))

current_time = datetime.now()
if current_time.year - first > current_time.year - second:
    print(f'This human older {first}')
elif current_time.year - first == current_time.year - second:
    print(f'This people == ')
else:
    print(f'This people older {second}')
