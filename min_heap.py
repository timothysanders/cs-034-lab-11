import heapq

from typing import Any

class MinHeap:
    """
    Implement a Min-heap using the heapq library.

    Attributes
    ----------
    heap : list

    Methods
    -------
    insert(item)
        Insert an item into the heap.
    remove_min()
        Remove and return the smallest item in the heap.
    peek_min()
        Return (but doesn't remove) the smallest item in the heap.
    """
    def __init__(self):
        self.heap = []

    def insert(self, item: Any) -> None:
        """
        Insert an item into the heap.

        Parameters
        ----------
        item : Any

        Returns
        -------
        None
        """
        heapq.heappush(self.heap, item)

    def remove_min(self) -> Any:
        """
        Remove and return the smallest item in the heap.

        Returns
        -------
        Any

        Raises
        ------
        IndexError
            If the heap is empty
        """
        if not self.heap:
            raise IndexError("Heap is empty")
        return heapq.heappop(self.heap)

    def peek_min(self) -> Any:
        """
        Return (but doesn't remove) the smallest item in the heap.

        Returns
        -------
        Any

        Raises
        ------
        IndexError
            If the heap is empty
        """
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]
