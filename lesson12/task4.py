# У нас есть список показателей студентов группы — это список с полученными балами по
# тестированию. Необходимо список поделить на две части. Напишите функцию split_list,
# которая принимает список (целые числа), находит среднее значение балла в списке и делит его
# на два списка. В первый попадают значения меньше среднего, включая среднее значение,
# а во второй — строго больше среднего. Функция возвращает кортеж этих двух списков.
# Для пустого списка возвращаем два пустых списка.

# [12, 10, 12, 11, 10] -> sum([12, 10, 12, 11, 10]) -> 55 / len([12, 10, 12, 11, 10]) -> 55 / 5
def split_list(grade):
    # Для пустого списка возвращаем два пустых списка
    if len(grade) == 0:
        return ([], [])
    grade1, grade2 = [], []
    average = sum(grade) / len(grade)
    print(average)
    for i in grade:
        if i > average:
            grade2.append(i)
        else:
            grade1.append(i)
    return grade1, grade2


if __name__ == "__main__":
    print(split_list([9, 11, 6, 3, 10, 12, 7, 10, 2, 1, 5]))