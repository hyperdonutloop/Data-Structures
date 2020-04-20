import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # adds item to the back (tail) of the queue
        self.size += 1
        # calling function add to tail to add item to the back of the queue
        self.storage.add_to_tail(value)

    def dequeue(self):
        # remove and return and item in front of the queue
        # if there are items
        if self.size > 0:
            # we are reducing the size by one
            self.size -= 1
            # removing from head and returning that item
            return self.storage.remove_from_head()

    def len(self):
        # returns the number of items in the queue
        return self.size
