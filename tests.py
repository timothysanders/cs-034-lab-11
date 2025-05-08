# Created by: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

# Date: 5/05/25

# Course: Spr25_CS_034 CRN 39575
#--------------------------------------------------------------------------------------------

import pytest
from min_heap import MinHeap

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
