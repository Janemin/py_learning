# List as a stack (LIFO)
stack = list()

stack.append(1)     # push
stack.append(2)
stack.pop()         # pop
stack.pop()


# List as a queue (FIFO)
from collections import deque

queue = deque(list())

queue.append(1)
queue.append(2)
queue.popleft()
queue.popleft()

# 列表推导式
vec = [2, 4, 6]
print([3 * x for x in vec])     # [6, 12, 18]
print(vec)                      # [2, 4, 6]

# if -  filter
print([3 * x for x in vec if x > 3])    # [12, 18]


vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print([x * y for x in vec1 for y in vec2])    # [8, 6, -18, 16, 12, -36, 24, 18, -54]



# nested list
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]


print([[row[i] for row in matrix] for i in range(4)])  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


# dict.items
dict = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in dict.items():
    print(k, v)


# list.enumerate

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)


# sequence - zip
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# sequence - reversed()
for i in reversed(range(1, 5)):
    print(i)

# sequence - sorted()
for i in sorted([2, 1, 3]):
    print(i)
