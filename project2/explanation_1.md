# Problem 1: LRU Cache

In this code, we are implementing an LRU (Least Recently Used) cache, a data structure that maintains a limited number of items, evicting the least recently used item when the capacity is exceeded. The cache uses a combination of a dictionary and a doubly linked list to achieve efficient access and eviction of items. 

## Class Definitions

### Node:
A `Node` class represents the individual elements in the doubly linked list. Each node contains a `key`, `value`, `prev` (a reference to the previous node), and `next` (a reference to the next node).

### LRU_Cache:
The `LRU_Cache` class is the main class representing the LRU cache. It is initialized with a specified `capacity`, and it maintains a dictionary (`cache`) to store the key-value pairs. Additionally, it maintains two sentinel nodes (`head` and `tail`) to simplify insertion and deletion operations.

## Time and Space Efficiency

### Data Structure Choices
- **Doubly Linked List**: The use of a doubly linked list is a key decision here. It allows for constant-time insertions and deletions at both the front and back of the list, making it efficient for maintaining the order of recently used items.
- **Dictionary**: The dictionary (`cache`) is used to store key-value pairs. This provides O(1) access time to any item in the cache.

### `get` Method
- The `get` method is used to retrieve a value from the cache based on a given key. 
- Time Efficiency: The dictionary provides O(1) access to the item, and then the `_remove` and `_add_to_front` methods are used to update the linked list in constant time.
- Space Efficiency: No additional memory is allocated for this operation.

### `set` Method
- The `set` method is used to add a new item to the cache.
- Time Efficiency: The method first checks if the key is already in the cache. If it is, the item is removed and added to the front of the linked list. If the cache is full, the least recently used item is removed (from the end of the linked list). Insertion is done in O(1) time.
- Space Efficiency: No additional memory is allocated for this operation.

In summary, the choice of a doubly linked list and a dictionary data structure for this LRU cache implementation ensures efficient time and space complexity for operations like adding, accessing, and evicting items. The test cases confirm that the implementation works correctly and efficiently in various scenarios.