from collections import UserList
class User:
    name = 'Sasha'
    age = 18


user1 = User()
print(user1.name)
print(user1.age)
user2 = User()
user2.name = 'Misha'
user2.age = 16
print(user2.name)
print(user2.age)


class User:
    name = 'Sasha'
    age = 18

    def say_name(self):
        print(f'Hi I am {self.name} and I am {self.age} years old')

    def set_age(self, age):
        self.age = age


user3 = User()
print(user3.name)
print(user3.age)
user3.say_name()
user3.set_age(19)
print(user3.age)
user3.say_name()

print(10 + 10)  # 10__add__10


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


person1 = Person('Oleksandr', 18)
print(person1.name)
print(person1.age)


class Human:
    def __init__(self, name: str):
        self.name = name

    def voice(self):
        print(f'Hello! My name is {self.name}')


class Developer(Human):
    language = ''

    def __init__(self, field_description: str, name: str):
        super().__init__(name)
        self.field_description = field_description

    def make_some_code(self):
        return f'{self.field_description} on {self.language}'


class PythonDeveloper(Developer):
    language = 'Python'


class JSDeveloper(Developer):
    language = 'JS'


python_dev = PythonDeveloper('I am making some code', 'Sasha')
print(python_dev.make_some_code())
python_dev.voice()
js_dev = JSDeveloper('I am making some code', 'Slava')
print(js_dev.make_some_code())
js_dev.voice()


class Human:
    name = 'Sasha'


class Sasha(Human):
    def voice(self):
        print(self.name)


print(Sasha.name)


class Human:
    name = 'Sasha'


class Sasha:
    def __init__(self, human: Human):
        self.name = human.name

    def voice(self):
        print(self.name)


human1 = Human()
sasha1 = Sasha(human1)
sasha1.voice()


class A:
    x = 'I am A class'


class B:
    x = 'I am B class'
    y = 'I exists only in B class'


class C(A, B):
    c = 'I exists only in C class'


c = C()
print(c.x)
print(c.y)
print(c.c)


class Our_List(UserList):
    def voice(self):
        print(self.data)


class Our_List:
    def __init__(self):
        self.data = []

    def voice(self):
        print(self.data)