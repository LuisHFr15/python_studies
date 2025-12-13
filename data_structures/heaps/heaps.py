import heapq
import random
from time import sleep

my_heap = []
for i in range(20):
    my_heap.append(random.randint(0, 100))
print('Starting my list with random numbers from 0 to 100:', my_heap)
print('\n\n')
heapq.heapify(my_heap)
print('Heapifying my list:', my_heap)

print('\n\n')

heapq.heappush(my_heap, 150)
print('My heap after adding 150:', my_heap)

heapq.heappush(my_heap, -10)
print('Added number -10', my_heap)

heapq.heappush(my_heap, -15)
print('Added number -15:', my_heap)

print('\n\n')

print('Popped:', heapq.heappop(my_heap))
print(my_heap)

print('\n\n')

value = heapq.heappushpop(my_heap, -5)
print(f'Push -5 and popped {value} with pushpop:', my_heap)


print('\n\n')

value = heapq.heapreplace(my_heap, -10)
print(f'Push -10 and popped {value} with replace:', my_heap)
