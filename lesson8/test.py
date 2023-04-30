# Змінна кількість параметрів
import kivy

# def say(message):
#     return f'Hi {message}'
#
#
# print(say('Віталій', 'Самусь'))


# (1, 2, 3, 4, 5)
def total(a=5, *numbers, **phone_book):
    print(f'a == {a}')
    # прохід по всіх елементах кортежу
    print(numbers)
    for item in numbers:
        print(f'item == {item}')

    # прохід по всіх елементах словника
    print(phone_book)
    for first, second in phone_book.items():
        print(first, second)



total(10, 1, 2, 3, Sasha=1123, Misha=1028, Bob=2034)
# {
# 'name': 'Oleksandr'
# }

# Кортеж -> це впорядковані незмінні множини елементів
a = (1, 2, 3)
print(a[0])

my_tuple1 = tuple()
my_tuple2 = ()
print(my_tuple1, my_tuple2)


# Словник -> це контейнер який зберігає пари ключ-значення

empty_dict1 = dict()
empty_dict2 = {}
print(empty_dict1, empty_dict2)


some_dict = {
    'key': 'value',
    1: 'one',
}

print(some_dict)

some_dict[2] = 'two'
print(some_dict)