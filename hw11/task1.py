# Створіть функцію change(list), яка приймає на вхід список і міняє місцями його перший і останній елемент
# В початковому списку має бути мінімум два елемента


def change(list: list):
    if len(list) > 2:
        first_elem = list.pop(0)
        last_elem = list.pop()
        print(first_elem, last_elem, list)
        list.insert(0, last_elem)
        list.insert(2, first_elem)
        return list
    else:
        return list


print(change([1, 2, 3]))
