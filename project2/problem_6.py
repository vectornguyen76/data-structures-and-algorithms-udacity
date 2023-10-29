class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    set1 = set()
    set2 = set()

    union_list = LinkedList()

    current1 = llist_1.head
    while current1 is not None:
        set1.add(current1.value)
        current1 = current1.next

    current2 = llist_2.head
    while current2 is not None:
        set2.add(current2.value)
        current2 = current2.next

    union_set = set1.union(set2)
    for value in union_set:
        union_list.append(value)

    return union_list

def intersection(llist_1, llist_2):
    # Your Solution Here
    set1 = set()
    set2 = set()

    intersection_list = LinkedList()

    current1 = llist_1.head
    while current1 is not None:
        set1.add(current1.value)
        current1 = current1.next

    current2 = llist_2.head
    while current2 is not None:
        set2.add(current2.value)
        current2 = current2.next

    intersection_set = set1.intersection(set2)
    for value in intersection_set:
        intersection_list.append(value)

    return intersection_list


# Test case 1
print("Test Case 1")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print ("Union:", union(linked_list_1,linked_list_2))
print ("Intersection:", intersection(linked_list_1,linked_list_2))

# Test case 2
print("Test Case 2")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print ("Union:", union(linked_list_3,linked_list_4))
print ("Intersection:", intersection(linked_list_3,linked_list_4))

# Test case 3: One set is empty
print("Test Case 3: One set is empty")
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
# Leave element_2 empty

for i in element_1:
    linked_list_5.append(i)

for i in []:
    linked_list_6.append(i)

print("Union:", union(linked_list_5, linked_list_6))  # Expecting the same as linked_list_5
print("Intersection:", intersection(linked_list_5, linked_list_6))  # Expecting an empty list

# Test case 4: Both sets are empty
print("Test Case 4: Both sets are empty")
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []  # Empty list
element_2 = []  # Empty list

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print("Union:", union(linked_list_7, linked_list_8))  # Expecting an empty list
print("Intersection:", intersection(linked_list_7, linked_list_8))  # Expecting an empty list
