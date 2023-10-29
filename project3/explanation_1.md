# Problem 2: Search in a Rotated Sorted Array

This repository contains a Python function, `sqrt(number)`, that calculates the square root of a given number. The function utilizes binary search to efficiently find the square root while minimizing time and space complexity.

## Reasoning Behind Code Decisions

1. **Base Case**: The code starts by checking for the base case where the input number is either 0 or 1. In these cases, the square root is the number itself. This simple check optimizes the function for common and trivial cases, avoiding the need for further computation.

2. **Binary Search**: For numbers greater than 1, the code employs a binary search algorithm to find the square root. Binary search is an efficient approach for this problem because it eliminates half of the possibilities with each iteration. By repeatedly narrowing the search range, it quickly converges to the square root. 

3. **Variable Initialization**: The `left` and `right` pointers define the search range, and the `result` variable stores the best approximation of the square root. The algorithm keeps updating the `result` whenever it encounters a square that is less than or equal to the input number.

4. **Loop and Midpoint Calculation**: The code enters a loop that continues as long as the `left` pointer is less than or equal to the `right` pointer. In each iteration, it calculates the midpoint `mid` between `left` and `right`. This is done using integer division to avoid floating-point precision issues.

5. **Comparison and Update**: The code calculates the square of the `mid` value and compares it to the input number. Depending on the comparison, it updates the `left`, `right`, and `result` variables. The algorithm ensures the search space is halved at each step until it finds the square root or a close approximation.

6. **Efficiency**: The time complexity of this solution is O(log(n)), where n is the input number. Binary search reduces the search space by half in each iteration, resulting in a logarithmic time complexity. The space complexity is O(1) as it only uses a few variables to store intermediate values.
