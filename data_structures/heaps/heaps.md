# Introduction

Also called binary heaps or nearly complete binary tree. Looking at it as a tree, all levers are filled but the lowest, when the lowest level are filled until a certain point, starting from the left.

Two common usages for heaps is to create priority queues or the Heap Sort algorithm. Also, heaps can be divided in two main categories, as the Min-Heaps and the Max-Heaps.

## Max-Heaps

In the Max-Heaps, we can define it as: the childs of a determined node have always a lower or equal value than the node, as the node itself has a **lower or equal value than it's parent**.

## Min-Heap

The Min-Heap uses the the same condition as the Max-Heaps, but instead of the childs having a lower or equal value than it's parents, the child have a **higher or equal value**.

This type of heaps are the preferred to implement Priority Queues.

## Characteristics

**Height**: The height of a heap can be defined, in the worst case, as `O(log n)`.

**Finding the childs**: Looking at a heap as an array, the *left child* of a node in the index *i* can be found at the index *(2 x i) + 1*, and the *right child* in the index *(2 x i) + 2*.

**Parent of a Node**: The parent of a determined node in the index *i* can be found as the *floor of (i - 2)/2*.

**Heapifying**: Actually, every moment you do an operation that changes the Heap structure, you must heapify the structure again to move the items as necessary.

- Pooling an item needs to heapify looking down to define a new root value, since it must define the new root as the last value and then rearrange the structure;
- Appending a new value in the final of the list also may require to heapify looking upwards (moving the item to the up) depending of the value;
- While heapifying downward, you only need to iterate through the left childs, since the insertion always start at the left.

## Some Use-Cases

**Finding *k* Most/Less Frequent Values**: Since heaps allow you to insert values based in a max/min heap, you can use it to insert/remove values and follows the order you want.

**Processing Tasks by Priority**: As you can define values/priorities, Heaps allow you to sort the data in a way to define the "most important" one first, while the others are already in the order.

**Routing/Djikstra**: The Heaps can define the next best node to walk through a path to help finding a way to the destiny from the origin.

### Key Insight

Whenever you need to use "the best" one, or access repeatdly the best element through some criteria, heaps could the the Data Structure to help you to resolve the situation.

---

## Functions

For the below functions, in `Python` you can add the ```_max``` before the arguments of every functions to use the Max-Heap. By default, the built-in lib `heapq` in Python uses Min-Heaps. Another alternative to use Max-Heap, is using negative values.

---

```python
heapq.heapify(heap: list)
heapq.heapify_max(heap: list)
```

Heapify a list into a heap (min or max, based in which function you used). The transformation are made in-place, without consuming more space.

**Average Cost: O(n)**

---

```python
heapq.heappush(heap: list, item: list | tuple | object)
```

This function allows you to add a new element into the Heap structure following the criteria (Min or Max). Since the function automatically heapify after the insertion, the cost increase due to the heapify operation.
If using an object, it needs to implement the `__lt__` function to be used in a heap.

**Average Cost: O(log n)**

---

```python
heapq.heappop(heap: list)
```

This functions pops the lowest value if using Min-Heap, or the higher value if using Max-Heap. As the `heappush()` operation, after this functions, the heap are automatically heapified.

**Average Cost: O(log n)**

---

```python
heapq.heappushpop(heap: list, item: list | tuple | object)
```

This function push the item in the heap and also executes the `heappop()` function, returning the lowest value in the Heap (again, if you are not using the `_max` variant). It is pretty faster than using `heappush()` followed by `heappop()` since you would need to heapify the structure two times. This functions only heapify one time.

**Average Cost: O(log n)**

---

```python
heapq.heareplace(heap: list, item: list | tuple | object)
```

This functions does the opposite than the `heappushpop()`, since it first pop the value and then insert the new element. This can create some concerns since it won't necessarily will return a value lower than the element to be inserted, but the heap principles are being used there.
This alternative can be really good if you're working with fixed-size heap.

This function also is faster than using `heappop()` followed by `heappush()` since it only heapify the heap one time.

**Average Cost: O(log n)**
