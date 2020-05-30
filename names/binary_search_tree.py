"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

import sys

# from queue import Queue
# from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # START with insert ...duh you need something in our tree to work w/ the tree.
    def insert(self, value):
        # if value < node.value look left   **
        if value < self.value:
            # if something is already there  # same as.... if self.left is not None:   - if a node exists
            if self.left:                
                 # recurse left
                 self.left.insert(value)
            # if not 
            else:
                # make a new node
                self.left = BSTNode(value)

        # if value is >= node.value look right
        if value >= self.value:
            # if something is already there
            if self.right:
                # recurse right
                self.right.insert(value)
            # if not
            else:
                # make a new node
                self.right = BSTNode(value)


# ---------------------------------------------------
        # if value >= self.value:
        #     if self.right is not None:   # same as if self.right:
        #         self.right.insert(value)
        #     else:
        #         self.right = BSTNode(value)

        # else:
        #     if self.left is not None:
        #         self.left.insert(value)
        #     else:
        #         self.left = BSTNode(value)
#-----------------------------------------------------

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        if target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False


# def contains(self, target):
#         current = self
#         while current:
#             if current.value == target:
#                 return True
#             elif current.value > target:
#                 if current.left is None:
#                     return False
#                 current = current.left
#             elif current.value < target:
#                 if current.right is None:
#                     return False
#                 current = current.right

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

# def get_max(self):
#     current_node = self
#     while current_node.right is not None:
#         current_node = current_node.right

#     return current_node.value






    # Call the function `fn` on the value of each node
    # NOTE YOU DO NOT HAVE TO DO THIS ONE
    def for_each(self, fn):
        # call fn on self.value
        fn(self.value)
        # if left
        if self.left:
            # call for_each
            self.left.for_each(fn)
        #if right
        if self.right:
            # call for_each
            self.right.for_each(fn)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    # def in_order_print(self, node):
    #     if node.left is not None:
    #         self.in_order_print(node.left)

    #     print(node.value)

    #     if node.right is not None:
    #         self.in_order_print(node.right)

    # # Print the value of every node, starting with the given node,
    # # in an iterative breadth first traversal
    # def bft_print(self, node):
    #     # make a queue
    #     q = Queue()
    #     # enqueue the node
    #     q.enqueue(node)
    #     # as long as the queue is not empty
    #     while len(q) > 0:
    #     # dequeue from the front of the queue, this is our current node
    #         current_node =  q.dequeue()
    #         print(current_node.value)
    #         # enqueue the kids on current node on the queue
    #         if current_node.left is not None:
    #             q.enqueue(current_node.left)
    #         if current_node.right is not None:
    #             q.enqueue(current_node.right)


    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    # def dft_print(self, node):
    #     # make a stack
    #     stack = Stack()
    #     # push the node on the stack
    #     stack.push(node)
    # # as long as the stack is not empty
    #     while len(stack) > 0:
    #     #pop off the stack - our current node
    #         current_node = stack.pop()
    #         print(current_node.value)
    #     ## put the kids of the current node on the stack
    #     if current_node.left:
    #         stack.push(current_node.left)
    #     if current_node.right:
    #         stack.push(current_node.right)
    #     # check that they are not None, then put them on the stack

    # # Stretch Goals -------------------------
    # # Note: Research may be required

    # # Print Pre-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass
