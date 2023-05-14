# структури даних


# 1 впорядкованість
# 2 змінність
# 3 унікальність


# списки

my_list = list()
my_list1 = []


not_empty = [1, 2, 'user']
print(not_empty)

iterable = ['a', 'b', 'c']
first_letter = iterable[0]
middle_letter = iterable[1]
last_letter = iterable[2]

print(first_letter, middle_letter, last_letter)

print(iterable)
iterable[1] = 'x'
print(iterable)


some_str = 'This is awesome string'
first_five = some_str[0:5]
print(first_five)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = numbers[0:10:2]
even_numbers = numbers[1:10:2]
three_numbers = numbers[2:10:3]
print(odd_numbers, even_numbers, three_numbers)

numbers_copy = numbers[:]
print(numbers_copy == numbers)

odd_numbers = numbers[::2]
even_numbers = numbers[1::2]
three_numbers = numbers[2::3]
print(odd_numbers, even_numbers, three_numbers)

# append
letters = ['a', 'b']
letters.append('c')
print(letters)

# clear
num = [1, 2]
num.clear()
print(num)

# remove
chars = ['a', 'b']
chars.remove('b')
print(chars)

# pop
chars = ['a', 'b']
last = chars.pop(1)
print(chars)
print(last)

# extend
chars = ['a', 'b']
numbers = [1, 2]

chars.extend(numbers)
print(chars)

# insert

chars = ['a', 'b']
chars.insert(1, 'c')
print(chars)

# index
chars = ['a', 'b', 'c', 'd', 'c']
c_indx = chars.index('c')
print(c_indx)

# count
chars = ['a', 'b', 'c', 'a', 'd', 'a']
a_count = chars.count('a')
print(a_count)

# sort
chars = ['x', 'y', 'a', 'd', 'c', 'n', 'm']
chars.sort()
print(chars)

# reverse
chars.reverse()
print(chars)


# copy
chars = ['a', 'b']
chars_copy = chars.copy()
print(chars == chars_copy)


# словники dict
# Ваше ім'я: Олександр

users = [
    {
        'name': 'Oleksandr',
        'age': 18
    },
    {
        'name': 'Kyryl',
        'age': 11
    },
    {
        'name': 'David',
        'age': 11
    },
    {
        'name': 'Maksym',
        'age': 11
    }
]

# pop
chars = {'a': 1, 'b': 2}
b_num = chars.pop('b')
print(b_num)
print(chars)

# update(another_dict)
chars = {'a': 1, 'b': 2}
chars.update({'c': 3})
print(chars)

# clear()
chars = {'a': 1, 'b': 2}
chars.clear()
print(chars)

# copy
chars = {'a': 1, 'b': 2}
chars_copy = chars.copy()
print(chars_copy == chars)

# get(key[,default]) - default=None
chars = {'a': 1, 'b': 2}
c_idx = chars.get('b', -1)
print(c_idx)
print(chars)

