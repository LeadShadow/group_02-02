# В предыдущей задаче мы записали сотрудников в файл в следующем виде:
#
# Robert Stivenson,28
# Alex Denver,30
# Drake Mikelsson,19
# Выполним теперь обратную задачу и создадим функцию read_employees_from_file(path),
# которая будет читать данные из файла и возвращать список сотрудников в виде:
#
# ['Robert Stivenson, 28', 'Alex Denver, 30', 'Drake Mikelsson, 19']
# Помните про присутствие символа конца строки \n при чтении данных из файла. Его
# необходимо убирать при добавлении прочитанной строки в список.
#
# Требования:
#
# прочтите содержимое файла, используя режим "r".
# мы пока не используем менеджер контекста with
# верните из функции список сотрудников из файла

def read_employees_from_file(path):
    file = open(path, 'r')
    result = []
    lines = file.readlines()
    # while True:
    #     line = file.readline().strip()  # 'Robert Stivenson,28\n'
    #     if not line:
    #         break
    #     result.append(line)
    for line in lines:
        line = line.strip()
        result.append(line)
    file.close()
    return result


print(read_employees_from_file('task1.txt'))
