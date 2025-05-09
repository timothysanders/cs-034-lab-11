# Created by: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

# Date: 5/05/25

# Course: Spr25_CS_034 CRN 39575
#--------------------------------------------------------------------------------------------

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

def test_treap_insert_duplicate_key(capsys):
    treap = Treap()
    treap.root = treap.insert(treap.root, 10)
    treap.root = treap.insert(treap.root, 10)
    out, _ = capsys.readouterr()
    assert "already exists" in out
