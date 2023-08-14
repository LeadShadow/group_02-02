import random

d = {
    1: 'Орел',
    2: 'Решка'
}

count_O = 0
count_P = 0
sequence = []

while count_P < 3 and count_O < 3:
    trial = random.randint(1, 2)
    if trial == 1:
        count_O += 1
        count_P = 0
    else:
        count_O = 0
        count_P += 1
    sequence.append(d[trial])

print(f'Отримана послідовність: {sequence}')

if count_O == 3:
    print('Випало три орла підряд')
else:
    print('Випало три решки підряд')

print(f'Кількість спроб: {len(sequence)}')
