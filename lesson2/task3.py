# При заполнении анкеты на сайте нам необходимо через функцию input присвоить соответствующим
# переменным значения:
#
# name - ваше имя, тип строка
# email - ваша электронная почта, тип строка
# age - ваш возраст, тип число int
# height - ваш рост, тип число float
# is_active - хотите ли вы получать уведомления от сайта, тип булевый

name = input('Input your name: ')
email = input('Input your email: ')
age = int(input('Input your age: '))
height = float(input('Input your height: '))
is_active = bool(int(input('Якщо не хочете отримувати повідомлення напишіть 0, якщо хочете, 1: '))) #
print(name, email, age, height, is_active)

# Ні не хочу -> False - неправильно
# Ні не хочу -> True - правильно