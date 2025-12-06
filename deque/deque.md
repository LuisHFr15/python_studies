# Introduction

We can say that Python Deques (as general deques) are formed with differents blocks of data to allow fast-implementation. Python stores Deques as a two-linked-list, that in other words means that two pointers are stored in the main structure, with one storaging the initial position of the first (far left) block in memory address and the other one storaging the position related to the final (far right) of the list.

These pointers allow to fast insertion and deletion on these position, but at the same time it costs more memory usage than simpler data structures as lists since it stores auxiliar structures and pointers to navigate through the blocks.

## Main Characteristics

Deques has more overhead/memory usage than simple lists.

- Blocks of statics arrays to allow direct access inside the same block, as it can perform faster iteration when iterating through the blocks (not accessing neither iterating the data inside the block).

Deques are fast to storage recently-used data. But less efficient when accessing index.

## Functions

```python
collections.deque.copy()
```

As same as the copy function in Lists, these function creates a new ```collections.deque``` object copying every value inside it in the same order as added.

**Average Cost: O(n)**

---

```python
collections.deque.append(val: Any)
collections.deque.appendleft(val: Any)
```

As said, since deque stores the position of the end/start of each block, the insertion is pretty fast.
We can say that the slower operation is when creating a new block, but since you don't need to iterate the current one, it can be considered negligible.

The key here is to understand that the ```appendleft()``` initiante populating the new block from the end and expanding to the left, while the ```append()``` start populating from the start and expand to the right.

**Average Cost: O(1)**

---

```python
collections.deque.pop()
collections.deque.popleft()
```

We can consider the same as when appending values, but removing it. The significant memory release will occur when clearing the entire block, but the algorithm cost can also be negligible.

This function only removes the first or the last value, so it is as fast as appending.

**Average Cost: O(1)**

---

```python
collections.deque.extend(value: Iterable)
collections.deque.extendleft(value: Iterable)
```

Here you can associate this as a sequence of ```append()``` or ```appendleft()```, and you are pretty right.

Assuming that *k* is the length of the iterable passed as a parameter, we got:

**Average Cost: O(k)**

---

```python
collections.deque.rotate(k: int)
```

Try to view the deque as a sequence of dots, where one dot is the object in a certain index. The ```rotate()``` function is the *k* times that you will make the ```pop()``` and ```appendleft()``` functions sequentially. In the same analogy, is catching the last dot in the list and positioning it in the first position, this sequence for *k* times.

So, we can see that, since ```pop()``` and ```appendleft()``` has the same cost, O(1), we get:

**Average Cost: O(k)**

---

```python
collections.deque.remove(val: Any)
```

Removes the first occurrence of a value in the Deque, the same as the ```list.remove()``` function. The function iterate from left to right (start to end) and removes the first occurrence of the value. The function will recquire to reorganize/move the values after it, increasing the time complexity.

**Average Cost: O(n)**

---

```python
len(collections.deque)
```

As python lists, the Deque object stores an integere variable that refers the count of values inside the Deque, not requiring to iterate through the structure.

**Average Cost: O(1)**