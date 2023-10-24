# В четвертом модуле мы реализовали функцию lookup_key для поиска всех ключей по значению
# в словаре. Первым параметром в функцию мы передавали словарь, а вторым — значение,
# которое хотели найти. Результатом был список ключей или пустой список, если мы ничего не находили.
#
# def lookup_key(data, value):
# keys = []
# for key in data:
# if data[key] == value:
# keys.append(key)
# return keys
# Создайте класс LookUpKeyDict, родителем которого будет класс UserDict.
# Сделайте функцию lookup_key методом класса LookUpKeyDict.

from collections import UserDict


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        keys = []
        for key in self.data:
            if self.data[key] == value:
                keys.append(key)
        return keys


lok_key_dict = LookUpKeyDict({'1': 1, '2423': 2, '3': 3, '201': 2})
print(lok_key_dict.lookup_key(2))
# def lookup_key(data, value):
#     keys = []
#     for key in data:
#         if data[key] == value:
#             keys.append(key)
#     return keys
