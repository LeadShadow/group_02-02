# В прошлую задачу добавим класс Owner — владельца собаки. У класса есть три атрибута:
# имя — name, возраст — age и адрес — address. Также необходимо реализовать метод info,
# который возвращает словарь с ключами 'name', 'age' и 'address', и значениями равными
# соответствующим свойствам экземпляра класса.
#
# Реализовать для класса Dog атрибут owner, который будет экземпляром класса Owner.
# Добавить в класс Dog метод who_is_owner, который возвращает результат вызова метода
# info у экземпляра класса Owner, т.е. словарь с ключами 'name', 'age' и 'address' владельца.

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Dog(Animal):
    def say(self):
        return 'Woof!'

    def __init__(self, breed, nickname, weight, owner):
        super().__init__(nickname, weight)
        self.breed = breed
        self.owner = owner

    def who_is_owner(self):
        return self.owner.info()


class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def info(self):
        return {'name': self.name, 'age': self.age, 'address': self.address}


owner = Owner('Sasha', 18, 'Keletskya 32')
dog = Dog('лабрадор', 'Rafik', 10, owner)
print(owner.info())
print(dog.who_is_owner())
