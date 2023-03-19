# У нас є три логічні змінні.
# Перша визначає статус користувача is_active, що дорівнює True або False.
# Друга is_admin визначає, чи є у користувача права адміністратора булевого типу.
# Третя is_permission — чи дозволено доступ, теж булевого типу. True or False
# Приведіть змінні is_active, is_admin та is_permission до булевого вигляду.

# Надайте змінної access, значення, яке покаже, чи є доступ користувача. Використовуйте логічні оператори.

# Адміністратор завжди має доступ незалежно від значень змінних is_permission і is_active.

# Користувач має доступ тільки якщо is_permission дорівнює True і is_active також дорівнює True


is_active = bool(input('Is the user active?: '))
is_permission = bool(input('Does the user have access?: '))
is_admin = bool(input('Is the user admin?: '))

# користувач повинен мати доступ, якщо він адмін АБО він активний і він має доступ

access = is_admin or is_active and is_permission
print(access)

