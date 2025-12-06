from collections import deque

my_python_deque = deque([x for x in range(100)])
print(my_python_deque)

my_python_deque.append(100)
print('Appending 100 in right', my_python_deque)
my_python_deque.appendleft(101)
print('Appending 101 in left:', my_python_deque)

print('Accessing index 50:', my_python_deque[50])
print()

my_python_deque.popleft()
my_python_deque.pop()
print('Popping right and left:', my_python_deque)

my_python_deque.append(40)
my_python_deque.remove(40)
print('Added value 40 and then used remove(40):', my_python_deque)

print()
my_python_deque.extend([1,2,3])
print('Extended [1,2,3]', my_python_deque)

print()
my_python_deque.extendleft([0, -1, -2])
print('Extended left [0, -1, -2]', my_python_deque)

print()
my_python_deque.rotate(2)
print('Rotated deque in 2 steps:', my_python_deque)