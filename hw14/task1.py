# Напишите функцию formatted_grades, которая принимает на вход словарь оценивания студентов по предмету следующего вида:
#
# students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
# И возвращает список отформатированных строк, чтобы при выводе следующего кода:
#
# for el in formatted_grades(students): print(el)
# Получалась следующая таблица:
#
# 1|Nick | A | 5
# 2|Olga | B | 5
# 3|Mike | FX | 2
# 4|Anna | C | 4
# первый столбец — ширина 4 символа, выравнивание по правому краю
# второй столбец — ширина 10 символов, выравнивание по левому краю
# третий и четвертый столбец — ширина 5 символов и выравнивание по центру
# вертикальный символ | не входит в ширину столбца

# Використовуємо форматування рядків .format

students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
grades = {'A': 5, 'B': 5, 'C': 4, 'D': 3, 'E': 3, 'FX': 2, 'F': 1}

def formatted_grades(students, grades):
    format_string = '{:>4}|{:<10}|{:^5}|{:^5}'
    counter, result = 0, []
    for student in students:
        counter += 1
        result.append(format_string.format(counter, student, students[student], grades[students[student]]))
    return result


for i in formatted_grades(students, grades):
    print(i)