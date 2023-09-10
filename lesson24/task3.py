# lifo

from collections import deque

MAX_LEN = 10

lifo = deque(maxlen=MAX_LEN)
# [1, 2, 3]
# [].append(4)
# [1, 2, 3, 4]
# .insert(4, 1)


def push(element):
    lifo.appendleft(element)


def pop():
    return lifo.popleft()
