# Introduction

Very simillar to ArrayLists in Java: flexible to store data, it don't need to be the same type

The very first index is 0, while each item is added adds one more index, sequentially.

Python lists uses object references without using hash functions, storaging object references in the contiguous memory address.
The access is direct, without passing the value through a hash function. The major costs is located in functions that alters all the structure, requiring objects in certains index to move to ```index + 1``` or ```index - 1```.
The object reference is the pointer to its address, since Python does not storage the Object itself in the list it allows to the pointers to be a fixed size, only needing arithmetics to access index data directly.

## Functions

```python
list.copy()
```

The ```copy()``` function creates exactly the same list in another variable. Since when you refer it in another variable, you are just referencing the same object in the same address. To solve this issue, here are the ```copy()``` function, creating the same list object into another memory address and referencing it to the new variable

**Average Cost: O(n)**

---

```python
list.append(value: Any)
```

The ```append()``` function inserts a new Object reference in the very last position of the list. Since the list index is accessed through arithmetics and Python stores the list size, it only needs to add a new index after the last one.

**Average Cost: O(1)**

---

```python
list.pop(pos: int = None)
```

There is a tricky question: the time complexity is different when you pass or not an argument to the very function.

- Without parameter = pop last: the function only removes the last item in the list, and following the same principles in ```list.append()```, only free the memory address of the object and delete the reference in the index, also deletes the index itself on the list.
  - **Average Cost: O(1)**
- With parameter = pop intermediate: the function will remove an intermediate index in the list, working the same as a generic ```remove_by_index()``` function. Here, Python follows the same steps as pop last, but needs to rearrange the entire list.
  - **Average Cost: O(n)**

---

```python
list.insert(pos: int, value: Any)
```

This function has the same working workflow as ```append()```, but has the same concerns as the pop intermediate, needing to rearrange the entire list after the insertion.

**Average Cost: O(n)**

---

```python
list[index]
list[index] = obj
```

This list manipulation, as shown in the Introduction, it's easy to understand how Python can access and change values in a determined index without extreme complexity.

The access is given by ```index_address = base_address + (index * pointer_size)```. The Python pointers is always 8 bytes length, the base_address is determined by memory allocation, only needing the index to, in fact, access the Object stored in.


**Average Cost: O(1)**

---

```python
list.remove(value: Any)
```

This function removes the very first occurrence in the list given an Object reference to delete. The worst case scenario is when the object is located in the final of the list as the function needs to access every index until find the match value.

Even when located in the middle of the list, it needs to rearrange it, as the pop intermediate, increasing time complexity.

**Average Cost: O(n)**

---

```python
for val in list:
    ...
```
A simple loop through each object in the list, accessing directly each component.

**Average Cost: O(n)**

---

```python
list[start:end:steps]
```

This function you can choose the parameters to use in it, the slice length can be calculated as ```k = slice_length = (end - start) / steps```.
You can think that it's look like an iteration through the list choosing the specifics indexes.

**Average Cost = O(k)**

You can set a slice of a list associating it with a list of same size
```python
list[start:end] = list2
```


Also, you can remove a slice of a determined list using the ```del``` statement in python, where the resultant list will be the part of the list that not belongs to the slice:
```python
del list[start:end]
```

The average cost of each usage is the same, dependending of the size of the slice (k) and the length of the list (n).

**Average Cost: O(n + k)**

---

```python
list.extend(another_list: Iterable)
```
In this function, is the same as appending each element of ```another_list``` in the list that you are using the function. Since the time complexity of ```append()``` function is O(1), we can assume the average cost of appending *k* elements:

**Average Cost: O(k)**

---

```python
list.sort(reverse = True | False)
```
The Python's default sorting algorithm is the Timsort, an algorithm created by Tim Peters. This algorithm combines Merge Sort and Insertion Sort, so it can ensure stability with O(n log n), as it can ensure good capacity to short lists.

Given it, we can see that the Best Scenario, the complexity can be pretty linear, but in average scenario:

**Average Cost: O(n log n)**

---

```python
list = list * n: int|float
```
This Python list operation is the same as multiplying numbers, but instead of it you're multiplying the list elements in *n* times. Due to that, we can assume that it's the same that appending each element of the list *n* times.

**Average Cost: O(n*k)**

---

```python
value in list
```
This operation is the same as the ```contains()``` function in another languages, checking if the value in the left is in the list. Here, is the same as iterating through the entire list to ensure that the list contains (or not) the value.

**Average Cost: O(n)**

---

```python
min(list)
max(list)
```
This operation has the same base behavior as the value checking said right ahead, we iterate through the entire list to get the maximum or minimum value present in the list. Again, since the access in list indexes is direct, we only has the time complexity defined by iterating the list.

**Average Cost: O(n)**

---

```python
len(list)
```
This built-in function return to us the total size/contained elements in the list. Python is very smart! Why? Because the ```list``` object stores an integer variable that contains the size of the object/total elements added to the list. So, when calling ```len()``` function, it's the same as accessing the direct variable that stores the list size.

**Average Cost(1)**
