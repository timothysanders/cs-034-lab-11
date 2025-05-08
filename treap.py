# Created by: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

# Date: 5/05/25

# Course: Spr25_CS_034 CRN 39575

#--------------------------------------------------------------------------------------------


# 🛠️❌🛠️❌🛠️❌🛠️❌🛠️❌🛠️❌🛠️❌🛠️❌🛠️❌🛠️❌🛠️❌🛠️❌🛠️❌🛠️❌🛠️❌🛠️❌🛠️❌🛠️❌

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

    def insert(self, root, key):
        if root is None:
            print(f"Creating new node with key: {key} as root")
            return TreapNode(key)

        if key < root.key:
            print(f"Going left from {root.key}")
            root.left = self.insert(root.left, key)
            if root.left.priority > root.priority:
                print(f"Rotating right on {root.key} to restore heap property")
                root = self.rotate_right(root)
        elif key > root.key:
            print(f"Going right from {root.key}")
            root.right = self.insert(root.right, key)         
            if root.right.priority > root.priority:
                print(f"Rotating left on {root.key} to restore heap property")
                root = self.rotate_left(root)
        else:
              pass  # Handle duplicates if needed

        return root

    def print_tree(self, root=None, level=0, indent=""):
        #if root is None:
            #root = self.root
        #if level > 10:  # Avoid infinite loops or very deep trees
            #print(indent + "...")
            #return
        if root:
            self.print_tree(root.right, level + 1, indent + "    ")
            print(indent + f"({root.key}, P:{root.priority})")
            self.print_tree(root.left, level + 1, indent + "    ")

# Re-run the corrected implementation
treap = Treap()
treap_values = [50, 30, 70, 20, 40, 60, 80]

for value in treap_values:
    treap.root = treap.insert(treap.root, value)
    print()

treap.print_tree()
print(f"Total Rotations: {treap.rotation_count}")
print("\nLog of Rotations")
print("=========================")
for log_entry in treap.log:
    print(log_entry)
