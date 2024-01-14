"""Принцип одиниці відповідальності (SRP):

Завдання: Напишіть клас, який відповідає за роботу з файлами. Розділіть його
функціонал на два класи - один для читання, інший для запису файлів."""


class FileManager:
    def read_file(self, filename):
        with open(filename, 'r') as file:
            content = file.read()
            print('file content is: {}'.format(content))

    def write_file(self, filename, text):
        with open(filename, 'w') as file:
            file.write(text)
            print('Content written to {}'.format(filename))


f = FileManager()
f.write_file('test.txt', 'Ура курс закінчується')
f.read_file('test.txt')
