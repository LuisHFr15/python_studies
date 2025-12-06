# Initializing sets
my_python_set = {x for x in range(10)}
print('Initial set:', my_python_set)

print('\nAdding and removing elements:')
my_python_set.add(10)
print('After add(10):', my_python_set)
my_python_set.remove(5)
print('After remove(5):', my_python_set)
my_python_set.discard(100)
print('After discard(100) - non-existent:', my_python_set)

popped = my_python_set.pop()
print(f'Popped element: {popped}, remaining set:', my_python_set)
\
print('\nMembership testing:')
print('Is 3 in set?', 3 in my_python_set)
print('Is 100 in set?', 100 in my_python_set)

print('\nSet operations:')
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
\
print('set_a:', set_a)
print('set_b:', set_b)
print('Union (set_a | set_b):', set_a | set_b)
print('Union (set_a.union(set_b)):', set_a.union(set_b))

print('Intersection (set_a & set_b):', set_a & set_b)
print('Intersection (set_a.intersection(set_b)):', set_a.intersection(set_b))

print('Difference (set_a - set_b):', set_a - set_b)
print('Difference (set_a.difference(set_b)):', set_a.difference(set_b))

print('Symmetric difference (set_a ^ set_b):', set_a ^ set_b)
print('Symmetric difference (set_a.symmetric_difference(set_b)):', set_a.symmetric_difference(set_b))

print('\nSubset and superset:')
set_c = {1, 2, 3}
print('set_c:', set_c)
print('Is set_c subset of set_a?', set_c.issubset(set_a))
print('Is set_a superset of set_c?', set_a.issuperset(set_c))
print('Are set_a and set_b disjoint?', set_a.isdisjoint(set_b))

print('\nUpdate operations:')
set_d = {1, 2, 3}
print('set_d before update:', set_d)
set_d.update([4, 5, 6])
print('After update([4, 5, 6]):', set_d)

set_d.intersection_update({3, 4, 5, 6, 7})
print('After intersection_update({3, 4, 5, 6, 7}):', set_d)

set_d.difference_update({5, 6})
print('After difference_update({5, 6}):', set_d)

print('\nConverting from other structures:')
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_values = set(my_list)
print('List with duplicates:', my_list)
print('Set from list (removes duplicates):', unique_values)

print('\nFrozenset (immutable):')
frozen = frozenset([1, 2, 3, 4, 5])
print('Frozenset:', frozen)
print('Can be used as dict key or set element:', {frozen: 'value'})

print('\nPractical example - finding duplicates:')
numbers = [1, 2, 3, 2, 4, 5, 3, 6, 7, 5]
seen = set()
duplicates = set()
for num in numbers:
    if num in seen:
        duplicates.add(num)
    seen.add(num)
print('Original list:', numbers)
print('Duplicates found:', duplicates)

print('\nSet comprehension:')
squares = {x**2 for x in range(10)}
print('Squares from 0 to 9:', squares)

even_squares = {x**2 for x in range(10) if x % 2 == 0}
print('Even squares:', even_squares)

print('\nLength and clearing:')
print('Length of set_a:', len(set_a))
set_copy = set_a.copy()
set_copy.clear()
print('After clear():', set_copy)
print('Original set_a unchanged:', set_a)
