def sqrt(number):
    # Base case: If the number is 0 or 1, the square root is the number itself
    if number == 0 or number == 1:
        return number

    if number < 0:
        return None

    # Use binary search to find the square root
    left, right = 1, number
    result = 0
    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid

        if square == number:
            return mid
        elif square < number:
            left = mid + 1
            result = mid
        else:
            right = mid - 1

    return result

# Test cases
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (None == sqrt(-25)) else "Fail")
print("Pass" if (None == sqrt(-1)) else "Fail")