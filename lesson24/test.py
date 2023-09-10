import collections
person = ('Sasha', 'Samus', 18, 'Pirogovo', '18')

Person = collections.namedtuple('Person', ['name', 'last_name', 'age', 'street', 'number_house'])
person1 = Person('Sasha', 'Samus', 18, 'Pirogovo', '18')
print(person1.name)
print(person1.last_name)


class Person:
    def __init__(self, name, last_name, age, street, number_house):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.street = street
        self.number_house = number_house


person = Person('Sasha', 'Samus', 18, 'Pirogovo', '18')
print(person.name)
print(person.last_name)
print(person.age)
print(person.street)
print(person.number_house)


sq = []
for i in range(1, 6):
    sq.append(i ** 2)

print(sq)

numbers = [i ** 2 for i in range(1, 6)]
print(sq == numbers)

sq = {i: i ** 2 for i in numbers}
print(sq)