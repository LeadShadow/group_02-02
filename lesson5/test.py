# цикл for
fruit = 'apple'

for char in fruit:
    print(char)


# цикл while
a = 1
while a <= 5:
    print(a)
    a = a + 1  # a = 1 + 1, a = 2 + 1, a = 3 + 1, a = 4 + 1, a = 5 + 1


a = 0
while True:
    print(a)
    if a >= 20:
        break
    a += 1


while True:
    user_input = input('Enter something (exit that quit): ') # exit
    print(user_input)
    if user_input == 'exit':  # 'exit' == 'exit'
        break


a = 0
while a < 6:
    a += 1
    if a % 2 == 0:  # (4 % 2 -> 0) 0 == 0
        continue
    print(a)
# 2 4 6 8
# 1 3 5 7 9

while True:
    number = int(input('number: ')) # '18' -> 18
    if number < 0:
        break
    while True:
        print(number)
        number -= 1
        if number < 0:
            break
