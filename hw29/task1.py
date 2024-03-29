# Создайте два класса: CatDog и DogCat. Эти классы должны наследоваться от двух классов сразу:
# Cat и Dog. После наследования у экземпляра класса CatDog, родительский метод say должен
# возвращать "Meow", а у класса DogCat — "Woof". Для обоих указанных классов реализуйте метод
# info, который возвращает строку в следующем формате f"{self.nickname}-{self.weight}".

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


class Cat(Animal):
    def say(self):
        return "Meow"


class Dog(Animal):
    def say(self):
        return "Woof"


class CatDog(Cat, Dog):
    def __call__(self, *args, **kwargs):
        return f'{self.nickname}-{self.weight}'


class DogCat(Dog, Cat):
    def __call__(self, *args, **kwargs):
        return f'{self.nickname}-{self.weight}'


catdog = CatDog('Tom', 4)
print(catdog())
print(catdog.say())
dogcat = DogCat('Barsik', 10)
print(dogcat.say())
print(dogcat())
