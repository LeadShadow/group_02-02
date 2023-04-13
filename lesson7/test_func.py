def func(a, b=5, c=10):
    print('a ==', a, 'b ==', b, 'c ==', c)


func(10, 10, 10)
func(a=5)
func(a=10, b=15, c=20)
func(c=200, a=100, b=150)


def say(message, times=1):
    print(message * times)


say('Привіт')
say(message='Світ', times=5)


