x = int(input('X: '))  # 0
y = int(input('Y: '))
# Неправильно!!!
# if x == 0:
#     print("X can't be equal to zero")
#     x = int(input('X: '))
#     if x == 0:
#         print("X can't be equal to zero")
#         x = int(input('X: '))
#         if x == 0:
#             print("X can't be equal to zero")
#             x = int(input('X: '))
#             if x == 0:
#                 print("X can't be equal to zero")
#                 x = int(input('X: '))

# result = y / x

# Правильно
while x == 0:  # 10 == 0
    print("X can't be equal to zero")
    x = int(input('X: '))

result = y / x
print(result)