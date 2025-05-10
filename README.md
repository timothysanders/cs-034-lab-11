# Lab 11: Heaps and Treaps in Python
## Objective
- This lab helps you understand and implement two advanced data structures: **Binary Heaps** and **Treaps**. You’ll design, implement, and test their behavior using Python, while reflecting on their algorithmic performance in different contexts.

## Part 1: Design (Required)
### A. Binary Min-Heap
- Purpose
- Input / Output
- Pseudocode (insert, remove, peek)
- Data representation (array-based using list)
#### Pseudocode
```
import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        ADD item to end of heap
        PERCOLATE_UP item to maintain min-heap property

    def remove_min(self):
        IF self.heap IS EMPTY:
            RETURN None
        ELSE:
            SWAP first item with last item
            REMOVE last item
            PERCOLATE_DOWN new heap first item to maintain min-heap property
        RETURN last item

    def peek_min(self):
        IF self.heap IS EMPTY:
            RETURN None
        ELSE:
            RETURN first item in heap
    
    def percolate_up(index):
        WHILE index > 0 AND self.heap[index] < heap[parent index]:
            SWAP heap[index] and heap[parent index]
            SET index = parent index

    def percolate_down(index):
        WHILE index has at least one child:
            SET smaller_child_index to index of smaller child
            IF heap[index] > heap[smaller_child_index]:
                SWAP heap[index] with heap[smaller_child_index]
                SET index to smaller_child_index
            ELSE:
                BREAK
```

### B. Treap
- Purpose
- Input / Output
- Pseudocode (insert with priority, rotation logic, search)
- Data representation (class-based with key and priority)
#### Pseudocode
```
import random

class TreapNode:
    def __init__(self, key):
        self.key = key
        self.priority = random.randint(1, 100)
        self.left = None
        self.right = None

class Treap:
    def __init__(self):
        self.root = None

    def rotate_left(self, root):
        # TODO: Implement left rotation 
        Set the new parent node as the node’s right child
        Set the node’s right child as the left child of the new parent node
        Set the new parent node’s left child as the node
    
    def rotate_right(self, root):
        # TODO: Implement right rotation Set the new parent node as the node’s left child
        Set the node’s left child as the right child of the new parent node
        Set the new parent node’s right child as the node

    def insert(self, root, key):
        # TODO: Insert node using BST 
        IF there is no root, create a node

        IF the key is less than the parent node’s key, set it as the left child
        IF the key is less than the parent node’s key but the priority is greater than the parent’s priority, rotate right
    
        IF the key is greater than the parent node’s key, set it as the right child
        IF the key is greater than the parent node’s key but the priority is greater than the parent’s priority, rotate left

        # TODO: Apply rotations based on priority
        See above

    def search(self, root, key):
        # TODO: Search for a key using BST logic
        IF the tree does not have a root, return

        IF the key is equal to the root node, return the root’s key

        IF the key is less than the root node, recursively search the root’s left child

        ELSE recursively search the root’s right child 
```
## Part 2: Implementation (Use TODOs)
### A. Min-Heap (Using List)
- Create a new file called `min_heap.py`.
```python
import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        # TODO: Use heapq to insert item into the heap
        pass

    def remove_min(self):
        # TODO: Use heapq to remove and return the smallest item
        pass

    def peek_min(self):
        # TODO: Return the smallest item without removing it
        pass
```
### B. Treap (Manual Implementation)
- Create a new file called `treap.py`.
```python
import random

class TreapNode:
    def __init__(self, key):
        self.key = key
        self.priority = random.randint(1, 100)
        self.left = None
        self.right = None

class Treap:
    def __init__(self):
        self.root = None

    def rotate_left(self, root):
        # TODO: Implement left rotation logic
        pass

    def rotate_right(self, root):
        # TODO: Implement right rotation logic
        pass

    def insert(self, root, key):
        # TODO: Insert node using BST rules
        # TODO: Apply rotations based on priority
        pass

    def search(self, root, key):
        # TODO: Search for a key using BST logic
        pass
```

## Part 3: Testing & Reflection
### Testing (tests.py)
- Write small test cases to verify:
  - Heap returns smallest value.
  - Treap maintains key and priority structure.
  - Search functions return expected results.
```python
# TODO: Create MinHeap instance and test insert/remove
# TODO: Create Treap instance and test insert/search
```
### Reflection (Submit as PDF or DOCX)
- Write 1–2 paragraphs addressing:
  - How does the heap maintain order with percolation?
  - How do priorities help the treap stay balanced?
  - When would you use a heap vs. a treap?
- Submit as: `reflection.pdf` or `reflection.docx`

## Deliverables (Submit via Canvas as a .zip folder)
- `min_heap.py`
- `treap.py`
- `tests.py`
- `design.pdf` (for both structures)
- `reflection.pdf` or `reflection.docx`

## Grading Rubric (30 points)
| Component                          | Points  |
|------------------------------------|---------|
| Design (Section 5.6)               | 10      |
| Heap + Treap Code (TODO filled in) | 10      |
| Testing                            | 5       |
| Reflection                         | 5       |
