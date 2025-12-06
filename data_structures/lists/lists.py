# initializing
my_python_list = [number for number in range(0, 100)]

# acessing and setting
print('Acessing and setting in list')
print(my_python_list[0])
my_python_list[0] = 'python!'
print(my_python_list)

print('\nBasic functions: append (insert) and pop')
my_python_list.append(1)
print('After append, last index:', my_python_list[-1])
my_python_list.pop()
print('After pop last, last index:', my_python_list[-1])
my_python_list.pop(1)
print('Popping intermediate (index 1), the slice from index 0 to 4:', my_python_list[:5])
my_python_list.insert(1, 1)
print('After inserting 1 at index 1, the slice from index 0 to 4:', my_python_list[:5])

# ------------------------

# removing and iteraing
my_python_list.remove('python!')
print('After removing "python!", the slice from index 0 to 4:', my_python_list[:5])
print('Iterating through index 0 to 10:')
for index, value in enumerate(my_python_list[:10]):
    print(index, ':', value)

my_python_list[:5] = ['a', 'b', 'c', 'd', 'e', 'f']
print('After setting a new slice:', my_python_list[:5])

del my_python_list[:6]
print('After deletion on slice from index 0 to 5:', my_python_list[:6])

# extending and sorting
my_python_list.sort(reverse=True)
print('Sorting list in descending order:', my_python_list)

my_python_list.extend([5,4,3,2,1])
print('After expanding the list with the values we removed before:', my_python_list)

print()
# Multiplying and getting values
my_other_python_list = my_python_list[:6]
print(r"Using slice from index 0 to 5, here's the list multiplyied to 3:", my_other_python_list * 3)

print('Min from the slice:', min(my_other_python_list), '| Max from the slice:', max(my_other_python_list))

print('Using *in* statement, looking for value 1 in the slice:')
if 1 in my_other_python_list:
    print('Value 1 in slice')
else:
    print('Not in list')
    
print('The final slice has length of:', len(my_other_python_list))    
