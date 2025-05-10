"""
Created by: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

Date: 5/05/25

Course: Spr25_CS_034 CRN 39575

Tests Covered
-------------
Heap
    - test_insert_and_peek_min
        Validates the MinHeap class insert method and that peek returns the correct minimum value
    - test_remove_min
        Validates that sequential remove_min() calls return the correct minimum value
    - test_peek_min_on_empty_heap
        Validates that an IndexError is appropriately raised when calling peek_min() on an empty heap
    - test_remove_min_on_empty_heap
        Validates that an IndexError is appropriately raised when calling remove_min() on an empty heap
    - test_insert_duplicates
        Validates that duplicates are appropriately inserted and returned from the heap
Treap
    - test_treap_rotation_count
        Validates that rotations are performed after a series of inserts and are logged
    - test_treap_insert_and_search
        Validates that the Treap.search() method returns the found integer key from the treap
    - test_treap_insert_nonexistent_search
        Validates that the Treap.search() method returns None for a key that is not found
    - test_treap_insert_duplicate_key
        Validates that duplicate keys are not entered and a message is returned
"""
import random
import time

import pytest
from min_heap import MinHeap
from treap import Treap

def test_insert_and_peek_min():
    heap = MinHeap()
    heap.insert(5)
    assert heap.peek_min() == 5

    heap.insert(3)
    assert heap.peek_min() == 3  # 3 is now the min

    heap.insert(8)
    assert heap.peek_min() == 3  # still 3

def test_remove_min():
    heap = MinHeap()
    values = [10, 4, 7, 1]
    for v in values:
        heap.insert(v)

    assert heap.remove_min() == 1
    assert heap.remove_min() == 4
    assert heap.remove_min() == 7
    assert heap.remove_min() == 10

def test_peek_min_on_empty_heap():
    heap = MinHeap()
    with pytest.raises(IndexError, match="Heap is empty"):
        heap.peek_min()

def test_remove_min_on_empty_heap():
    heap = MinHeap()
    with pytest.raises(IndexError, match="Heap is empty"):
        heap.remove_min()

def test_insert_duplicates():
    heap = MinHeap()
    heap.insert(2)
    heap.insert(2)
    heap.insert(1)
    heap.insert(1)
    assert heap.remove_min() == 1
    assert heap.remove_min() == 1
    assert heap.remove_min() == 2
    assert heap.remove_min() == 2

def test_treap_rotation_count():
    treap = Treap()
    for val in [90, 100, 110, 150, 160]:
        treap.root = treap.insert(treap.root, val)
    assert treap.rotation_count > 0
    assert all("rotation" in log.lower() for log in treap.log)

def test_treap_insert_and_search():
    treap = Treap()
    for val in [400, 401, 500, 501, 600, 601]:
        treap.root = treap.insert(treap.root, val)

    assert treap.search(treap.root, 400) == 400
    assert treap.search(treap.root, 401) == 401
    assert treap.search(treap.root, 500) == 500
    assert treap.search(treap.root, 501) == 501
    assert treap.search(treap.root, 600) == 600
    assert treap.search(treap.root, 601) == 601

def test_treap_insert_nonexistent_search():
    treap = Treap()
    treap.root = treap.insert(treap.root, 400)
    assert treap.search(treap.root, 500) is None

def test_treap_insert_duplicate_key(capsys):
    treap = Treap()
    treap.root = treap.insert(treap.root, 10)
    treap.root = treap.insert(treap.root, 10)
    out, _ = capsys.readouterr()
    assert "already exists" in out


if __name__ == "__main__":
    # Run basic tests to create MinHeap instance and test insert/remove
    # Instantiate MinHeap instance
    heap = MinHeap()
    for num in [10, 4, 7, 1, 8, 3, 9]:
        # Insert items into heap
        heap.insert(num)
        print(heap.heap)
    print(heap)
    print("\n\n                     =====================================")
    print("Min-Heap List Representation".center(80))
    # Print constructed Heap
    print(f"{heap.heap}".center(80))
    print("                     =====================================\n")

    # Loop to repeatedly remove the minimum element
    for _ in range(3):  # Remove the minimum 3 times
        heap.peek_min()
        # Remove items from heap
        heap.remove_min()
        print()
        # Print the deconstructed Heap
        heap.print_tree()
        print()

    print("Min-Heap List Representation".center(80))
    print(f"{heap.heap}".center(80))

    # Run basic tests to create Treap instance and test insert/search
    # Instantiate Treap instance
    treap = Treap()
    treap_values = random.sample(range(1, 100), 7)

    for value in treap_values:
        # Insert values into Treap and verify structure
        treap.root = treap.insert(treap.root, value)
        print("\nTree Structure:")
        print("----------------\n")
        treap.print_tree(treap.root)
        print("\n\n==================================================")

    treap.print_tree()
    print(f"\nTotal Rotations: {treap.rotation_count}")
    print("\nLog of Rotations")
    print("=========================")
    for log_entry in treap.log:
        print(log_entry)

    print()
    search_keys = [50, 80, 10]
    start_time = time.time()
    for v in search_keys:
        # Validate search operation for Treap instance
        result = treap.search(treap.root, v)
        print(f"Search result for {v}: {result}")
    end_time = time.time()
    print(f"\nTotal searching time: {end_time - start_time} seconds")
