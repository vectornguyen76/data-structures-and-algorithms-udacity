# Problem 2: Search in a Rotated Sorted Array

This repository contains a Python function, `rotated_array_search(input_list, number)`, which is designed to search for a target number within a rotated (circularly shifted) sorted array. The function employs a binary search algorithm to efficiently find the target number's index in the array.

## Reasoning Behind Code Decisions

1. **Binary Search**: The primary algorithm used in this code is binary search. Binary search is chosen for its efficiency in searching in sorted arrays. The binary search algorithm iteratively halves the search space, making it efficient for large datasets.

2. **Search Space**: The code maintains two pointers, `left` and `right`, that represent the current search space. The initial search space is the entire input array, with `left` starting at index 0 and `right` starting at the last index of the array. These pointers define the range in which the code searches for the target number.

3. **Midpoint Calculation**: In each iteration, the code calculates the midpoint, `mid`, as the average of `left` and `right`. It uses integer division to ensure `mid` is an integer.

4. **Comparison and Update**: The code compares the element at the `mid` index with the target number. If they match, the function returns the index `mid`. If not, the code checks if the left half of the search space is sorted (i.e., if `input_list[left]` is less than or equal to `input_list[mid]`). If it is, the code determines whether the target number is in the left half. If the left half is not sorted, then the right half is sorted, and the code determines whether the target number is in the right half. Based on these comparisons, the `left` and `right` pointers are updated to narrow down the search space.

5. **Efficiency**: The time complexity of this solution is O(log(n)), where n is the size of the input array. Binary search divides the search space in half with each iteration, resulting in logarithmic time complexity. The space complexity is O(1) since it uses only a constant amount of additional memory to store pointers and indices.
