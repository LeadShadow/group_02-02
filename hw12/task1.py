# Необходимо написать функцию is_valid_password, которая будет проверять полученный
# параметр — пароль на надежность.
#
# Критерии надежного пароля:
#
# Длина строки пароля восемь символов.
# Содержит хотя бы одну букву в верхнем регистре.
# Содержит хотя бы одну букву в нижнем регистре.

# Підказка, перевірка на великі літери і маленькі, можна зробити за допомогою
# if 'A' <= ch <= 'Z':
# if 'a' <= ch <= 'z':
def is_valid_pin_codes(pin_codes):
    a = False
    b = False
    c = False
    if len(pin_codes) < 8:
        return False
    for ch in pin_codes:
        if "A" <= ch <= "Z":  # 1 <= x <= 36
            a = True
        elif "a" <= ch <= "z":
            b = True
        elif "0" <= ch <= "9":
            c = True
    return a and b and c  # True


print(is_valid_pin_codes('QWErtY1'))