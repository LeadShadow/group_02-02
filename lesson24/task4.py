# fifo

from collections import deque

MAX_LEN = 10

fifo = deque(maxlen=MAX_LEN)


def push(element):
    fifo.append(element)

# []
# [1, 2]
# [2]
def pop():
    return fifo.popleft()
