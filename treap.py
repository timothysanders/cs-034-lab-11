# Created by: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

# Date: 5/05/25

# Course: Spr25_CS_034 CRN 39575

#--------------------------------------------------------------------------------------------

from __future__ import annotations
import time
from typing import Any
import random
import sys
sys.setrecursionlimit(2000)  # Allow deeper recursion for printing

class TreapNode:
    """
    Implements a treap node.

    Attributes
    ----------
    key : Any
    priority : int
    left : TreapNode
    right : TreapNode
    """

    def __init__(self, key):
        self.key: Any = key
        self.priority: int = random.randint(1, 100)
        self.left: TreapNode = None
        self.right: TreapNode = None

class Treap:
    """
    A Treap (Tree/Heap) implementation supporting insertion, rotation, and search.

    Attributes
    ----------
    root : TreapNode
        The root node of the treap.
    rotation_count : int
        The total number of rotations performed during insertions.
    log : list
        A list recording each rotation that occurs.

    Methods
    -------
    rotate_left
        Performs a left rotation around the given node.
    rotate_right
        Perform a right rotation around the given node.
    insert
        Insert a key into the treap while maintaining heap and BST properties.
    search
        Search for a key in the treap.
    print_tree
        Recursively print the tree structure of the treap.
    """
    def __init__(self):
        self.root: TreapNode = None
        self.rotation_count: int = 0
        self.log: list = []

    def rotate_left(self, root: TreapNode) -> TreapNode:
        """
        Perform a left rotation around the given node.

        Parameters
        ----------
        root : TreapNode
            The root node around which to perform the left rotation.

        Returns
        -------
        TreapNode
            The new root node after rotation.
        """
        if not root or not root.right:
            return root
        self.rotation_count += 1
        self.log.append(f"Left rotation on node {root.key}")
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        return new_root

    def rotate_right(self, root: TreapNode) -> TreapNode:
        """
        Perform a right rotation around the given node.

        Parameters
        ----------
        root : TreapNode
            The root node around which to perform the right rotation.

        Returns
        -------
        TreapNode
            The new root node after rotation.
        """
        if not root or not root.left:
            return root
        self.rotation_count += 1
        self.log.append(f"Right rotation on node {root.key}")
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        return new_root

    def insert(self, root: TreapNode, key: Any) -> TreapNode:
        """
        Insert a key into the treap while maintaining heap and BST properties.

        Parameters
        ----------
        root : TreapNode
            The root of the treap subtree where the key should be inserted.
        key : Any
            The key to insert into the treap.

        Returns
        -------
        TreapNode
            The root node of the updated subtree.
        """
        if root is None:
            print(f"Creating new node with key: {key}")
            return TreapNode(key)

        if key < root.key:
            print(f"Going left from {root.key}")
            root.left = self.insert(root.left, key)
            if root.left and root.left.priority > root.priority:
                print(f"Rotating right on {root.key} to restore heap property")
                root = self.rotate_right(root)
        elif key > root.key:
            print(f"Going right from {root.key}")
            root.right = self.insert(root.right, key)
            if root.right and root.right.priority > root.priority:
                print(f"Rotating left on {root.key} to restore heap property")
                root = self.rotate_left(root)
        else:
            print(f"Key {key} already exists in the tree")

        return root


    def search(self, root: TreapNode, key: Any) -> Any | None:
        """
        Search for a key in the treap.

        Parameters
        ----------
        root : TreapNode
            The root of the treap subtree to search.
        key : Any
            The key to search for.

        Returns
        -------
        Any or None
            The key if found, otherwise None.
        """
        if not root:
            return None

        if key == root.key:
            return root.key
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)


    def print_tree(self, root: TreapNode = None, indent: str = "") -> None:
        """
        Recursively print the tree structure of the treap.

        Parameters
        ----------
        root : TreapNode, optional
            The root of the subtree to print. If None, starts at the treap root.
        indent : str, default=""
            Indentation used to format the tree output.

        Returns
        -------
        None
        """
        if root:
            self.print_tree(root.right, indent + "         ")
            print(indent + f"({root.key}/{root.priority/100})")
            self.print_tree(root.left, indent + "         ")

if __name__ == "__main__":
    treap = Treap()
    treap_values = [50, 30, 70, 20, 40, 60, 80]

    for value in treap_values:
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
        result = treap.search(treap.root, v)
        print(f"Search result for {v}: {result}")
    end_time = time.time()
    print(f"\nTotal execution time: {end_time - start_time} seconds")
