# Created by: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

# Date: 5/05/25

# Course: Spr25_CS_034 CRN 39575

#--------------------------------------------------------------------------------------------



# Re-implementing with capped depth and safer rotation logic

import random
import sys
sys.setrecursionlimit(2000)  # Allow deeper recursion for printing

class TreapNode:
    def __init__(self, key):
        self.key = key
        self.priority = random.randint(1, 100)
        self.left = None
        self.right = None

class Treap:
    def __init__(self):
        self.root = None
        self.rotation_count = 0
        self.log = []

    def rotate_left(self, root):
        if not root or not root.right:
            return root
        self.rotation_count += 1
        self.log.append(f"Left rotation on node {root.key}")
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        return new_root

    def rotate_right(self, root):
        if not root or not root.left:
            return root
        self.rotation_count += 1
        self.log.append(f"Right rotation on node {root.key}")
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        return new_root

    def _insert(self, root, key):
        if root is None:
            print(f"Creating new node with key: {key}")
            return TreapNode(key)

        if key < root.key:
            print(f"Going left from {root.key}")
            root.left = self._insert(root.left, key)
            if root.left and root.left.priority > root.priority:
                print(f"Rotating right on {root.key} to restore heap property")
                root = self.rotate_right(root)
        elif key > root.key:
            print(f"Going right from {root.key}")
            root.right = self._insert(root.right, key)
            if root.right and root.right.priority > root.priority:
                print(f"Rotating left on {root.key} to restore heap property")
                root = self.rotate_left(root)
        else:
            print(f"Key {key} already exists in the tree")

        return root

    def insert(self, key):
        self.root = self._insert(self.root, key)


    def search(self, root, key):
        if not root:
            return None

        if key == root.key:
            return root.key
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)


    def print_tree(self, root=None, level=0, indent=""):
        #if root is None:
            #root = self.root
        #if level > 10:  # Avoid infinite loops or very deep trees
            #print(indent + "...")
            #return
        if root:
            self.print_tree(root.right, level + 1, indent + "    ")
            print(indent + f"({root.key}/{root.priority})")
            self.print_tree(root.left, level + 1, indent + "    ")

if __name__ == "__main__":
    treap = Treap()
    treap_values = [50, 30, 70, 20, 40, 60, 80]

    for value in treap_values:
        treap.insert(value)
        print()

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
