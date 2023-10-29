# Problem 6: Union and Intersection

This code defines a simple singly-linked list data structure using two classes, `Node` and `LinkedList`, and provides functions for finding the union and intersection of two linked lists.

## `Node` Class

The `Node` class represents a node in the linked list. It has the following attributes and methods:

- `value`: The value stored in the node.
- `next`: Reference to the next node in the linked list.

## `LinkedList` Class

The `LinkedList` class represents a linked list and includes the following methods:

- `append(self, value)`: Appends a new node with the given value to the end of the linked list.
- `size(self)`: Returns the size (number of nodes) of the linked list.
- `__str__(self)`: Returns a string representation of the linked list, displaying the values in the list in order.

## `union(llist_1, llist_2)` Function

This function takes two linked lists, `llist_1` and `llist_2`, and finds the union of their elements. The union of two sets is a new set containing all distinct elements from both sets. The function uses Python's `set` data structure to perform this operation. It iterates through both linked lists, adding the elements to two sets (`set1` and `set2`), and then finds the union of these sets. The resulting elements are appended to a new linked list called `union_list`.

## `intersection(llist_1, llist_2)` Function

This function takes two linked lists, `llist_1` and `llist_2`, and finds the intersection of their elements. The intersection of two sets is a new set containing elements that are common to both sets. Like the `union` function, it uses sets to perform this operation. It iterates through both linked lists, adding the elements to two sets (`set1` and `set2`), and then finds the intersection of these sets. The resulting elements are appended to a new linked list called `intersection_list`.

## Efficiency

- The `append` method has a time complexity of O(n), where 'n' is the number of elements in the linked list. Appending an element to the end of the list requires iterating through the list to find the last node.

- The `size` method has a time complexity of O(n) since it also requires iterating through the entire list to count the number of nodes.

- The `union` and `intersection` functions have a time complexity of O(m + n), where 'm' and 'n' are the sizes of the input linked lists. This is because both functions iterate through both linked lists once to create sets of elements and then perform set operations (union and intersection), which have a time complexity of O(min(m, n)). The overall space complexity of these functions is also O(m + n) due to the sets created.

- The use of sets ensures that the result of union and intersection operations contains distinct elements.