import random

print(random.randint(1, 1000))

print(random.random())
# 0.984838438

fruits = ['apple', 'banana', 'orange']
random.shuffle(fruits)
print(fruits)

print(random.choice(fruits))
print(fruits)

print(random.choices(fruits, k=4))

print(random.sample(fruits, k=2))



