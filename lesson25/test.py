def func(x, y):
    return x + y


func1 = func
result = func1(10, 10)
print(result)


def sum_func(x, y):
    return x + y


def sub_func(x, y):
    return x - y


def tricky_func(x, y, func):
    return func(x, y)


sum_result = tricky_func(2, 3, sum_func)
sub_result = tricky_func(3, 2, sub_func)
print(sum_result)
print(sub_result)


def get_operator(operator):
    if operator == '+':
        return sum_func
    elif operator == '-':
        return sub_func
    else:
        print('Unknown operator')


sum_action = get_operator("+")
# sum_action -> sum_func
print(sum_action(2, 3))


sub_action = get_operator("-")
# sub_action -> sub_func
print(sub_action(3, 2))


def adder(value):
    def inner(x):
        return x + value
    return inner


two_adder = adder(3)
# inner, value=3
print(two_adder(3))


def handle_operation(x, y, operator):
    if operator == '-':
        return x - y
    elif operator == '+':
        return x + y
    elif operator == '*':
        return x * y
    elif operator == '/':
        return x / y


print(handle_operation(2, 3, '+'))


def sum_func(x, y):
    return x + y


def sub_func(x, y):
    return x - y


OPERATIONS = {
    '+': sum_func,
    '-': sub_func
}


def get_handler(operator: str):
    return OPERATIONS.get(operator)


handler = get_handler('-')

handler2 = get_handler('*')


def logged_func(func):
    def inner(x, y):
        print(f'called with {x}, {y}')
        result = func(x, y)
        print(f'result: {result}')
        return result
    return inner


@logged_func
def complicated(x, y):
    return x / y
# complicated = logged_func(complicated)
# print(complicated(10, 10))
print(complicated(10, 10))


class LoggedClass:
    def __init__(self, function):
        self.function = function

    def __call__(self, x, y):
        print(f'called with {x}, {y}')
        result = self.function(x, y)
        print(f'result: {result}')


@LoggedClass
def complicated(x, y):
    return x / y


complicated(10, 10)


def interval_generator(x, y):
    while x < y:
        yield x
        x += 1


five_to_ten_generator = interval_generator(5, 10)
print(next(five_to_ten_generator))  # 5
print(next(five_to_ten_generator))  # 6
print(next(five_to_ten_generator))  # 7
print(next(five_to_ten_generator))  # 8
print(next(five_to_ten_generator))  # 9


for i in interval_generator(5, 10):
    print(i)


for i in range(5, 10):
    print(i)


