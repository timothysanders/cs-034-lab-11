# Lab 11: Heaps and Treaps in Python
## Objective
- This lab helps you understand and implement two advanced data structures: **Binary Heaps** and **Treaps**. You’ll design, implement, and test their behavior using Python, while reflecting on their algorithmic performance in different contexts.

## Part 1: Design (Required)
### A. Binary Min-Heap
- Purpose
- Input / Output
- Pseudocode (insert, remove, peek)
- Data representation (array-based using list)

### B. Treap
- Purpose
- Input / Output
- Pseudocode (insert with priority, rotation logic, search)
- Data representation (class-based with key and priority)

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
