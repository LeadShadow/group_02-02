# SOLID
from abc import ABC, abstractmethod
# 1 Single Responsibility
import time


class FileManager:
    def read_file(self, filename):
        # код
        ...

    def write_file(self, filename, text):
        # код
        ...

# 2 Open-Closed принцип відкритості-закритості


class InputError:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print('time is {}'.format(time.time()))
        self.func()
        print('time is {}'.format(time.time()))


@InputError
def func1(a=10, b=20):
    print(a * b)


func1()


# Принципи проектування

# 3 Принцип підстановки Барбари Лісков(Liskov Substitution)

class Bird:
    def fly(self):
        pass


class Sparrow(Bird):
    def fly(self):
        print('Sparrow is flying')


class Penguin(Bird):
    def swim(self):
        print('Penguin is swimming')


def make_bird_fly(bird):
    bird.fly()


sparrow = Sparrow()
penguin = Penguin()

make_bird_fly(sparrow)
make_bird_fly(penguin)


# 4 Принцип розділення інтерфейсу Interface Segregation

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class TeamLead(Worker):
    def work(self):
        print('SuperWorker is working')

    def eat(self):
        print('SuperWorker is eating')

    def code(self):
        print('SuperWorker is coding')


class MiddleDev(Worker):
    def work(self):
        print('MiddleDev is working')

    def eat(self):
        print('MiddleDev is eating')


# 5 Принцип інверсії залежностей Dependency Inversion

