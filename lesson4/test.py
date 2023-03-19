is_nice = True
state = 'nice' if 30 > 20 else 'not nice'


some_data = None
msg = some_data or 'Не було повернено даних'  # False or True
print(msg)


x = int(input('X: '))
y = int(input('Y: '))

if x == 0:
    print("X can't be equal to zero")
    x = int(input('X: '))
    if x == 0:
        print("X can't be equal to zero")
        x = int(input('X: '))
        if x == 0:
            print("X can't be equal to zero")
            x = int(input('X: '))
            if x == 0:
                print("X can't be equal to zero")
                x = int(input('X: '))

result = y / x

