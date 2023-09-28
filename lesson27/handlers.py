import re
from decorator import input_error


def hello(*args: tuple) -> str:
    return 'Hello! How can I help you?'


@input_error
def add_contact(contacts: dict, *args: tuple) -> str:
    name, phone = args[0], args[1]
    contacts[name] = verify_phone(phone)  # contacts = {},  contacts['Sasha'] = '+380937316048' -> contacts = {'Sasha': '+380937316048'}
    return f'Added user {name}'


@input_error
def change_contact(contacts: dict, *args: tuple) -> str:
    name, phone = args[0], args[1]
    contacts[name] = verify_phone(phone)
    return f'Change user {name}'


@input_error
def show_phone(contacts: dict, *args: tuple) -> str:
    name = args[0]
    return f'User - {name}, phone - {contacts[name]}'


@input_error
def show_all(contacts: dict, *args: tuple) -> str:
    result = 'List of all users: '
    for name, phone in contacts.items():
        result += '\nUser - {:^10}| phone - {:^15}'.format(name, phone)
    return result


def goodbye(*args: tuple) -> None:
    return None


def help_me(*args: tuple) -> str:
    return """Command format:
help or ? - help
hello - func of greeting
add <name> <phone> - add user to addressbook
change <name> <phone> - change the user's phone number
phone <name> - show the user's phone number
show all - show all contacts
close or . or exit or stop - exit the program"""


def verify_phone(phone: str) -> str:  # \+
    new_phone = re.sub(r'\+|\(|\)|-| |[a-zA-ZА-Яа-я]', '', phone)
    return new_phone
