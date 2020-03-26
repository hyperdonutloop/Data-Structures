from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        # this is the max number of nodes it can hold
        self.limit = limit
        # this is the current number of nodes it is holding
        self.size = 0
        # the DLL that holds the key-value entries in the correct order
        self.order = DoublyLinkedList()
        # storage dict that provides fast access to every node stored in the cache
        self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # key is not in cache - return none
        if key not in self.storage:
            return None
        else:
            # key is in cache
            node = self.storage[key]
            # move to most recently used
            self.order.move_to_end(node)
            # return value
            return node.value[1]


        # # if there is a key in the storage
        # if key in self.storage:
        #     # assigning node to the key in storage
        #     node = self.storage[key]
        #     # moving node to end
        #     self.order.move_to_end(node)
        #     # returning value associated with key
        #     return node.value[1]
        # else:
        #     return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # if item/key already exists
        if key in self.storage:
            # overwrite the value
            # where is the value stored?
            node = self.storage[key]
            node.value = (key, value)
            # move to the tail (most recently used)
            self.order.move_to_end(node)
            return

        # size is at limit
        if len(self.order) == self.limit:
            # evict the oldest one
            # saved as a tuple (key, value) [0] is key
            index_of_oldest = self.order.head.value[0]
            del self.storage[index_of_oldest]
            self.order.remove_from_head()
            # add new one to the end
        
    
        # add to order
        self.order.add_to_tail((key, value)) # using a tuple bc?
        # add it to storage
        self.storage[key] = self.order.tail

        






        # if key in self.storage:
        #     node = self.storage[key]
        #     node.value = (key, value)
        #     self.order.move_to_end(node)
        #     return
        
        # if self.size == self.limit:
        #     del self.storage[self.order.head.value[0]]
        #     self.order.remove_from_head()
        #     self.size -= 1

        # self.order.add_to_tail((key, value))
        # self.storage[key] = self.order.tail
        # self.size += 1
