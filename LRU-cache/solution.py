from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        # hashmap of {key: value}
        self.capacity = capacity
        self.hashmap = OrderedDict()

    def get(self, key: int) -> int: # needs to update recently used
        if key not in self.hashmap:
            return -1
        # move key to most recent
        self.hashmap.move_to_end(key)
        return self.hashmap[key]

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            # then i need to move it back to the end
            self.hashmap.move_to_end(key)
        self.hashmap[key] = value

        if len(self.hashmap) > self.capacity:
            self.hashmap.popitem(last = False)
        
        
        

