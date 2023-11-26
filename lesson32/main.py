"""
Наш ассистент уже умеет взаимодействовать с пользователем посредством командной строки,
получая команды и аргументы и выполняя нужные действия. В этом задании нужно будет поработать
над внутренней логикой ассистента, над тем, как хранятся данные, какие именно данные и что с
 ними можно сделать.

Применим для этих целей объектно-ориентированное программирование. Для начала выделим несколько
сущностей (моделей) с которыми будем работать.

У пользователя будет адресная книга или книга контактов. Эта книга контактов содержит записи.
Каждая запись содержит некоторый набор полей.

Таким образом мы описали сущности (классы), которые необходимо реализовать. Далее рассмотрим
требования к этим классам и установим их взаимосвязь, правила, по которым они будут взаимодействовать.

Пользователь взаимодействует с книгой контактов, добавляя, удаляя и редактируя записи. Также
пользователь должен иметь возможность искать в книге контактов записи по одному или нескольким
критериям (полям).

Про поля также можно сказать, что они могут быть обязательными (имя) и необязательными
(телефон или email например). Также записи могут содержать несколько полей одного типа
(несколько телефонов например). Пользователь должен иметь возможность добавлять/удалять/редактировать
поля в любой записи.

В этой домашней работе вы должны реализовать такие классы:

Класс AddressBook, который наследуется от UserDict, и мы потом добавим логику поиска по записям в этот класс.
Класс Record, который отвечает за логику добавления/удаления/редактирования необязательных полей и
хранения обязательного поля Name.
Класс Field, который будет родительским для всех полей, в нем потом реализуем логику общую для всех полей.
Класс Name, обязательное поле с именем.
Класс Phone, необязательное поле с телефоном и таких одна запись (Record) может содержать несколько.
Критерии приёма#
Реализованы все классы из задания.
Записи Record в AddressBook хранятся как значения в словаре. В качестве ключей используется значение
Record.name.value.
Record хранит объект Name в отдельном атрибуте.
Record хранит список объектов Phone в отдельном атрибуте.
Record реализует методы для добавления/удаления/редактирования объектов Phone.
AddressBook реализует метод add_record, который добавляет Record в self.data.
"""
from __future__ import annotations

import re
from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return f'{self.value}'


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name: Name, phones: list[Phone] | Phone = []):
        self.name = name
        self.phone_list = phones

    def __str__(self) -> str:
        return f'User: {self.name.value} - Phones: {", ".join([phone.value for phone in self.phone_list])}'

    def add_phone(self, phone: Phone) -> None:
        self.phone_list.append(phone)

    def del_phone(self, phone) -> None:
        self.phone_list.remove(phone)

    def edit_phone(self, phone: Phone, new_phone: Phone):
        self.phone_list.remove(phone)
        self.phone_list.append(new_phone)


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record  # 'Sasha': record


class PhoneUserAlreadyExists(Exception):
    def __str__(self):
        return """You cannot add an existing phone number"""


class InputError:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, contacts: AddressBook, *args: tuple):
        try:
            return self.func(contacts, *args)
        except IndexError:
            return 'Error! Give me name and phone please'
        except KeyError:
            return 'Error! User not found'
        except ValueError:
            return 'Error! Phone number is incorrect'
        except PhoneUserAlreadyExists:
            return PhoneUserAlreadyExists()


def hello(*args: tuple) -> str:
    return 'Hello! How can I help you?'


@InputError
def add_contact(contacts: AddressBook, *args: tuple) -> str:
    name, phone = Name(args[0]), Phone(args[1])
    phone = verify_phone(phone.value)
    if name.value in contacts:
        if phone in contacts[name.value].phone_list:
            raise PhoneUserAlreadyExists
        else:
            contacts[name.value].add_phone(phone)
            return f'Add phone {phone} to user {name.value}'
    else:
        contacts[name.value] = Record(name, [Phone(phone)])
        return f'Add user {name.value} with phone {phone}'


@InputError
def change_contact(contacts: AddressBook, *args: tuple) -> str:
    name, old_phone, new_phone = Name(args[0]), Phone(args[1]), Phone(args[1])
    new_phone = verify_phone(new_phone.value)
    old_phone = verify_phone(old_phone.value)
    contacts[name.value].edit_phone(Phone(old_phone), new_phone)
    return f'Change user {name}'


@InputError
def del_phone(contacts: AddressBook, *args: tuple) -> str:
    name, phone = Name(args[0]), Phone(args[1])
    phone = verify_phone(phone.value)
    contacts[name.value].del_phone(phone)
    return f'Delete phone {phone} from user {name.value}'


@InputError
def show_phone(contacts: AddressBook, *args: tuple) -> str:
    name = Name(args[0])
    return f'{contacts[name.value]}'


@InputError
def show_all(contacts: AddressBook, *args: tuple) -> str:
    result = 'List of all users: '
    for key in contacts:
        result += f'\n{contacts[key]}'
    return result


def goodbye(*args: tuple) -> str:
    return 'Good bye!'


def help_me(*args: tuple) -> str:
    return """Command format:
help or ? - help
hello - func of greeting
add <name> <phone> - add user to addressbook
change <name> <old_phone> <new_phone> - change the user's phone number
del <name> <phone> - delete the user's phone number
phone <name> - show the user's phone number
show all - show all contacts
close or . or exit or stop - exit the program"""


def verify_phone(phone: str) -> str:  # \+
    new_phone = re.sub(r'\+|\(|\)|-| |[a-zA-ZА-Яа-я]', '', phone)
    return new_phone


def unknown_command(*args: tuple):
    return 'Unknown command!'


COMMANDS = {'hello': hello, 'add': add_contact, 'change': change_contact, 'phone': show_phone,
            'show all': show_all, 'exit': goodbye, 'close': goodbye, 'stop': goodbye, '.': goodbye,
            '?': help_me, 'help': help_me, 'del': del_phone}


def command_parser(user_command: str):
    for key, value in COMMANDS.items():
        if user_command.lower().startswith(key):
            args = user_command[len(key):].split()
            return value, args
    else:
        return unknown_command, []


def main():
    contacts = AddressBook()
    while True:
        user_command = input('Enter command: ')
        command, data = command_parser(user_command)
        print(command(contacts, *data))
        if command is goodbye:
            break


if __name__ == "__main__":
    main()
