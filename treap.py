# Created by: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

# Date: 5/05/25

# Course: Spr25_CS_034 CRN 39575

#--------------------------------------------------------------------------------------------


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
