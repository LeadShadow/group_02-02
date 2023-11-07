class Human:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def say_hello(self):
        return f'Hello! I am {self.name}'


bill = Human('Bill', 18)
print(bill.say_hello())
print(bill.age)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point ({self.x};{self.y})'

    def __str__(self):
        return f'Point ({self.x}: {self.y})'


point = Point(10, 20)
print(point)
list = [1, 2, 3]


class ListedValueDict:
    def __init__(self):
        self.data = {}

    def __setitem__(self, key, value):
        if key in self.data:
            self.data[key].append(value)  # {1: ['a', 'b']}
        else:
            self.data[key] = [value]  # {1: ['a']}

    def __getitem__(self, key):
        result = str(self.data[key][0])  # {1: ['a', 'b']}
        for value in self.data[key][1:]:
            result += ', ' + str(value)
        return result


l_dict = ListedValueDict()
l_dict[1] = 'a'
l_dict[1] = 'b'
print(l_dict[1])


class Adder:
    def __init__(self, add_value):
        self.add_value = add_value

    def __call__(self, value):
        return self.add_value + value


two_adder = Adder(5)
print(two_adder(10))


class Session:
    def __init__(self, addr, port=8080):
        self.connected = True
        self.addr = addr
        self.port = port

    def __enter__(self):
        print(f'Connected to {self.addr}: {self.port}')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connected = False
        if exc_type is not None:
            print('Some error!')
        else:
            print('No problem')


localhost_session = Session('localhost')
with localhost_session as session:
    raise Exception('OH NO!')

print(localhost_session.connected)
