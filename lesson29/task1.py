# Создайте класс Dog, родительским классом которого является класс Animal.
# В классе Dog выполните переопределение метода say, чтобы он возвращал строку
# "Woof" для экземпляров класса Dog.
#
# В конструкторе класса Dog введите новое свойство breed — порода, при этом должны
# остаться все свойства, наследуемые от класса Animal.
#
# Создайте в коде следующий экземпляр класса Dog.
#
# dog = Dog("Barbos", 23, "labrador")

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

    def __init__(self, breed, nickname, weight):
        super().__init__(nickname, weight)
        self.breed = breed


class Cat(Animal):
    def say(self):
        return 'Meow!'

    def __init__(self, breed, nickname, weight):
        super().__init__(nickname, weight)
        self.breed = breed


dog = Dog('ретрівер', 'Tom', 15)
print(dog.breed)
print(dog.nickname)
print(dog.weight)
print(dog.say())
dog.change_weight(17)
print(dog.weight)
cat = Cat('шотландець', 'Lesya', 3)
print(cat.breed)
print(cat.nickname)
print(cat.weight)
print(cat.say())
cat.change_weight(4)
print(cat.weight)
