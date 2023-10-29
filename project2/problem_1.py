class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRU_Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node):
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_front(node)
            return node.value
        return -1

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
        elif len(self.cache) >= self.capacity:
            # Remove the least recently used item (from the end of the linked list)
            del self.cache[self.tail.prev.key]
            self._remove(self.tail.prev)
        # Add the new key-value pair to the cache
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add_to_front(new_node)

# Example usage:
print("Test case 0:")
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))  # returns -1

# Test Case 1: Normal Operation
print("Test case 1:")
our_cache = LRU_Cache(3)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)

# Cache: [1 -> 2 -> 3]
print(our_cache.get(2))  # returns 2
print(our_cache.get(1))  # returns 1

# Getting the same value over and over again to see if the program works
print(our_cache.get(1))  # returns 1 

# Getting only invalid values
print(our_cache.get(10))  # returns -1 

our_cache.set(4, 4)
# Cache is full, so the least recently used item (3) should be removed
# Cache: [2 -> 1 -> 4]
print(our_cache.get(3))  # returns -1 (cache miss)

# Test Case 2: Edge Case - Cache Capacity of 1
print("Test case 2:")
our_cache = LRU_Cache(1)
our_cache.set(1, 1)

# Cache: [1]
print(our_cache.get(1))  # returns 1

our_cache.set(2, 2)
# Cache is full, so the least recently used item (1) should be removed
# Cache: [2]
print(our_cache.get(1))  # returns -1 (cache miss)

# Test Case 3: Edge Case - Large Cache Capacity
print("Test case 3:")
our_cache = LRU_Cache(1000)

# Adding 1000 key-value pairs
for i in range(1000):
    our_cache.set(i, i)

# Cache: [999 -> 998 -> ... -> 3 -> 2 -> 1 -> 0]
print(our_cache.get(0))    # returns 0
print(our_cache.get(999))  # returns 999
print(our_cache.get(500))  # returns 500

# Test case 4: Adding cases where the input is NULL, negative, or high capacity.    print("Test case 3:")
print("Test case 4:")

our_cache = LRU_Cache(1)

our_cache.set(1, None)

print(our_cache.get(1))    # returns None
print(our_cache.get(-1))  # returns -1