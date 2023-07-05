file = open('test.txt', 'w')
file.write('first line\nsecond line\nthird line')
file.close()

file = open('test.txt', 'r')
lines = file.readlines()
print(lines)
file.close()


file = open('test.txt')
try:
    lines = file.readlines()
    print(lines)
finally:
    file.close()


with open('test.txt') as file:
    lines = file.readlines()
    print(lines)
