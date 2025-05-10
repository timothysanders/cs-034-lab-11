# Created by: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

# Date: 5/05/25

# Course: Spr25_CS_034 CRN 39575

#--------------------------------------------------------------------------------------------

import heapq
import math

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
        print(f"Inserting {item} into the heap")
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
        print(f"Removing the minimum element {self.heap[0]} from the heap")
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
        print(f"The minimum element in the heap is {self.heap[0]}")
        return self.heap[0]

    def __str__(self) -> str:
        """
        Print the binary heap as a tree-like structure.

        Returns
        -------
        str
        """
        return_string = "Min-Heap Tree Representation".center(80) + "\n"
        if not self.heap:
            return_string += "<empty heap>"
            return return_string

        height = math.floor(math.log2(len(self.heap))) + 1
        max_width = 2 ** (height - 1)

        index = 0
        for level in range(height):
            level_width = 2 ** level
            padding = " " * (max_width // level_width)
            line = ""
            for _ in range(level_width):
                if index >= len(self.heap):
                    break
                line += f"{padding}{self.heap[index]}{padding}"
                index += 1
            return_string += line.center(80) + "\n"
        return return_string.rstrip("\n")

    def print_tree(self) -> None:
        """
        Prints a visual representation of the existing heap tree structure.

        Returns
        -------
        None
        """
        def _print_tree(index, indent):
            if index >= len(self.heap):
                return
            right = 2 * index + 2
            left = 2 * index + 1
            _print_tree(right, indent + "   ")
            print(f"{indent}{self.heap[index]}")
            _print_tree(left, indent + "   ")
        print("Heap Tree Structure:")
        _print_tree(0, "")


if __name__ == "__main__":
    heap = MinHeap()
    for num in [10, 4, 7, 1, 8, 3, 9]:
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
        heap.remove_min()
        print()
        # Print the deconstructed Heap
        heap.print_tree()
        print()

    print("Min-Heap List Representation".center(80))
    print(f"{heap.heap}".center(80))
