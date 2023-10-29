# Problem 3: Rearrange Array Digits

This repository contains a Python function, `rearrange_digits(input_list)`, that takes a list of non-negative integers and rearranges the digits in the list to form two new integers. The function employs a merge sort algorithm to sort the input list in descending order and then distributes the digits alternately to create two large integers.

## Reasoning Behind Code Decisions

1. **Merge Sort**: The code uses the merge sort algorithm to efficiently sort the input list in descending order. Merge sort is chosen for its stability and efficiency in handling larger lists.

2. **Splitting the List**: The `merge_sort` function first divides the input list into two halves and recursively sorts each half. This division and sorting process continues until the base case is reached, where the list size is 1 or less.

3. **Merging the Halves**: The `merge` function is responsible for merging two sorted lists into one sorted list. It compares elements from both lists and appends the larger element to the result list. This ensures the final sorted list is in descending order.

4. **Creating the Two Numbers**: After obtaining the sorted list, the code iterates through it and creates two new integers, `num1` and `num2`, by alternatively adding digits from the sorted list. This process results in two integers with the maximum possible values.

5. **Efficiency**: The time complexity of this solution is O(n log(n)), where n is the number of digits in the input list. This is due to the merge sort algorithm, which has a time complexity of O(n log(n)). The space complexity is O(n) because the merge sort process requires additional memory proportional to the size of the input list.