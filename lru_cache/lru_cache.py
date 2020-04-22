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
        # this means key does not exist
        if key not in self.storage:
            return None
        # key is in cache
        else:
            # assigning node to self.storage which is the dict and choosing key
            node = self.storage[key]
            # because an item has been retrieved, it becomes most recently used
            self.order.move_to_end(node)
            # return value at 1 because you are always adding at position 1
            return node.value[1]

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
            # calling the key
            node = self.storage[key]
            # then assigning the new value
            node.value = (key, value)
            # move to the tail/end (most recently used) because when you put in something new, it is now the most recently used
            self.order.move_to_end(node)
            return

        # size is at limit
        if len(self.order) == self.limit:
            # assigning the variable t0 the oldest item(calling the key)
            index_of_oldest = self.order.head.value[0]
            # evict the oldest one/ deleting that item
            del self.storage[index_of_oldest]
            # 
            self.order.remove_from_head()
            # add new one to the end
        
    
        # add to order
        self.order.add_to_tail((key, value)) # using a tuple bc? # cannot mutate things inside tuple.
        # add it to storage
        self.storage[key] = self.order.tail

