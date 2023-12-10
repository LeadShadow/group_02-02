# головна(фронтенд)
# json(JavaScript Object Notation) -> main.json
# backend -> main.json
import pickle
import json
import csv
import yaml

expenses = {
   'hotel': 1000,
    'breakfast': 100,
    'taxi': 150,
    'lunch': 200
}

file_name = 'expenses.txt'
with open(file_name, 'w') as fh:
    for key, value in expenses.items():
        fh.write(f'{key} | {value}\n')


with open(file_name, 'r') as file:
    for line in file:
        value_of_items = line.split('|')[1].strip().replace('\n', '')
        print(value_of_items)


some_data = {
    'tuple': (1, 2),
    2: [1, 2, 3],
    'a': {'key': 'value'}
}

byte_string = pickle.dumps(some_data)
unpacked = pickle.loads(byte_string)

print(unpacked == some_data)
# (), {} -> []
# 1 -> '1'
# True -> true

file_name = 'data.bin'
with open(file_name, 'wb') as fh:
    pickle.dump(some_data, fh)


with open(file_name, 'rb') as fh:
    unpacked = pickle.load(fh)


print(unpacked)


class Human:
    def __init__(self, name):
        self.name = name


bob = Human('Bob')
encoded_bob = pickle.dumps(bob)
decoded_bob = pickle.loads(encoded_bob)

print(bob.name == decoded_bob.name)


file_name = 'data1.bin'
with open(file_name, 'wb') as fh:
    pickle.dump(bob, fh)


with open(file_name, 'rb') as fh:
    unpacked = pickle.load(fh)


print(unpacked.name)


byte_string = json.dumps(some_data)
unpacked = json.loads(byte_string)

print(unpacked == some_data)
print(unpacked)

file_name = 'data.json'
with open(file_name, 'w') as fh:
    json.dump(some_data, fh)


with open(file_name, 'r') as fh:
    unpacked = json.load(fh)


print(unpacked)

with open('eggs.csv', 'w', newline='') as file:
    spam_writer = csv.writer(file)
    spam_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
    spam_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful spam'])


with open('eggs.csv', newline='') as fh:
    spam_reader = csv.reader(fh)
    for row in spam_reader:
        print(row)


