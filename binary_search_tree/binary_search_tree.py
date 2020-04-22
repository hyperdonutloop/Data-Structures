import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if new value is less than current node:
        if value < self.value:
            # is there already a value at self.left
            # no ->
            if not self.left:
                self.left = BinarySearchTree(value)
                # after this ^, left is a new 'self' with it's own L/R
            # yes ->
            else:
                # then insert a the left
                self.left.insert(value)
        # if the value is greater:
        else:
            # is there a right? 
            # if there is not a right then
            if not self.right:
                # add it to the right
                self.right = BinarySearchTree(value)
            else:
                # if then insert that value
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the value is the target then return true
        if self.value == target:
            return True
        # go left
        # if target is less than self.value
        if target < self.value:
            # and it's not on the left
            if not self.left:
                # return false
                return False
            # otherwise
            else:
                # return the value of the target
                return self.left.contains(target)
        # go right
        else:
            # if it is not found
            if not self.right:
                # return false
                return False
            # otherwise
            else:
                # target is found and return that value
                return self.right.contains(target)

    # Return the maximum value found in the tree
    # self = root
    def get_max(self):
        # 1. if the tree is empty
        if not self:
            # returning None
            return None
        # 2. Otherwise, recur down the tree always going right
        # if you get to Null
        if not self.right:
            # then return last value found(we have found the value we need)
            return self.value
        # if there is something on the right, then return that value and call get max
        # this makes the function run again on the current node you are at
        # this is recursion
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # going through left then right node values
        # printing values low to high
        if node:
            if node.left:
                self.in_order_print(node.left)
            print (f'{node.value}')
            if node.right:
                self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    # BFT 
    # initialize a queue
    # push root to queue
    # while stack is not empty
    # pop top item out of queue into temp
    # print/return what you are doing
    # if temp has right, put into queue
    # if temp has left, put into queue
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        temp = queue.storage.head.value
        while queue.size > 0:
            temp = queue.dequeue()
            print(temp.value)
            if temp.right:
                queue.enqueue(temp.right)
            if temp.left:
                queue.enqueue(temp.left)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        temp = stack.storage.head.value
        while stack.size > 0:
            print(temp.value)
            if temp.right:
                stack.push(temp.right)
            if temp.left:
                stack.push(temp.left)
            temp = stack.pop()
    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node:
            print(f"{node.value}")
            if node.left:
                self.pre_order_dft(node.left)
            if node.right:
                self.pre_order_dft(node.right)

    # Print Post-order recursive DFT

    def post_order_dft(self, node):
        if node:
            if node.left:
                self.post_order_dft(node.left)
            if node.right:
                self.post_order_dft(node.right)
            print(f"{node.value}")
