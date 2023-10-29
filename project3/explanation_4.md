# Problem 4: Dutch National Flag Problem

This repository contains a Python function, `sort_012(input_list)`, which sorts an input list containing only the elements 0, 1, and 2 in ascending order. The function utilizes the Dutch National Flag algorithm to efficiently sort the input list.

## Reasoning Behind Code Decisions

1. **Dutch National Flag Algorithm**: The code uses the Dutch National Flag algorithm to sort the list efficiently. This algorithm is designed to sort an array containing three distinct elements and is well-suited for this problem.

2. **Pointers for 0, 1, and 2**: The code initializes three pointers: `low`, `mid`, and `high`. These pointers represent the current positions for the numbers 0, 1, and 2 in the sorted array, respectively.

3. **Iterating Through the List**: The code uses a `while` loop that continues until the `mid` pointer reaches the end of the list (`high`). It examines the element at the `mid` position and performs the following actions:
   - If the element is 0, it swaps the element at `mid` with the element at `low` and increments both `low` and `mid` pointers. This moves the 0 to the correct position.
   - If the element is 1, it increments the `mid` pointer. Since 1s should appear in the middle of the sorted list, no swap is necessary.
   - If the element is 2, it swaps the element at `mid` with the element at `high` and decrements the `high` pointer. This moves the 2 to the correct position.

4. **Efficiency**: The Dutch National Flag algorithm is highly efficient for sorting in linear time, and it sorts the list in a single pass. The time complexity is O(n), where n is the length of the input list, and the space complexity is O(1) since it uses only a constant amount of additional memory.
