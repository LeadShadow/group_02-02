# Задача: Аналіз даних з CSV файлу
#
# У вас є CSV файл з даними про різних студентів у форматі:
#
# Ім'я, Вік, Середній_бал
# Анна, 21, 8.5
# Петро, 20, 7.2
# Марія, 22, 9.0
# Іван, 19, 6.8
# ...
# Це початкова структура файлу csv, який потрібно створити і наповнити данними(бажано через пайтон)
# Задача:
#
# Завантажте дані з CSV файлу та збережіть їх у зручній для роботи структурі даних.
# Обчисліть середній вік студентів.
# Знайдіть студента з найвищим середнім балом та виведіть його ім'я і бал.
# Порахуйте кількість студентів, які молодші за 20 років.
# Створіть новий CSV файл, в який запишете імена студентів, вік та середній бал, але
# відсортовані за спаданням середнього балу.

# ps: можна використовувати загальний клас(методи класу), наслідування(якщо потрібно), а також функ
# ціональний підхід(пам'ятай кожен крок це функція нова, 1 функція відповідає за одну дію))
import csv


def save_students_to_csv():
    with open('students_info.csv', 'w', newline='') as file:
        fields_names = ["Name", 'Age', 'Average grade']
        writer = csv.DictWriter(file, fieldnames=fields_names)
        writer.writeheader()
        writer.writerow({"Name": 'Annya', 'Age': '21', 'Average grade': '8.5'})
        writer.writerow({"Name": 'Petro', 'Age': '20', 'Average grade': '7.2'})
        writer.writerow({"Name": 'Mari', 'Age': '22', 'Average grade': '9.0'})
        writer.writerow({"Name": 'Ivan', 'Age': '19', 'Average grade': '7.1'})


save_students_to_csv()


def load_students_from_csv():
    data = []
    with open('students_info.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # пропускаємо заголовок
        for row in reader:
            name, age, grade = row
            data.append({
                'name': name,
                'age': int(age),
                'grade': float(grade)
            })
    return data


data = load_students_from_csv()

# Середній вік
data1 = [student['age'] for student in data]
print(data1)
total_age = sum(student['age'] for student in data)
average_age = total_age / len(data)
print(average_age)

# Знаходження студента з найвищим балом
best_student = max(data, key=lambda student: student['grade'])
print(f'Студент з найвищим балом {best_student["name"]}, бал: {best_student["grade"]}')
print('Студент з найвищим балом {}, бал: {}'.format(best_student["name"], best_student["grade"]))


# Порахувати кількість студентів молодших за 20 років
young_students = sum(1 for student in data if student['age'] <= 20)
print('Кількість студентів молодших за 20 років {}'.format(young_students))


# Створіть новий CSV файл, в який запишете імена студентів, вік та середній бал, але
# відсортовані за спаданням середнього балу
# sorted_students.csv