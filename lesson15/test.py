import re
# десятковий формат
# двійковому форматі
# шістнадцятковому форматі
# науковою анотацією
# з фіксованою точністю
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f
# 0, 1, 2, 3, 4, 5, 6, 7,
# 0 1 10 11 100
for i in range(16):
    s = "int: {0:d}; hex: {0:#x}; oct: {0:#o}; bin: {0:#b}".format(i)
    print(s)


width = 5
for num in range(12):
    print('| {:>10} | {:>10} | {:>10} |'.format(num, num ** 2, num ** 3))  # 2, 4, 8


s = 'I am 18 years old 25'
age = re.search('\d+', s)
print(age.group())

s = 'I bought 7 nuts for 6$ and 10 bolts for 3$'
numbers = re.findall('\d+', s)
print(numbers)
