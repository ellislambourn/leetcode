from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        # hashmap of {key: value}
        self.capacity = capacity
        self.queue = deque()
        self.hashmap = {}

    def get(self, key: int) -> int: # needs to update recently used
        if key not in self.hashmap:
            return -1
        # move key to most recent
        self.queue.remove(key)
        self.queue.append(key)
        return self.hashmap.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.queue.remove(key)

        elif len(self.queue) == self.capacity:
            lru = self.queue.popleft()
            del self.hashmap[lru]

        self.hashmap[key] = value
        self.queue.append(key)

        
        

