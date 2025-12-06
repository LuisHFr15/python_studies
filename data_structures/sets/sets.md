# Introduction

Python Sets it's an unordered collection of unique elements, being usually compared with the HashSets from other languages. Since sets uses hash functions to allocate the memory to the object to be added in the collection, many of the functions of the set can be considered faster than common operations in other data structures.

## Collisions

Everything when using hash functions can cause memory address collisions, turning necessary to use a method to allocate the object even when a collision occurs.

To be more exactly, many languages and databases uses linked-lists when a collision happens. Differently, Python uses open addressing with probing, associating the values contiguously and non-linearly.

### How Python Handles Collisions

Python sets use **open addressing** instead of chaining (linked lists). When a collision occurs, Python searches for the next available slot using a pseudo-random probing sequence.

#### Open Addressing vs Chaining

```
Chaining (Java, C++):
[0] → None
[1] → [elem1] → [elem2] → [elem3]  (linked list)
[2] → [elem4]

Open Addressing (Python):
[0] None
[1] elem1
[2] elem2  ← collision with index 1, moved to next slot
[3] elem3  ← collision, continued probing
[4] None
```

#### Probing Algorithm

When inserting an element that collides:
```python
def insert(table, key):
    index = hash(key) % len(table)
    
    # Probing: search for next free slot
    while table[index] is not None:
        if table[index] == key:
            return  # already exists
        index = (index + 1) % len(table)  # next slot
    
    table[index] = key
```

**Example:**

```python
s = set()
# Assume hash(10) % 8 = 3
# Assume hash(18) % 8 = 3  (collision!)
# Assume hash(26) % 8 = 3  (collision!)

s.add(10)
s.add(18)
s.add(26)

# Table state:
# Index: [0][1][2][3][4][5][6][7]
# Value: [ ][ ][ ][10][18][26][ ][ ]
#                  ↑  ↑  ↑
#               hash=3
#                  collision→
#                     collision→
```

#### Expected Costs

| Scenario | Complexity | Probability |
|----------|------------|-------------|
| Average case | O(1) | ~99.9% |
| Table nearly full | O(n) | ~0% (resizes before) |
| Bad hash + full | O(n) | ~0% (Python prevents) |

**Why O(1) in practice:**

Python maintains a **low load factor** (~66%):
- When `size/capacity > 2/3`, the table is resized (doubled)
- With load factor α = 0.66, expected probes ≈ 3
- Good hash function distributes elements uniformly
- Pseudo-random probing avoids clustering

**Worst case O(n):**
Theoretically possible when:
- Table is 99% full
- Poor hash function (all elements collide)
- No resizing occurs

In practice, Python's automatic resizing and good hash functions ensure O(1) amortized performance.

## Main Characteristics

Sets can be used to remove duplicates from another lists

Sets can be used to do faster operations when compared to other structures, as a auxiliar data structure

- Seeing if sequences is contained in a list/stack/queue;
- If conditions faster to check if a desirable value is present in a list.

It's important to say that when using the sets as an auxiliar structure, you will consume more memory space equal *k*, being *k* the number of distinct elements.

## Functions | Operations

```python
val in set
val not in set
```

This operation, since sets uses hash functions to calculate, the only necessary thing is to associate the value into a hash function and then check if the result is the equal than the used in the operation.

**Average Cost: O(1)**

---

```python
set_s | set_t
```

This operation is the *union* operation, where the result is the distincts values in *set_s* + distincts values in *set_t*, without repeating them.
There, you can presume that it's like adding each value sequentially if it's not in the resultant set.

**Average Cost: O(len(set_s) + len(set_t))**

---

```python
set_s & set_t
```

This operation is the *intersection* operation, where the resultant set is the distinct values present in both *set_s* and *set_t*.

We can assume here that the best case is when a set is entirelly contained in the other set, so the cost would be the length of the set contained in the other one.
Unfortunatelly, the world isn't that beautiful, since both the sets can contain distinct values when compared to the other one, as also all the values colided, needing to iterate through the both sets and the entire collision in open addressing.

**Average Cost: O(min(len(s), len(t)))**
**Worst Case: O(len(s) * len(t))**

---

```python
set_s & ... & set_x
```

Multiple intersection can also be done, it's not sure the average case since the math behind it can be very complex, but we can ensure the worst case:

**Worst Case: (n - 1) * O(min(len(set_s), ..., len(set_x)))

---

```python
set_s - set_t
```

This operation is the *difference* operation, only maintaing the values in *set_s* that are not contained in *set_t*. You can presume that we need to iterate thorugh *set_s* entirely and check if each value is contained in *set_t*, and you're right!

**Average Cost: O(len(set_s))**

---

```python
set.difference_update(values: Iterable)
```

The major difference between this function and the *difference* operation is that the function doesn't create a new set as all operations do, but do an *in-place* update in the original set, only iterating through the parameter of length *k* and removing the values contained in the original set.

**Average Cost: O(k)**

---

```python
set_s ^ set_t
```

This operation is the *symmetric difference* operation, this operation results a set that only contains values inside *set_s* and not in *set_t*, as values inside *set_t* and not in *set_t*.

The average can be described as the cost of iterating through every element in the bigger set and only remove the values in the other set. When the worst case is iterating through both sets that are completely different, where each value occurred a collision.

**Average Cost: O(len(set_s))**
**Worst Cost: O(len(set_s) * len(set_t))**

---

```python
set.symmetric_difference_update(values: Iterable)
```

As the ```difference_update()``` method, this function changes the original set only adding the values that are contained in values, but not in both sets, as removes the values in the original set and are present in the parameter. Given an *k* length in the parameter:

**Average Cost: O(k)**
