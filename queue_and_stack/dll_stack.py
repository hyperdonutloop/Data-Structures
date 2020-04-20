import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

# stack is LIFO 
class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def push(self, value):
        # increasing the size by 1
        self.size += 1
        # adding new item to the stack. 
        self.storage.add_to_head(value)

    def pop(self):
        # if there are items
        if self.size > 0:
            # decreasing the size
            self.size -= 1
            # calling remove from head and returning that item
            # when you are adding and removing from a stack it's always the top one, and the top is always the head
            return self.storage.remove_from_head()
        else:
            return None

    def len(self):
        return self.size
